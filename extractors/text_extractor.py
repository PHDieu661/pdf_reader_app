def extract_text_from_pdf(filepath):
    import pdfplumber
    text_all = []
    with pdfplumber.open(filepath) as pdf:
        for page in pdf.pages:
            text_all.append(page.extract_text() or '')
    return text_all