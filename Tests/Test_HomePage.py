from Configuration.Context import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.Test_conf import BaseTest


class Test_Home(BaseTest):
    def test_users(self,):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)

        self.click_user = HomePage(self.driver)
        self.click_user.sel_users()


