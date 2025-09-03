import pytest

from control_up.pages.controlup_inventory_page import ControlUpInventoryPage
from control_up.pages.controlup_login_page import ControlUpLoginPage
from core.core_logger import LOGGER


@pytest.fixture(scope="function")
def log_to_application(core_config, core_driver):
    user = core_config.USER
    password = core_config.PASSWORD

    _login_page = ControlUpLoginPage(core_driver)
    LOGGER.test_info(f"Navigating to {core_config.ENV_URL}")
    core_driver.get(core_config.ENV_URL)
    LOGGER.test_info(f"Logging as {user}...")
    _login_page.set_login(user)
    _login_page.set_password(password)
    _login_page.click_submit_button()
    _login_page.wait_for_url_contains("inventory")
    LOGGER.test_info(f"Logged as {user}.")
    return ControlUpInventoryPage(core_driver)
