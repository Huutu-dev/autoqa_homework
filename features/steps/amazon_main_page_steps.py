from behave import given, when, then


@given('Open Amazon page')
def open_amazon_page(context):
    # context.driver.get("https://www.amazon.com/")
    context.app.main_page.open_me()


@when("Look Amazon Icon")
def look_amazon_icon(context):
    # context.amazon_icon_element = context.driver.find_element(*AMAZON_ICON)
    return context.app.header.amazon_icon_element


@then('Verify aria-label is "{expected_label}"')
def verify_aria_label(context, expected_label):
    actual_label = context.app.header.amazon_icon_element.get_attribute("aria-label")
    assert expected_label == actual_label, f'Expected "{expected_label}" label, but got "{actual_label}"'


@when('Input {search_word} into Amazon search')
def search_product(context, search_word):
    # search_textbox = context.driver.find_element(By.ID, "twotabsearchtextbox")
    # search_textbox.clear()
    # search_textbox.send_keys(search_word)
    context.app.header.input_search(search_word)


@when('Click on Amazon search icon')
def click_search_button(context):
    # context.driver.find_element(By.ID, "nav-search-submit-button").click()
    context.app.header.click_search()


@when('Click Amazon Orders link')
def click_order_link(context):
    context.app.header.go_return_n_order()


@when("Click on cart icon")
def click_cart_icon(context):
    context.app.header.checkin_cart(context.app.cart_page)
