"""HOW TO SWITCH BETWEEN WINDOWS
"""
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


@when("Store original windows")
def store_current_window(context):
    context.original_window = context.driver.current_window_handle


@when("Switch to the newly opened window")
def switch_newly_window(context):
    new_window = context.driver.window_handles[1]
    context.driver.switch_to_window(new_window)


@then("Close the current window")
def close_window(context):
    context.driver.close()


@then("Switch back to original")
def switch_back(context):
    context.driver.switch_to_window(context.original_window)


def all_steps(context, link):
    """Just to demonstration"""
    # Store all windows in a variable
    driver = context.driver
    original_window = driver.current_window_handle
    # old_windows = driver.window_handles

    # Click on element that is supposed to open a new windows
    link.click()

    # Wait for new window to open
    context.wait.until(EC.new_window_is_opened)

    # Switch to new window
    new_window = driver.window_handles[1]
    driver.switch_to_window(new_window)

    # Close new window
    context.driver.close()

    # Go back
    context.driver.switch_to_window(original_window)

