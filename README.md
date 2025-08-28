# 📄 PDF Text & OCR Extractor

A Flask web app to extract content from PDF files — supports both native text and OCR from images. Modular architecture makes it easy to upgrade or swap processing components.

Một ứng dụng web dùng Flask để trích xuất nội dung từ file PDF — hỗ trợ cả văn bản gốc và nhận dạng văn bản từ ảnh (OCR). Thiết kế module giúp dễ dàng nâng cấp từng phần xử lý.

---

## 🚀 Features | Tính năng

- Extract text from PDF using `pdfplumber`  
  Trích xuất văn bản từ PDF bằng `pdfplumber`
- OCR from PDF images using `pytesseract` + `pdf2image`  
  Nhận dạng ký tự từ ảnh PDF bằng `pytesseract` + `pdf2image`
- Image preprocessing with `OpenCV` for better OCR accuracy  
  Tiền xử lý ảnh với `OpenCV` để tăng độ chính xác OCR
- Flexible configuration: process text, images, or both  
  Cấu hình linh hoạt: xử lý văn bản, ảnh, hoặc cả hai
- Modular design: easily swap out processing libraries  
  Modular hóa: dễ thay thế từng phần xử lý bằng thư viện khác

---

## 🧰 Installation | Cài đặt

### 1. Create a virtual environment (recommended)  
Tạo môi trường ảo (khuyến nghị)

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 2. Install dependencies  
Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

## 📌 System Requirements | Yêu cầu hệ thống

- Install Poppler for `pdf2image`  
  Cài đặt Poppler để dùng `pdf2image`
- Install Tesseract OCR and Vietnamese language data (`vie`) for OCR  
  Cài đặt Tesseract OCR và ngôn ngữ `vie` để nhận dạng tiếng Việt

---

## 🐳 Docker Support | Hỗ trợ Docker

You can run the app easily using Docker.

Bạn có thể chạy ứng dụng dễ dàng với Docker.

### Build the Docker image | Tạo Docker image

```bash
docker build -t pdf-reader-app .
```

### Run the app in a container | Chạy ứng dụng trong container

```bash
docker run -p 5000:5000 pdf-reader-app
```

The app will be available at [http://localhost:5000](http://localhost:5000).

Ứng dụng sẽ chạy tại [http://localhost:5000](http://localhost:5000).

---