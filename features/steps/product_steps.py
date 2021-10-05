from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART_BIN = (By.ID, 'add-to-cart-button')
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span]")
PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')
    context.driver.refresh()


@when('Click on the first product')
def click_first_product(context):
    context.driver.refresh()
    context.driver.find_element(*PRODUCT_PRICE).click()


@when('Store product name')
def get_product_name(context):
    context.driver.refresh()
    context.current_product_name = context.driver.find_element(*PRODUCT_NAME).text
    print(f'Current product: {context.current_product_name}')


@when('Click on Add to cart button')
def click_add_to_cart(context):
    # if Subscribe & Save is appear in the desktop buybox
    buybox_rows = context.driver.find_elements(By.CSS_SELECTOR, "#newAccordionRow i.a-icon-radio-inactive")
    if buybox_rows:
        buybox_rows[1].click()

    e = context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BIN),
                                  message='Can not clickable on Cart button')
    e.click()
    # Check if there is special plane appear
    cancel_buttons = context.driver.find_elements(By.CSS_SELECTOR, "#attachSiNoCoverage input.a-button-input")
    if len(cancel_buttons):
        context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART_BIN)).click()


@then('Verify user can click through colors')
def verify_user_can_click_through_colors(context):
    expected_color = """
        Brown Snake Print
        Bright White Modena Calf Leather 2
        Bright Red
        Bright White
        Red
        Baltic Navy
        Black Leather
        Ntrl Flrl Prt
        Mineral Green Suede Leather
        Pink
        White Leopard
        Modern Ivory Croc Embossed
        Natural Floral Print
        Saddle Leather
        Cantalope Modena Calf Leather"""

    expected_color = [color for color in (x.strip() for x in expected_color.split('\n')) if color]
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for i, color in enumerate(colors):
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        assert current_color == expected_color[i], f'Error "{expected_color[i]}" expected did not match "{current_color}"'
