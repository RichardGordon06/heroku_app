import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.advanced
@pytest.mark.regression
def test_dynamic_control(browser):
    browser.get("https://the-internet.herokuapp.com/dynamic_controls")
    remove_button = browser.find_element(By.CSS_SELECTOR, "#checkbox-example > button ")
    remove_button.click()
    wait = WebDriverWait(browser, 10)
    text_gone = wait.until (EC.visibility_of_element_located((By.CSS_SELECTOR, "form > #message")))
    checkbox_not_visible = wait.until_not(EC.visibility_of_element_located((By.CSS_SELECTOR, "#checkbox > input")))
    assert checkbox_not_visible == True, f'ОШИБКА: чекбок виден на странице (О.Р Чекбокс отсутсвует на странице)'
    input_field = browser.find_element(By.CSS_SELECTOR, "#input-example> input")
    assert input_field.is_enabled() == False, f'ОШИБКА: Поле ввода активно (О.Р Поле неактивно)'
    enable_button = browser.find_element(By.CSS_SELECTOR, "#input-example> button")
    enable_button.click()
    text_enable = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#input-example> p")))
    assert input_field.is_enabled() == True, f'ОШИБКА: Поле ввода неактивно (О.Р Поле активно)'