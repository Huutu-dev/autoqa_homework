from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep

CARD_METRIC_LIST = (By.CSS_SELECTOR, "#CardInstanceXeGRD8VlbLZwHSx6bccQmQ a")


@given('Open BestSellers page')
def open_bestsellers_page(context):
    context.driver.get("https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers")


@when("Store card metric list")
def get_metric_list(context):
    context.card_metric_list = context.driver.find_elements(*CARD_METRIC_LIST)
    print(context.card_metric_list)


@then("Verify there is {s_number} links in the list")
def count_metric_list(context, s_number):
    number = int(s_number)
    actual_len = len(context.card_metric_list)
    assert number == actual_len, f'Expected {number} links, but got {actual_len} stuffs'


@then('Verify the number the {i_row} item is "{expected_title}"')
def step_impl(context, i_row, expected_title):
    sz = len(context.card_metric_list)
    assert 0 < i_row <= sz, f'{i_row} index given is out of range [1, {sz}]'
    actual_title = context.card_metric_list[i_row-1].text
    assert expected_title == actual_title, f'Expected "{actual_title}" text content, but got "{actual_title}"'