from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep


AMAZON_ICON = (By.ID, "nav-logo-sprites")


@given('Open Amazon page')
def open_amazon_page(context):
    context.driver.get("https://www.amazon.com/")


@when("Look Amazon Icon")
def look_amazon_icon(context):
    context.amazon_icon_element = context.driver.find_element(*AMAZON_ICON)


@then('Verify aria-label is "{expected_label}"')
def verify_aria_label(context, expected_label):
    actual_label = context.amazon_icon_element.get_attribute("aria-label")
    assert expected_label == actual_label, f'Expected "{expected_label}" label, but got "{actual_label}"'


@when('Input {search_word} into Amazon search')
def search_product(context, search_word):
    search_textbox = context.driver.find_element(By.ID, "twotabsearchtextbox")
    search_textbox.clear()
    search_textbox.send_keys(search_word)
    sleep(0.5)


@when('Click on Amazon search icon')
def click_search_button(context):
    context.driver.find_element(By.ID, "nav-search-submit-button").click()
    sleep(1)

