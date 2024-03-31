# auth page:
input_user = '//input[@id="user-name"]'
input_pass = '//input[@id="password"]'
login_btn = '//input[@id="login-button"]'

locked_msg = 'Epic sadface: Sorry, this user has been locked out.'
login_err_msg = 'Epic sadface: Username and password do not match any user in this service'

# menu:
menu_btn = '//div[@class="bm-burger-button"]//button'
all_items_btn = '//a[@id="inventory_sidebar_link"]'
about_btn = '//a[@id="about_sidebar_link"]'
logout_btn = '//a[@id="logout_sidebar_link"]'
reset_btn = '//a[@id="reset_sidebar_link"]'
x_btn = '//div[@class="bm-cross-button"]/button'

# inventory page:
prod_header = '//div[@class="product_label"]'

drop_a_z = '//option[@value="az"]'
drop_z_a = '//option[@value="za"]'
drop_low_high = '//option[@value="lohi"]'
drop_high_low = '//option[@value="hilo"]'

item_imgs = '//img[@class="inventory_item_img"]'
item_names = '//div[@class="inventory_item_name"]'
item_descs = '//div[@class="inventory_item_desc"]'
item_prices = '//div[@class="inventory_item_price"]'

add_btns = '//button[@class="btn_primary btn_inventory"]'
remove_btns = '//button[@class="btn_secondary btn_inventory"]'

# item card page:
card_add_btn = '//button[@class="btn_primary btn_inventory"]'
card_remove_btn = '//button[@class="btn_secondary btn_inventory"]'

card_img = '//img[@class="inventory_details_img"]'
card_name = '//div[@class="inventory_details_name"]'
card_desc = '//div[@class="inventory_details_desc"]'
card_price = '//div[@class="inventory_details_price"]'

# cart page:
cart_header = '//div[@class="subheader"]'
cart_btn = '//a[@class="shopping_cart_link fa-layers fa-fw"]'
cart_tag = '//a[@class="shopping_cart_link fa-layers fa-fw"]/span'
cart_remove_btn = '//button[@class="btn_secondary cart_button"]'

# checkout page:
input_fname = '//input[@id="first-name"]'
input_lname = '//input[@id="last-name"]'
input_zipcode = '//input[@id="postal-code"]'

checkout_btn = '//a[@class="btn_action checkout_button"]'
continue_btn = '//input[@class="btn_primary cart_button"]'
finish_btn = '//a[@class="btn_action cart_button"]'
cancel_btn = '//a[@class="cart_cancel_link btn_secondary"]'

complete_msg = 'THANK YOU FOR YOUR ORDER'

# about page:
exp_title = 'Sauce Labs: Cross Browser Testing, Selenium Testing & Mobile Testing'
