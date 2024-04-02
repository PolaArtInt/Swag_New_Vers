import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


# driver init:
@pytest.fixture(scope="function", autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'normal'

    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--window-size=1280,800")
    chrome_options.add_argument("--disable-cache")

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=chrome_options, service=service)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
