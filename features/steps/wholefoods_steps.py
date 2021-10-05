from selenium.webdriver.common.by import By
from behave import given, when, then

PRODUCTS = (By.XPATH,
            "//li[@class='s-result-item' and .//span[contains(@class, 'prime-price')]]//div[@class='s-item-container']")
PRODUCT_NAME = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__product-name')
REGULAR_CASE = (By.CSS_SELECTOR, 'span.wfm-sales-item-card__regular-price')


@given('Open Amazon Wholefoods page')
def open_wholefoods_product(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals/')
    context.driver.refresh()


@then('Verify that every product has a text "Regular" and a product name')
def verify_regular_name_product(context):
    item_cards = context.driver.find_elements(*PRODUCTS)
    for card in item_cards:
        assert 'Regular' in card.text, f"Expected 'Regular' in '{card.tex}', But didn't find"
        prod = card.find_element(*PRODUCT_NAME).text
        assert prod, 'Expected product name is not empty'

        price = card.find_element(*REGULAR_CASE).text
        print(prod, '\n\t', price)

