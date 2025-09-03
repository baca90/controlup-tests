from selenium.webdriver.common.by import By

from control_up.pages.controlup_base_page import ControlUpBasePage
from core import core_driver

# region Locators

INPUT_LOGIN = (By.ID, 'user-name')
INPUT_PASSWORD = (By.ID, 'password')
BUTTON_SUBMIT = (By.ID, 'login-button')


# endregion

class ControlUpLoginPage(ControlUpBasePage):

    def __init__(self, driver: core_driver):
        super().__init__(driver)

    @property
    def url_suffix(self):
        return

    def set_login(self, login):
        self._driver.find_element(*INPUT_LOGIN).send_keys(login)

    def set_password(self, password):
        self._driver.find_element(*INPUT_PASSWORD).send_keys(password)

    def click_submit_button(self):
        self._driver.find_element(*BUTTON_SUBMIT).click()
