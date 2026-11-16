import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
@pytest.mark.regression
def test_text(browser):
    browser.get("https://the-internet.herokuapp.com/typos")

    correct_text = "Sometimes you'll see a typo, other times you won't."
    element = browser.find_element(By.CSS_SELECTOR, 'div.example :nth-child(3)')
    expected_text = element.text

    attempts = 0
    while correct_text != expected_text and attempts < 15:
        browser.refresh()
        element = browser.find_element(By.CSS_SELECTOR, 'div.example :nth-child(3)')
        expected_text = element.text
        browser.implicitly_wait(10)
        attempts += 1

    assert correct_text == expected_text, 'Совпадение не прошло проверку. Текст не совпадает эталонному'
