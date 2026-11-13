import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
@pytest.mark.regression
def test_dropdown(browser):
    browser.get("https://the-internet.herokuapp.com/dropdown")

    dropdown_elements = browser.find_elements(By.CSS_SELECTOR, 'select > option')
    options_list = [opt.text for opt in dropdown_elements]
    print(options_list)
    assert 'Option 1' in options_list and 'Option 2' in options_list, 'Одной из опций нет в списке'

    dropdown = browser.find_element(By.XPATH, '//*[@id="dropdown"]')
    dropdown.click()

    option_1 = browser.find_element(By.CSS_SELECTOR, '#dropdown > option:nth-child(2)')
    option_1.click()
    browser.implicitly_wait(5)
    assert option_1.is_selected() == True, 'Option 1 не выбран'

    dropdown = browser.find_element(By.XPATH, '//*[@id="dropdown"]')
    dropdown.click()
    option_2 = browser.find_element(By.CSS_SELECTOR, '#dropdown > option:nth-child(3)')
    option_2.click()
    browser.implicitly_wait(5)
    assert option_2.is_selected() == True, 'Option 2 не выборан'
