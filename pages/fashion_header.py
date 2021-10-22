from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from .base_page import Page


class FashionHeader(Page):
    ANCHOR_FLY = (By.XPATH, '//div[@id="nav-subnav"]/a[./span[contains(text(),"{CONTENT}")]]')
    FASHION_DEAL = (By.XPATH, '//header//a/ul[@class="mm-category-list" and ./li[contains(text(), "See More")]]')
    FASHION_WOMEN_DEAL = (By.XPATH, './li/h3[contains(text(), "Women")]')  # child of FASHION_DEAL ul element

    @classmethod
    def get_sub_url(cls):
        return NotImplemented

    def _get_anchor_content(self, a_content):
        return self.ANCHOR_FLY[0], self.ANCHOR_FLY[1].format(CONTENT=a_content)

    def hover_over_fly_fashion(self, a_content):
        a_fly = self.find_element(*self._get_anchor_content(a_content))
        actions = ActionChains(self.driver)
        actions.move_to_element(a_fly)
        actions.perform()

    def verify_fly_fashion_present(self):
        e = self.wait_for_element_appear(self.FASHION_DEAL)
        e.find_element(*self.FASHION_WOMEN_DEAL)
