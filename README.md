# 📄 PDF Text & OCR Extractor

Một ứng dụng web đơn giản dùng Flask để trích xuất nội dung từ file PDF — bao gồm cả text gốc và text từ ảnh thông qua OCR.

## 🚀 Tính năng

- Trích xuất text từ PDF bằng `pdfplumber`
- Chuyển đổi PDF sang ảnh bằng `pdf2image`
- Nhận dạng ký tự quang học (OCR) bằng `pytesseract`
- Tiền xử lý ảnh với `OpenCV` để tăng độ chính xác OCR
- Hiển thị kết quả từng trang: text gốc vs text OCR

## 🧰 Cài đặt

```bash
pip install -r requirements.txt


