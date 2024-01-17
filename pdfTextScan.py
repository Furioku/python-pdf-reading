import PyPDF2 # reading PDF
from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LTTextContainer, LTChar # Layout analize and text extracting
import pdfplumber # Text extracting from tabs 
from pdf2image import convert_from_path #Img extracting


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

pdf_path = 'test_task.pdf'
pdfFileObj = open(pdf_path, 'rb')
pdfReaded = PyPDF2.PdfReader(pdfFileObj)
text_per_page = {} # Dictionary for text from every PDF page

# Extracting pages from PDF
for pagenum, page in enumerate(extract_pages(pdf_path)):
    
    # Initializing varuables for extracting text 
    page_obj = pdfReaded.pages[pagenum]
    page_text = []
    line_format = []
    page_content = []
    
    pdf = pdfplumber.open(pdf_path) # Open the pdf file
    page_elements = [(element.y1, element) for element in page._objs] # Finding all elements on page
    page_elements.sort(key=lambda a: a[0], reverse=True) # Sorting all the element as they appear in the page

    # Finding the elements that make up the page 
    for i,component in enumerate(page_elements):
        # Determing the position of the element and extracting it from the page layout
        pos = component[0]
        element = component[1]
        
        # Checking if the elemnt is text element and adding text format for every line oo text 
        if isinstance(element, LTTextContainer):
            (line_text, format_per_line) = text_extraction(element)
            page_text.append(line_text) # Adding text of every line to the page text
            line_format.append(format_per_line)
            page_content.append(line_text)
            
    dctkey = 'Page_'+str(pagenum) # Create the key of the dictionary
    text_per_page[dctkey]= [page_text, line_format, page_content] # Add the list of list as value of the page key

pdfFileObj.close()
# Page content representation
result = ''.join(text_per_page['Page_0'][2])
print(result)
