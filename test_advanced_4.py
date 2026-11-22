import pytest
from selenium.webdriver.common.by import By


@pytest.mark.advanced
@pytest.mark.regression
def test_iframe(browser):
    browser.get("https://the-internet.herokuapp.com/iframe")
    iframe = browser.find_element(By.CSS_SELECTOR, "iframe#mce_0_ifr")
    browser.switch_to.frame(iframe)
    text = browser.find_element(By.CSS_SELECTOR, "body#tinymce > p").text
    assert text == 'Your content goes here.', f'ОШИБКА: {text} не соответсвует ожидаемому'
    browser.switch_to.default_content()