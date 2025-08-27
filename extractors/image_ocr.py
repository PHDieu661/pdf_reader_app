def extract_text_from_images(filepath):
    from pdf2image import convert_from_path
    import pytesseract
    import cv2
    import numpy as np

    def preprocess_image(pil_img):
        img = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2GRAY)
        _, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        return thresh

    pages = convert_from_path(filepath, dpi=300)
    ocr_all = []
    for img in pages:
        processed = preprocess_image(img)
        txt = pytesseract.image_to_string(processed, lang='vie', config='--psm 3')
        ocr_all.append(txt)
    return ocr_all