from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span]")
ADD_TO_CART_BIN = (By.ID, 'add-to-cart-button')
PRODUCT_NAME = (By.ID, 'productTitle')


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Store product name')
def get_product_name(context):
    context.current_product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.current_product_name}')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    # if Subscribe & Save is appear in the desktop buybox
    buybox_rows = context.driver.find_elements(By.CSS_SELECTOR, "#newAccordionRow i.a-icon-radio-inactive")
    if buybox_rows:
        buybox_rows[1].click()

    context.driver.find_element(*ADD_TO_CART_BIN).click()
    sleep(1)
    # Check if there is special plane appear
    cancel_buttons = context.driver.find_elements(By.CSS_SELECTOR, "#attachSiNoCoverage input.a-button-input")
    if len(cancel_buttons):
        cancel_buttons[0].click()
        sleep(1)
