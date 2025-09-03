from selenium.webdriver.common.by import By

from control_up.pages.controlup_base_page import ControlUpBasePage
from core import core_driver

# region Locators

_CONTAINER_INVENTORY_ITEM = (By.CSS_SELECTOR, '.inventory_list .inventory_item')
_SPAN_CART_BAGDE = (By.CSS_SELECTOR, '.shopping_cart_badge')


# endregion

class ControlUpInventoryPage(ControlUpBasePage):

    def __init__(self, driver: core_driver):
        super().__init__(driver)

    @property
    def url_suffix(self):
        return "inventory.html"

    def get_inventory_items(self):
        return self._driver.find_elements(*_CONTAINER_INVENTORY_ITEM)

    def get_cart_items_count(self):
        return self._driver.find_element(*_SPAN_CART_BAGDE).text