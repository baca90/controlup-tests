import logging

from core import core_test_config


LOGGER = logging.getLogger(__name__)

TEST_INFO_LEVEL = 25
logging.addLevelName(TEST_INFO_LEVEL, "TEST_INFO")

"""
TEST INFO is a logging level between WARNING(30) and INFO(20), to avoid displaying unnecessary information at
INFO level, for example WebDriver Manager logs.
"""


def test_info(self, message, *args, **kws):
    if self.isEnabledFor(TEST_INFO_LEVEL):
        self._log(TEST_INFO_LEVEL, message, args, **kws)


logging.Logger.test_info = test_info
