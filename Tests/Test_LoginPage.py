from Configuration.Context import TestData
from Pages.LoginPage import LoginPage
from Tests.Test_conf import BaseTest


class Test_login(BaseTest):
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)