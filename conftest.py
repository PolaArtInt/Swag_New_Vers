from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest
from data import *
from locators import *


# driver init:
@pytest.fixture(scope="function", autouse=True)
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'normal'

    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--window-size=1280,800")
    # chrome_options.add_argument("--disable-cache")

    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=chrome_options, service=service)
    browser.implicitly_wait(5)

    yield browser
    browser.quit()


@pytest.fixture()
def standard_auth(browser):
    browser.get(URLs.url)
    browser.find_element(*AuthPage.input_user).send_keys(Auth.user)
    browser.find_element(*AuthPage.input_pass).send_keys(Auth.pass_word)
    browser.find_element(*AuthPage.login_btn).click()


@pytest.fixture()
def problem_auth(browser):
    browser.get(URLs.url)
    browser.find_element(*AuthPage.input_user).send_keys(Auth.problem_user)
    browser.find_element(*AuthPage.input_pass).send_keys(Auth.pass_word)
    browser.find_element(*AuthPage.login_btn).click()


@pytest.fixture()
def locked_out_auth(browser):
    browser.get(URLs.url)
    browser.find_element(*AuthPage.input_user).send_keys(Auth.locked_user)
    browser.find_element(*AuthPage.input_pass).send_keys(Auth.pass_word)
    browser.find_element(*AuthPage.login_btn).click()


@pytest.fixture()
def glitch_auth(browser):
    browser.get(URLs.url)
    browser.find_element(*AuthPage.input_user).send_keys(Auth.glitch_user)
    browser.find_element(*AuthPage.input_pass).send_keys(Auth.pass_word)
    browser.find_element(*AuthPage.login_btn).click()

