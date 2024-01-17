import pdfplumber

searched_element = input("Please enter searched string:\n")
file = 'test_task.pdf'


c = 0
with pdfplumber.open(file) as pdf:
    for page in pdf.pages:
        for line in page.extract_text():
            if searched_element in line:
                c=1
                break


if c == 0: 
	print('String \'', searched_element, '\' Not Found') 
else: 
	print('String \'', searched_element, '\' Is Found In Line', line) 

