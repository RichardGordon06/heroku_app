import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


@pytest.mark.basic
@pytest.mark.regression
@pytest.mark.smoke
def test_inputs(browser):
    browser.get("https://the-internet.herokuapp.com/inputs")

    input_element = browser.find_element(By.CSS_SELECTOR, 'input:nth-child(2)')
    browser.implicitly_wait(10)

    input_element.send_keys(Keys.ARROW_UP)
    input_text = input_element.get_attribute("value")
    assert input_text == "1", 'Значение в строке не = 1, ОШИБКА'
    input_element.clear()

    input_element.send_keys(Keys.ARROW_DOWN)
    input_text = input_element.get_attribute("value")
    assert input_text == "-1", 'Значение в строке не = -1, ОШИБКА'
    input_element.clear()

    input_element.send_keys('123')
    input_text = input_element.get_attribute("value")
    print(input_text)
    assert input_text == '123', 'Цифровые значения не могут введены в строку, ошибка'
