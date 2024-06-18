import PyPDF2

# Open the PDF file
def read_pdf(file):
    reader = PyPDF2.PdfReader(file)
    number_of_pages = len(reader.pages)
    text = ""

    # Extract text from each page
    for page_number in range(number_of_pages):
        page = reader.pages[page_number]
        text += page.extract_text()
    return text

def read_page(file, pagenum):
    reader = PyPDF2.PdfReader(file)
    return reader.pages[pagenum].extract_text()

def number_pages(file):
    return len(PyPDF2.PdfReader(file).pages)

from io import StringIO
from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams

def pdf_to_html(file_path, output_path):
    # Open the output file in write mode
    with open(output_path, 'w', encoding='utf-8') as output_file:
        # Use StringIO to temporarily store the extracted HTML content
        output = StringIO()
        with open(file_path, 'rb') as input_file:
            # Extract text and convert to HTMl 
            extract_text_to_fp(input_file, output, laparams=LAParams(),
                       output_type='html', codec=None) 
        # Write the HTML content to the output file
        output_file.write(output.getvalue())
