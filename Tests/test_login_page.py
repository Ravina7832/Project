import allure

from Configuration.Context import TestData
from Pages.LoginPage import LoginPage
from Tests.Test_conf import BaseTest


@allure.title("TEST SUITE 1")
@allure.feature('Login Page')
class Test_login(BaseTest):
    @allure.title('Login with valid credentials ')
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login()
        self.loginPage.username(TestData.USERNAME)
        self.loginPage.submit()
        self.loginPage.password(TestData.PASSWORD)
        self.loginPage.login()
