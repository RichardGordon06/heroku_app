import pytest
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


@pytest.mark.advanced
@pytest.mark.regression
def test_context_menu(browser):
    browser.get("https://the-internet.herokuapp.com/context_menu")
    element = browser.find_element(By.CSS_SELECTOR, "#hot-spot")
    standard = 'You selected a context menu'
    actions = ActionChains(browser)
    actions.move_to_element(element).perform()
    actions.context_click().perform()
    alert = browser.switch_to.alert
    text = alert.text
    assert text == standard, f'Текст алерта {text} не совпадает с ожидаемым {standard}'
    alert.accept()



