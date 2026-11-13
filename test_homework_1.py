import pytest
from selenium.webdriver.common.by import By


@pytest.mark.basic
@pytest.mark.regression
@pytest.mark.smoke
def test_add_remove_element(browser):
    browser.get("https://the-internet.herokuapp.com/add_remove_elements/")
    add_element = browser.find_element(By.CSS_SELECTOR, '#content > div > button')
    add_element.click()
    add_element.click()
    delete_elements = browser.find_elements(By.CSS_SELECTOR, '#elements > button')
    assert len(delete_elements) == 2, "Элементов должно быть 2"
    count = len(delete_elements)
    print(count)