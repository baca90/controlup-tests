from abc import ABC

from selenium.webdriver.common.by import By

from core import core_driver
from core.base_page import BasePage


class ControlUpBasePage(BasePage, ABC):

    def __init__(self, driver: core_driver):
        super().__init__(driver)

    def click_element_by_data_testid(self, data_testid):
        self._driver.find_element(By.XPATH, f"//a[@data-testid='{data_testid}']").click()
