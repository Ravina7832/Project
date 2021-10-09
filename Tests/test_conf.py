import pytest
from selenium import webdriver
from Configuration.constants import CHROME_PATH
import os, sys, stat

CHROME_PATH = "/Users/pc/PycharmProjects/Project/chromedriver"


@pytest.mark.usefixtures("set_up")
class BaseTest:
    @pytest.fixture(params=["chrome"], scope="class")
    def set_up(self, request):
        # options = webdriver.ChromeOptions()
        # options.headless = True
        # web_driver = webdriver.Chrome(CHROME_PATH)
        # web_driver.maximize_window()
        # request.cls.driver = web_driver

        os.environ["webdriver.chrome.driver"] = CHROME_PATH

        prefs = {"profile.default_content_setting_values.notifications": 2,
                 "download.prompt_for_download": False,
                 "download.directory_upgrade": True
                 }
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        chrome_options.add_argument('headless')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument("start-maximized")
        chrome_options.add_argument("disable-infobars")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("window-size=1920x1080")
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(executable_path=CHROME_PATH, options=chrome_options)

        driver.maximize_window()
        driver.implicitly_wait(10)
        request.cls.driver = driver

        yield
        driver.close()
