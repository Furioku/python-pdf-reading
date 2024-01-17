#File to extract images from file, but as barcodes seems not to be an PNG it does not recognize it
from spire.pdf.common import *
from spire.pdf import *



doc = PdfDocument()
doc.LoadFromFile('ExampleForExtractingPNG.pdf')

for i in range(doc.Pages.Count):
    page = doc.Pages.get_Item(i)

    images = []
    for image in page.ExtractImages():
        images.append(image)

index = 0
for image in images:
    imageFileName = 'C:/Users/Furioku/Documents/GitHub/python-pdf-reading/Extracted/Image-{0:d}.png'.format(index)
    index += 1
    image.Save(imageFileName, ImageFormat.get_Png())
doc.Close()