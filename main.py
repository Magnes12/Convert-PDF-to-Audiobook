from gtts import gTTS
import os
import PyPDF2

pdf_path = './test.pdf'

with open(pdf_path, 'rb') as pdf_file:
    read_pdf = PyPDF2.PdfReader(pdf_file)
    number_of_pages = len(read_pdf.pages)
    page = read_pdf.pages[0]
    page_content = page.extract_text()

pdf_file_name = os.path.basename(pdf_path)

my_text = page_content
language = 'en'

my_obj = gTTS(text=my_text, lang=language, slow=False)
my_obj.save(f'{pdf_file_name}_ebook.mp3')

os.system(f'{pdf_file_name}_ebook.mp3')
