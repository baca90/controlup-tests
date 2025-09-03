import urllib
from abc import ABC, abstractmethod
from urllib import parse

from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from core import core_test_config, core_driver
from core.core_logger import LOGGER


# region web elements


def button_xpath_by_text(text):
    return By.XPATH, f'//button[contains(text(),"{text}")]'


def button_xpath_by_span_text(text):
    return By.XPATH, f'//button//span[contains(text(),"{text}")]'


def span_by_text(text):
    return By.XPATH, f'//span[text()="{text}"]'


# endregion


def _is_page_ready(driver):
    state = driver.execute_script("return document.readyState;")
    return state == "complete"


class BasePage(ABC):

    # region class definition

    def __init__(self, driver: core_driver):
        self._driver = driver
        self._driver.implicitly_wait(core_test_config.TIMEOUT)
        self._driver.set_page_load_timeout(core_test_config.PAGE_LOAD_TIMEOUT)
        self._wait = WebDriverWait(driver, core_test_config.PAGE_LOAD_TIMEOUT)
        self._actions = ActionChains(self._driver)

    @property
    @abstractmethod
    def url_suffix(self):
        pass

    # endregion

    # region page methods

    # region waits

    def wait_for_page_to_load(self):
        LOGGER.test_info("Waiting for page to load...")
        self._wait.until(_is_page_ready)

    def wait_for_url_contains(self, expected_url):
        LOGGER.test_info(f"Waiting for url to constains {expected_url}...")
        self._wait.until(ec.url_contains(expected_url))

    # endregion

    # region clicks

    def click_button_by_text(self, text):
        self._driver.find_element(*button_xpath_by_text(text)).click()
        LOGGER.test_info(f"Clicked button with text {text}.")
        self.wait_for_page_to_load()

    # endregion
