import pytest
from selenium import webdriver

from Configuration.Context import TestData


@pytest.mark.usefixtures("set_up")
class BaseTest:
    @pytest.fixture(params=["chrome"], scope="class")
    def set_up(self, request):
        if request.param == "chrome":
            web_driver = webdriver.Chrome()
            web_driver.maximize_window()
        request.cls.driver = web_driver
        # yield
        # web_driver.close()
        # executable_path=TestData.CHROME_EXECUTABLE_PATH
