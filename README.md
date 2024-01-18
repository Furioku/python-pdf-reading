In this test task I was using certain Python libraries also as Selenium framework with Behave library, such as

PyPDF2 (pip install PyPDF2)

Pdfminer (pip install pdfminer.six)

Pdfplumber (pip install pdfplumber)

Spire.PDF (pip install Spire.PDF)

In file pdfTextScan.py provided solution to the first part of the taks, also in file pdfIMGScan.py there are PNG images scan mobule, so if barcodes in file would be represented as images it would also scan them.

File pdfVerifyStringElements.py contains mechanism to verify what string elements are present in file.

In folder verifyPDFelementsViaSelenium there is test verifying if pdf file contains appropriate conten, if pdf file would be placed in web via link "https://drive.google.com/file/d/1j44kRGKteLgsklXJmGw3fc-1EjIn3uQF/view".

This repo contains automated e2e tests in selenium python

To open project we need:

python

pip

selenium ( pip install selenium )

beahve ( pip install behave )

chrome browser + chromedriver

To run all tests: behave
