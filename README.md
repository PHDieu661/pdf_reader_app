# 📄 PDF Text & OCR Extractor

Ứng dụng web dùng Flask để trích xuất nội dung từ file PDF — hỗ trợ cả văn bản gốc và nhận dạng văn bản từ ảnh (OCR). Thiết kế theo kiến trúc module giúp dễ dàng nâng cấp từng phần xử lý.

---

## 🚀 Tính năng chính

- Trích xuất văn bản từ PDF bằng `pdfplumber`
- Nhận dạng ký tự từ ảnh PDF bằng `pytesseract` + `pdf2image`
- Tiền xử lý ảnh với `OpenCV` để tăng độ chính xác OCR
- Cấu hình linh hoạt: xử lý văn bản, ảnh, hoặc cả hai
- Modular hóa: dễ thay thế từng phần xử lý bằng thư viện khác

---

## 🧰 Cài đặt

### 1. Tạo môi trường ảo (khuyến nghị)

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 2. Cài đặt thư viện
pip install -r requirements.txt

## 📌 Yêu cầu hệ thống:
- Cài đặt Poppler để dùng pdf2image
- Cài đặt Tesseract OCR và ngôn ngữ vie để nhận dạng tiếng Việt