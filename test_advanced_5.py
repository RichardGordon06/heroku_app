from pathlib import Path
import pytest
import time
from selenium.webdriver.common.by import By


@pytest.mark.advanced
@pytest.mark.regression
def test_download(browser):
    browser.get("https://the-internet.herokuapp.com/download")
    download_dir = Path(__file__).parent / "downloads"
    file = browser.find_element(By.XPATH, "//div[@class='example'] /a[5]")
    file_text = file.text
    target_file = download_dir / file_text
    if target_file.exists():
        target_file.unlink()
    file.click()

    timeout = 10
    while not target_file.exists() and timeout > 0:
        time.sleep(0.5)
        timeout -= 0.5

    assert target_file.exists(), f'ОШИБКА: файл "{file_text}" не найден в папке загрузок!'
    assert target_file.stat().st_size > 0, f'ОШИБКА: скачанный файл "{file_text}" пуст!'