def fake_it():
    from faker import Faker
    fake = Faker()
    return fake


class Auth:
    user = 'standard_user'
    locked_user = 'locked_out_user'
    problem_user = 'problem_user'
    glitch_user = 'performance_glitch_user'
    pass_word = 'secret_sauce'


class TestAuth:
    wrong_user = 'user'
    wrong_password = 'user'


class URLs:
    url = 'https://www.saucedemo.com/v1/'
    login_url = 'https://www.saucedemo.com/v1/index.html'
    inventory_url = 'https://www.saucedemo.com/v1/inventory.html'
    cart_url = 'https://www.saucedemo.com/v1/cart.html'
    checkout_url = 'https://www.saucedemo.com/v1/checkout-complete.html'
    about_url = 'https://saucelabs.com/'
