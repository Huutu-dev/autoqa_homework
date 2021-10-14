from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC


CARD_METRIC_LIST = (By.CSS_SELECTOR, "#zg_header a")
HEADER_TEXT = (By.ID, "zg_banner_text")


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


@then('Verify the number the {s_idx} item is "{expected_title}"')
def verify_the_th_item(context, s_idx, expected_title):
    n_idx = int(s_idx)
    sz = len(context.card_metric_list)
    assert 0 < n_idx <= sz, f'{n_idx} index given is out of range [1, {sz}]'
    actual_title = context.card_metric_list[n_idx-1].text
    assert expected_title == actual_title, f'Expected "{actual_title}" text content, but got "{actual_title}"'


@then('Verify that new page open when looping')
def verify_header_pages(context):
    expected_titles = [x.text for x in context.driver.find_elements(*CARD_METRIC_LIST)]

    for i, expected_title in enumerate(expected_titles):
        ax_path = f'//div[@id="zg_header"]//ul/li[{i+1}]/div'
        w_element = context.driver.find_element_by_xpath(ax_path)

        # w_parent = w_element.find_element_by_xpath('./..')
        # if 'zg-tabs-li-selected' not in w_parent.get_attribute('class'):
        #    w_element.click()

        w_element.click()
        actual_text = context.driver.find_element(*HEADER_TEXT).text
        # print(expected_title)
        # print('\t', actual_text)
        assert expected_title in actual_text, f'"{actual_text}" did not contains "{actual_text}"'

