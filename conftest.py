from pathlib import Path
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    download_dir = Path(__file__).parent / "downloads"
    download_dir.mkdir(exist_ok=True)

    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": str(download_dir.resolve()),  # Абсолютный путь к папке
        "download.prompt_for_download": False,  # Не спрашивать, куда сохранить
        "safebrowsing.enabled": True  # Разрешить скачивание любых типов файлов
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    driver.download_dir = download_dir
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()