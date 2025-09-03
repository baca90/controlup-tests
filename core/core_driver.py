from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def initialize(core_config):
    match core_config.BROWSER:
        case 'chrome':
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--lang=pl")
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-search-engine-choice-screen')
            if core_config.HEADLESS:
                chrome_options.add_argument("--headless")

            return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

        case 'firefox':
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--lang=pl")
            log_path = core_config.OUTPUT_DIR
            if core_config.HEADLESS:
                firefox_options.add_argument("--headless")

            return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install(), log_path=log_path),
                                     options=firefox_options)
