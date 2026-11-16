import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


@pytest.mark.basic
@pytest.mark.regression
def test_dropdown(browser):
    browser.get("https://the-internet.herokuapp.com/dropdown")

    dropdown = browser.find_element(By.XPATH, '//*[@id="dropdown"]')
    expected_options = ["Please select an option", "Option 1", "Option 2"]
    select = Select(dropdown)
    options = select.options
    options_list = [opt.text for opt in options]
    assert expected_options == options_list, 'Одной из опций нет в списке'

    select.select_by_value(value='1')
    assert select.first_selected_option.text == 'Option 1', 'Option 1 не выбран'
    select.select_by_value(value='2')
    assert select.first_selected_option.text == 'Option 2', 'Option 2 не выбран'

