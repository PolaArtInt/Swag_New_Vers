class FormData:
    form_url = 'https://victoretc.github.io/webelements_information/'
    form_header = 'Register'
    form_name = ('xpath', '//input[@id="username"]')
    form_pass = ('xpath', '//input[@id="password"]')
    form_check = ('xpath', '//input[@id="agreement"]')
    form_reg_btn = ('xpath', '//button[@id="registerButton"]')


class AuthPage:
    input_user = ('xpath', '//input[@id="user-name"]')
    input_pass = ('xpath', '//input[@id="password"]')
    login_btn = ('xpath', '//input[@id="login-button"]')

    locked_msg = 'Epic sadface: Sorry, this user has been locked out.'
    login_err_msg = 'Epic sadface: Username and password do not match any user in this service'


class Menu:
    menu_btn = ('xpath', '//div[@class="bm-burger-button"]//button')
    all_items_btn = ('xpath', '//a[@id="inventory_sidebar_link"]')
    about_btn = ('xpath', '//a[@id="about_sidebar_link"]')
    logout_btn = ('xpath', '//a[@id="logout_sidebar_link"]')
    reset_btn = ('xpath', '//a[@id="reset_sidebar_link"]')
    x_btn = ('xpath', '//div[@class="bm-cross-button"]/button')


class InventoryPage:
    prod_header = ('xpath', '//div[@class="product_label"]')

    item_cards = ('xpath', '//div[@class="inventory_item"]')
    item_imgs = ('xpath', '//img[@class="inventory_item_img"]')
    item_names = ('xpath', '//div[@class="inventory_item_name"]')
    item_descs = ('xpath', '//div[@class="inventory_item_desc"]')
    item_prices = ('xpath', '//div[@class="inventory_item_price"]')

    add_btns = ('xpath', '//button[@class="btn_primary btn_inventory"]')
    remove_btns = ('xpath', '//button[@class="btn_secondary btn_inventory"]')

    drop_a_z = ('xpath', '//option[@value="az"]')
    drop_z_a = ('xpath', '//option[@value="za"]')
    drop_low_high = ('xpath', '//option[@value="lohi"]')
    drop_high_low = ('xpath', '//option[@value="hilo"]')


class ItemPage:
    card_add_btn = ('xpath', '//button[@class="btn_primary btn_inventory"]')
    card_remove_btn = ('xpath', '//button[@class="btn_secondary btn_inventory"]')

    card_img = ('xpath', '//img[@class="inventory_details_img"]')
    card_name = ('xpath', '//div[@class="inventory_details_name"]')
    card_desc = ('xpath', '//div[@class="inventory_details_desc"]')
    card_price = ('xpath', '//div[@class="inventory_details_price"]')


class CartPage:
    # cart icon:
    cart_header = ('xpath', '//div[@class="subheader"]')
    cart_btn = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]')
    cart_tag = ('xpath', '//a[@class="shopping_cart_link fa-layers fa-fw"]/span')
    cart_quantity_tag = '//a[@class="shopping_cart_link fa-layers fa-fw"]/span'

    # item details:
    cart = ('xpath', '//div[@id="cart_contents_container"]')
    cart_item_name = ('xpath', '//div[@class="inventory_item_name"]')
    cart_item_desc = ('xpath', '//div[@class="inventory_item_desc"]')
    cart_price = ('xpath', '//div[@class="inventory_item_price"]')
    cart_quantity_num = ('xpath', '//div[@class="cart_quantity"]')
    cart_remove_btn = ('xpath', '//button[@class="btn_secondary cart_button"]')


class CheckoutPage:
    input_fname = ('xpath', '//input[@id="first-name"]')
    input_lname = ('xpath', '//input[@id="last-name"]')
    input_zipcode = ('xpath', '//input[@id="postal-code"]')

    checkout_btn = ('xpath', '//a[@class="btn_action checkout_button"]')
    continue_btn = ('xpath', '//input[@class="btn_primary cart_button"]')
    finish_btn = ('xpath', '//a[@class="btn_action cart_button"]')
    cancel_btn = ('xpath', '//a[@class="cart_cancel_link btn_secondary"]')

    complete_msg = 'THANK YOU FOR YOUR ORDER'


class AboutPage:
    exp_title = 'Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing'
