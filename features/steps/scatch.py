from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep


pass


""""
@given('Open Amazon Help page')
def open_amazon_help(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@when('Use "Search Help Library" field and search for {search_word}')
def search_help_library(context, search_word):
    search_textbox = context.driver.find_element(By.ID, "helpsearch")
    search_textbox.clear()
    search_textbox.send_keys(search_word)
    sleep(1)


@when('Hitting enter to send keys')
def enter_helpsearch(context):
    context.driver.find_element(By.ID, "helpsearch").send_keys(Keys.ENTER)
    sleep(1)


@then('Verify that {expect_result} text is present')
def validate_help_content(context, expect_result):
    actual_result = context.driver.find_element(By.XPATH, '//div[@class="help-content"]//h1').text
    assert actual_result == expect_result, f'Error! Actual "{actual_result}" does not match expected "{expect_result}"'


@when('Click on the cart')
def force_cart_item(context):
    context.driver.find_element_by_css_selector("#nav-cart-count").click()
    sleep(1)


@then('Look the empty cart')
def find_empty_place_cart(context):
    context.cart_place = context.driver.find_element_by_css_selector(".sc-your-amazon-cart-is-empty")


@then('Double check "{expect_result}" on text')
def text_contain(context, expect_result):
    actual_result = context.cart_place.text
    assert actual_result == expect_result, f'Error! Actual "{actual_result}" does not match expected "{expect_result}"'
"""