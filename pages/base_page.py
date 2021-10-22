from abc import ABCMeta, abstractmethod
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(metaclass=ABCMeta):

    @classmethod
    @abstractmethod
    def get_sub_url(cls):
        return NotImplemented

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._base_url = 'https://www.amazon.com/'

    @property
    def driver(self):
        return self._driver

    def open_page(self, page_address=''):
        self.driver.get(f'{self._base_url}{page_address}')

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def _wait_click_to_open(self, locator, partial_url, sec_try, nb_try):
        i = 0
        while i < nb_try:
            e = WebDriverWait(self.driver, sec_try).until(EC.element_to_be_clickable(locator))
            e.click()
            if partial_url in self.driver.current_url:
                break
        else:
            assert False, f'Error! could not open new page by clicked trigger'
        print(f"Try with {i} times")

    def click_wait_page_opened(self, locator, sec_try=4, nb_try=3):
        self._wait_click_to_open(locator, self.get_sub_url(), sec_try, nb_try)

    def wait_page_opened(self, message='') -> WebElement:
        return self.wait_for_opening(self.get_sub_url(), message=message)

    def wait_for_element_click(self, locator, message=''):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator), message=message)
        e.click()

    def wait_for_element_disappear(self, locator) -> WebElement:
        return self.driver.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, locator) -> WebElement:
        return self.driver.wait.until(EC.presence_of_element_located(locator))

    def wait_for_opening(self, partial_url, message='') -> WebElement:
        return self.driver.wait.until(EC.url_contains(partial_url), message=message)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, \
            f'Error! Actual text "{actual_text}" does not match expected "{expected_text}"'

    def verify_url_contains_query(self, query):
        assert query in self.driver.current_url, f'{query} not in {self.driver.current_url}'
