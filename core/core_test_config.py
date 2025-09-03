import configparser
import os

ROOT_DIR = os.path.abspath(os.curdir)
OUTPUT_DIR = os.path.join(ROOT_DIR, "output")
TEMP_DIR = os.path.join(ROOT_DIR, "temp")

config = configparser.ConfigParser()
config.read(os.path.join(ROOT_DIR, "default_config.ini"))


def get_config_value(section, key):
    if os.environ.get(key) is not None:
        return os.environ.get(key)
    else:
        return config.get(section, key)


def get_config_bool(section, key):
    if os.environ.get(key) is not None:
        return os.environ.get(key).lower() in ('true', '1', 't')
    else:
        return config.getboolean(section, key)


ENV_URL = get_config_value("APP", "ENV_URL")
API_URL = get_config_value("APP", "API_URL")
USER = get_config_value("APP", "APP_USER")
PASSWORD = get_config_value("APP", "APP_PASS")
ACC_TOKEN = get_config_value("APP", "ACC_TOKEN")

BROWSER = get_config_value("BROWSER", "BROWSER_NAME")
BROWSER_WIDTH = get_config_value("BROWSER", "WIDTH")
BROWSER_HEIGHT = get_config_value("BROWSER", "HEIGHT")
HEADLESS = get_config_bool("BROWSER", "HEADLESS")
WDM_LOG = get_config_bool("BROWSER", "WDM_LOG")

TIMEOUT = int(get_config_value("DRIVER", "TIMEOUT"))
PAGE_LOAD_TIMEOUT = int(get_config_value("DRIVER", "PAGE_LOAD_TIMEOUT"))
