import pytest
from selenium.webdriver.common.by import By

@pytest.mark.basic
@pytest.mark.regression
def test_notification(browser):
    browser.get("https://the-internet.herokuapp.com/notification_message_rendered")

    button = browser.find_element(By.XPATH, "//a [text()='Click here']")
    button.click()
    correct_text = "Action successful"

    message = browser.find_element(By.XPATH, "//*[@id='flash']")
    clean_text = message.text.replace('×', '').strip()

    while clean_text != correct_text:
        browser.implicitly_wait(10)
        message = browser.find_element(By.XPATH, "//*[@id='flash']")
        clean_text = message.text.replace('×', '').strip()
        button = browser.find_element(By.XPATH, "//a [text()='Click here']")
        button.click()
    assert clean_text == correct_text, 'Совпадение не прошло проверку. Текст не совпадает эталонному'