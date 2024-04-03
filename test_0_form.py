import pytest
from locators import *
from data import *


# case 0.1
@pytest.mark.positive
def test_register_btn_unblocked(browser, form_conditions):
    # pre: form_conditions fixture
    # test:
    browser.find_element(*FormData.form_name).send_keys(TestAuth.fake_user_fname)
    browser.find_element(*FormData.form_pass).send_keys(TestAuth.fake_pass)

    checkbox = browser.find_element(*FormData.form_check)
    checkbox.click()
    assert checkbox.is_selected(), 'Checkbox is not checked'

    register_btn = browser.find_element(*FormData.form_reg_btn)
    assert register_btn.is_enabled(), 'Register button is blocked'

    # post: form_conditions fixture


# case 0.2
def test_positive_fill_form_fields(browser, form_conditions):
    pass


# case 0.3
def test_negative_fill_form(browser, form_conditions):
    pass


# case 0.4
def test_empty_fields(browser, form_conditions):
    pass
