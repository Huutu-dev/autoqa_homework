from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

PRIVACY_HREF = (By.CSS_SELECTOR, 'a[href="https://www.amazon.com/privacy"]')


@given('Open Amazon Terms of Conditions page')
def open_tnc(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/'
                       'ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Click on Amazon Privacy Notice link')
def click_private_notice(context):
    context.driver.find_element(*PRIVACY_HREF).click()
    context.driver.wait.until(EC.new_window_is_opened)


@then("Verify Amazon Privacy Notice page is opened")
def verify_private_notice_opened(context):
    assert 'nodeId=GX7NJQ4ZB8MHFRNJ' in context.driver.current_url, f'Error, "Amazon.com Privacy Notice" not opened'
