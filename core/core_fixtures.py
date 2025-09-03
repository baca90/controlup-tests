import logging

import pytest

import core.core_driver as cd
from core import core_test_config
from core.core_logger import LOGGER


# region Fixtures

@pytest.fixture(scope="session", autouse=True)
def core_config():
    return core_test_config


@pytest.fixture(scope="function")
def core_driver(core_config, _set_webdriver_manager_params):
    driver = cd.initialize(core_config)
    LOGGER.test_info(f"{core_config.BROWSER} driver started")

    yield driver

    driver.quit()


@pytest.fixture(scope="session")
def _set_webdriver_manager_params(core_config):
    if not core_config.WDM_LOG:
        logging.getLogger('WDM').setLevel(logging.NOTSET)


# endregion


# region Hooks


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logstart(nodeid):
    LOGGER.test_info(f"Test '{nodeid}' STARTED")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logfinish(nodeid):
    LOGGER.test_info(f"Test '{nodeid}' COMPLETED")


# endregion
