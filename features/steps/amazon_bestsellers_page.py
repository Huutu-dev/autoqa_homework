from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep

CARD_METRIC_LIST = (By.CSS_SELECTOR, "#zg_header a")


@given('Open BestSellers page')
def open_bestsellers_page(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/")
    context.driver.refresh()


@when("Store card metric list")
def get_metric_list(context):
    context.card_metric_list = context.driver.find_elements(*CARD_METRIC_LIST)


@then("Verify there are {s_number} links in the list")
def count_metric_list(context, s_number):
    number = int(s_number)
    actual_len = len(context.card_metric_list)
    assert number == actual_len, f'Expected {number} links, but got {actual_len} stuffs'


@then('Verify the number the {s_row} item is "{expected_title}"')
def verify_the_th_item(context, s_row, expected_title):
    i_row = int(s_row)
    sz = len(context.card_metric_list)
    assert 0 < i_row <= sz, f'{i_row} index given is out of range [1, {sz}]'
    actual_title = context.card_metric_list[i_row-1].text
    assert expected_title == actual_title, f'Expected "{actual_title}" text content, but got "{actual_title}"'