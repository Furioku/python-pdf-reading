import PyPDF2 # reading PDF
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LTTextContainer, LTChar, LTRect, LTFigure # Layout analize and text extracting
import pdfplumber # Text extracting from tabs 
from PIL import Image
from pdf2image import convert_from_path #Img extracting
import pytesseract
import os

# Defining the function for extracting text from file page and indentifining it by font name and size

def text_extraction(element):
    line_text = element.get_text()
    
    line_formats = []
    for text_line in element:
        if isinstance(text_line, LTTextContainer):
            # Iterating through each character in the line of text
            for character in text_line:
                if isinstance(character, LTChar):
                    line_formats.append(character.fontname) # Append the font name
                    line_formats.append(character.size) # Append the font size
    format_per_line = list(set(line_formats))     # Find the unique font sizes and names in the line
    
    return (line_text, format_per_line)

# Нахождение пути к PDF-файлу
pdf_path = 'test_task.pdf'

# создание объекта PDF-файла
pdfFileObj = open(pdf_path, 'rb')
# создание объекта для чтения PDF-файлов
pdfReaded = PyPDF2.PdfReader(pdfFileObj)

# Создание словаря для извлечения текста из каждого изображения
text_per_page = {}
# Мы извлекаем страницы из PDF-файла
for pagenum, page in enumerate(extract_pages(pdf_path)):
    
    # Инициализация переменных, необходимых для извлечения текста со страницы
    page_obj = pdfReaded.pages[pagenum]
    page_text = []
    line_format = []
    page_content = []
    
    pdf = pdfplumber.open(pdf_path)



    # Нахождение всех элементов
    page_elements = [(element.y1, element) for element in page._objs]
    # Сортировка всех элементов по мере их появления на странице
    page_elements.sort(key=lambda a: a[0], reverse=True)

    # Поиск элементов, из которых состоит страница
    for i,component in enumerate(page_elements):
        # Извлечение положения верхней стороны элемента в PDF
        pos= component[0]
        # Извлечение элемента макета страницы
        element = component[1]
        
        # Проверка того, является ли элемент текстовым
        if isinstance(element, LTTextContainer):
            (line_text, format_per_line) = text_extraction(element)
            # Добавление текста каждой строки к тексту страницы
            page_text.append(line_text)
            # Добавление формата для каждой строки, содержащей текст
            line_format.append(format_per_line)
            page_content.append(line_text)
            

    # Создание ключа словаря
    dctkey = 'Page_'+str(pagenum)
    # Добавить список списков в качестве значения ключа страницы
    text_per_page[dctkey]= [page_text, line_format, page_content]

pdfFileObj.close()
# Page content representation
result = ''.join(text_per_page['Page_0'][2])
print(result)