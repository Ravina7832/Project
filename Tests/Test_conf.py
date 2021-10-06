import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Configuration.Context import TestData


@pytest.mark.usefixtures("set_up")
class BaseTest:
    @pytest.fixture(params=["chrome"], scope="class")
    def set_up(self, request):
        if request.param == "chrome":
            # options = webdriver.ChromeOptions()
            # options.headless = True
            web_driver = webdriver.Chrome()
            web_driver.maximize_window()
        request.cls.driver = web_driver
        yield
        web_driver.close()
