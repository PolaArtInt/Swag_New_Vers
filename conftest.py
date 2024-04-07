from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
import pytest
from locators import FormData, AuthPage
from data import URLs, Auth


@pytest.fixture
def options():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.page_load_strategy = 'normal'

    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--window-size=1280,1000")
    chrome_options.add_argument("--incognito")
    return chrome_options


@pytest.fixture(scope="function", autouse=True)
def browser(options):
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(options=options, service=service)

    yield browser
    browser.quit()


@pytest.fixture()
def imp_wait(browser):
    browser.implicitly_wait(5)
    return imp_wait


@pytest.fixture()
def wait(browser):
    wait = WebDriverWait(browser, timeout=10)
    return wait


@pytest.fixture()
def form_conditions(browser):
    browser.get(FormData.form_url)
    assert browser.current_url == FormData.form_url and \
           FormData.form_header == 'Register'

    name_field = browser.find_element(*FormData.form_name)
    pass_field = browser.find_element(*FormData.form_pass)
    checkbox = browser.find_element(*FormData.form_check)

    if checkbox.is_selected() or name_field.text != '' or pass_field.text != '':
        checkbox.click()
        name_field.clear()
        pass_field.clear()

    assert name_field.text == '', 'Input Email is filled'
    assert pass_field.text == '', 'Input Password is filled'
    assert not checkbox.is_selected(), 'Checkbox is selected'

    yield form_conditions
    # browser.get(FormData.form_url)


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

