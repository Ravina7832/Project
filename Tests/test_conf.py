import pytest
from selenium import webdriver

from Configuration.constants import CHROME_PATH


@pytest.mark.usefixtures("set_up")
class BaseTest:
    @pytest.fixture(params=["chrome"], scope="class")
    def set_up(self, request):
        # options = webdriver.ChromeOptions()
        # options.headless = True
        web_driver = webdriver.Chrome(CHROME_PATH)
        web_driver.maximize_window()
        request.cls.driver = web_driver
    # yield
    # web_driver.close()
