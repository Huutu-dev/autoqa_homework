import behave.runner
from selenium.webdriver.common.by import By
from behave import given, when, then


@then("Verify Sign In page is opened")
def verify_sign_in_opened(context):
    # context.driver.wait.until(EC.url_contains('https://www.amazon.com/ap/signin'),
    #                           message='Sign In page did not open')
    context.app.sign_in_page.wait_page_opened(message='Sign In page did not open')

