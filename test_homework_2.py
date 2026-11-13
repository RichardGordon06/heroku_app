import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
@pytest.mark.regression
@pytest.mark.smoke
def test_checkbox(browser):
    checkbox_1 = browser.find_element(By.XPATH, '//*[@id="checkboxes"]/input[1]')

    assert checkbox_1.is_selected() == False, "Чек-бокс выбран, ошибка"
    checkbox_1.click()
    browser.implicitly_wait(5)
    assert checkbox_1.is_selected() == True, "Чек-бокс не выбран, ошибка"

    checkbox_2 = browser.find_element(By.XPATH, '//*[@id="checkboxes"]/input[2]')

    assert checkbox_2.is_selected() == True, "Чек-бокс не выбран, ошибка"
    checkbox_2.click()
    browser.implicitly_wait(5)
    assert checkbox_2.is_selected() == False, "Чек-бокс выбран, ошибка"

    print('Успех')
