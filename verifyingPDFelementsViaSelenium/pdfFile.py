from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from seleniumEnvironmentSetUp import *

PDF_CONTENT = "//div[@class = 'ndfHFb-c4YZDc-cYSp0e-DARUcf-PLDbbf']"

pdf_file_url = "https://drive.google.com/file/d/1j44kRGKteLgsklXJmGw3fc-1EjIn3uQF/view"


@given('User enters to pdf file via provided link')
def open_pdf_file(context):
    open_page(context, pdf_file_url)

@then('User verifies that pdf file contains content')
def assert_if_content_present(context):
    WebDriverWait(context.driver, 20).until(EC.visibility_of_element_located((By.XPATH, PDF_CONTENT)))

