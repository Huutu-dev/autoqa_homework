from behave import given, when, then


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.app.product_page.open_product(product_id).refresh()


@when('Click on the first product')
def click_first_product(context):
    context.app.product_page.click_first_product()


@when('Store product name')
def store_product_name(context):
    context.app.product_page.store_product_name()


@when('Click on Add to cart button')
def click_add_to_cart(context):
    context.app.product_page.add_to_cart()


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

    expected_colors = [color for color in (x.strip() for x in expected_color.split('\n')) if color]
    context.app.product_page.verify_through_colors(expected_colors)


@when("Select department by alias {alias}")
def select_department_by_alias(context, alias):
    context.app.header.select_department_by_alias(alias)


@then("Verify {dept} department is selected")
def verify_books_department_is_selected(context, dept):
    context.app.product_page.verify_correct_department_selected(dept)


@when("Hover over {a_content}")
def hover_over_fly_fashion(context, a_content):
    context.app.fashion_header.hover_over_fly_fashion(a_content)


@then('Verify user sees the deals')
def verify_fly_fashion_present(context):
    context.app.fashion_header.verify_fly_fashion_present()