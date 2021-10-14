from behave import given, when, then


@when('Open cart page')
def open_cart_page(context):
    # context.driver.get('https://www.amazon.com/gp/cart/view.html?ref_=nav_cart')
    context.app.cart_page.open_me()


@then("Verify Cart page is opened")
def verify_card_page_opened(context):
    context.app.cart_page.wait_page_opened()


@then('Verify cart has {expected_count} item(s)')
def verify_cart_count(context, expected_count):
    # actual_count = context.driver.find_element(*CART_COUNT).text
    # assert actual_count == expected_count, f'Expected {expected_count} item(s), but got {actual_count} item(s)'
    context.app.cart_page.count_products(expected_count)


@then('Verify cart has correct product')
def verify_product_name(context):
    # cart_product_name = context.driver.find_element(*PRODUCT_NAME).text
    # print(f'Product name in cart: {cart_product_name}')
    # assert cart_product_name == context.current_product_name, \
    #     f'Expected "{context.current_product_name}" product, but got "{cart_product_name}"'
    context.app.cart_page.verify_product_name(context.app.product_page.current_product_name)


@then("Verify '{text_present}' text present")
def verify_empty_cart(context, text_present):
    context.app.cart_page.cart_is_empty(text_present)
