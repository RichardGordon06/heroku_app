import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.basic
@pytest.mark.regression
def test_hovers(browser):
    browser.get("https://the-internet.herokuapp.com/hovers")

    target_element_1 = browser.find_element(By.CSS_SELECTOR, "div.example :nth-child(3)")
    actions = ActionChains(browser)
    actions.move_to_element(target_element_1).perform()
    name_profile_1 = browser.find_element(By.CSS_SELECTOR, "div.example :nth-child(3) > .figcaption > h5")
    assert name_profile_1.text == 'name: user1', 'Текст не совпадает, ОШИБКА'
    view_profile_1 = browser.find_element(By.CSS_SELECTOR, "div.example :nth-child(3) > .figcaption > a")
    view_profile_1.click()
    error = browser.find_element(By.CSS_SELECTOR, "h1")
    assert error.text == 'Not Found', 'Страница загрузилась не корректно, нет ошибки!'

    browser.back()

    target_element_2 = browser.find_element(By.CSS_SELECTOR, "div.example :nth-child(4)")
    actions = ActionChains(browser)
    actions.move_to_element(target_element_2).perform()
    name_profile_2 = browser.find_element(By.CSS_SELECTOR, "div.example :nth-child(4) > .figcaption > h5")
    assert name_profile_2.text == 'name: user2', 'Текст не совпадает, ОШИБКА'
    view_profile_2 = browser.find_element(By.CSS_SELECTOR, "div.example :nth-child(4) > .figcaption > a")
    view_profile_2.click()
    error = browser.find_element(By.CSS_SELECTOR, "h1")
    assert error.text == 'Not Found', 'Страница загрузилась не корректно, нет ошибки!'

    browser.back()

    target_element_3 = browser.find_element(By.CSS_SELECTOR, "div.example :nth-child(5)")
    actions = ActionChains(browser)
    actions.move_to_element(target_element_3).perform()
    name_profile_3 = browser.find_element(By.CSS_SELECTOR, "div.example :nth-child(5) > .figcaption > h5")
    assert name_profile_3.text == 'name: user3', 'Текст не совпадает, ОШИБКА'
    view_profile_3 = browser.find_element(By.CSS_SELECTOR, "div.example :nth-child(5) > .figcaption > a")
    view_profile_3.click()
    error = browser.find_element(By.CSS_SELECTOR, "h1")
    assert error.text == 'Not Found', 'Страница загрузилась не корректно, нет ошибки!'