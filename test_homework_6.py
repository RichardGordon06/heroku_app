import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
@pytest.mark.smoke
def test_tables(browser):
    browser.get("https://the-internet.herokuapp.com/tables")

    standards_list = ['Smith John jsmith@gmail.com $50.00 http://www.jsmith.com edit delete',
                    'Bach Frank fbach@yahoo.com $51.00 http://www.frank.com edit delete',
                    'Doe Jason jdoe@hotmail.com $100.00 http://www.jdoe.com edit delete',
                    'Conway Tim tconway@earthlink.net $50.00 http://www.timconway.com edit delete']

    table_elements = browser.find_elements(By.XPATH, '//table[1]//tbody/tr')

    for row in table_elements:
        line_text = row.text.strip()
        print(line_text)
        assert line_text in standards_list, f'Текст "{line_text}" отсутствует в эталоне'

