import PyPDF2

def read_text_from_pages(pdf_path, start_page, end_page):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in range(start_page-1, end_page):
            text += reader.pages[page].extract_text()
    return text