from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_COUNT = (By.ID, 'nav-cart-count')
PRODUCT_NAME = (By.CSS_SELECTOR, '#sc-active-cart li')


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    actual_count = context.driver.find_element(*CART_COUNT).text
    assert actual_count == expected_count, f'Expected {expected_count} item(s), but got {actual_count} item(s)'


@then('Verify cart has correct product')
def verify_product_name(context):
    cart_product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Product name in cart: {cart_product_name}')
    assert cart_product_name == context.current_product_name, \
        f'Expected "{context.current_product_name}" product, but got "{cart_product_name}"'
