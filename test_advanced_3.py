from pathlib import Path
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.advanced
@pytest.mark.regression
def test_upload(browser):
    browser.get("https://the-internet.herokuapp.com/upload")
    file_path = str(Path(__file__).parent.joinpath('file.txt').resolve())
    button = browser.find_element(By.CSS_SELECTOR, 'input#file-upload')
    button.send_keys(file_path)
    button_upload = browser.find_element(By.CSS_SELECTOR, 'input.button')
    button_upload.click()
    uploaded_file = browser.find_element(By.CSS_SELECTOR, '#uploaded-files').text
    assert uploaded_file == 'file.txt', f'ОШИБКА: название {uploaded_file} не совпадает с "file.txt"'