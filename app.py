import os
import subprocess
from flask import Flask, request, render_template, redirect, url_for

# Import từ các module đã tách
from extractors.config import PROCESS_TEXT, PROCESS_IMAGE
from extractors.text_extractor import extract_text_from_pdf
from extractors.image_ocr import extract_text_from_images

# Cấu hình thư mục upload
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Kiểm tra đuôi file hợp lệ
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)

            # Lấy thông tin PDF bằng pdfinfo
            try:
                result = subprocess.run(['pdfinfo', filepath], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                pdf_info = result.stdout if result.returncode == 0 else f"Lỗi khi gọi pdfinfo: {result.stderr}"
            except Exception as e:
                pdf_info = f"Lỗi hệ thống: {str(e)}"

            # Trích xuất văn bản
            text_all = extract_text_from_pdf(filepath) if PROCESS_TEXT else []

            # Trích xuất OCR từ ảnh
            ocr_all = extract_text_from_images(filepath) if PROCESS_IMAGE else []

            # Ghép kết quả theo từng trang
            combined = []
            max_pages = max(len(text_all), len(ocr_all))
            for i in range(max_pages):
                combined.append({
                    'page': i + 1,
                    'text_raw': text_all[i] if i < len(text_all) else '',
                    'text_ocr': ocr_all[i] if i < len(ocr_all) else ''
                })

            return render_template('index.html', results=combined, pdf_info=pdf_info)

    return render_template('index.html', results=None)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(host='0.0.0.0', port=5000, debug=True)