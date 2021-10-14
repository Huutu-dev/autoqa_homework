from web_driver import chrome_driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# init driver
driver = chrome_driver()
driver.maximize_window()
driver.wait = WebDriverWait(driver, 10)
# driver.implicitly_wait(10)

# open the url
driver.get('https://www.google.com/')

search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

e = driver.wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')), message="Error, Couldn't each Search button'")
e.click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
