import os
from flask import Flask, request, render_template, redirect, url_for
import pdfplumber
from pdf2image import convert_from_path
import pytesseract
import cv2
import numpy as np
from PIL import Image

# Cấu hình
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Kiểm tra đuôi file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Tiền xử lý ảnh để OCR
def preprocess_image(pil_img):
    img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2GRAY)
    _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return thresh

# Route chính
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            
            # 1. Trích text gốc
            text_all = []
            with pdfplumber.open(filepath) as pdf:
                for page in pdf.pages:
                    text_all.append(page.extract_text() or '')

            # 2. OCR trên ảnh
            ocr_all = []
            pages = convert_from_path(filepath, dpi=300)
            for img in pages:
                processed = preprocess_image(img)
                txt = pytesseract.image_to_string(processed, lang='vie', config='--psm 3')
                ocr_all.append(txt)

            # Kết hợp kết quả
            combined = []
            for i in range(len(text_all)):
                combined.append({
                    'page': i + 1,
                    'text_raw': text_all[i].strip(),
                    'text_ocr': ocr_all[i].strip()
                })

            return render_template('index.html', results=combined)

    return render_template('index.html', results=None)

if __name__ == '__main__':
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    app.run(debug=True)