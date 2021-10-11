from Project.Configuration.Context import TestData
from Project.Pages.HomePage import HomePage
from Project.Pages.LoginPage import LoginPage
from Project.Tests.test_conf import BaseTest


class Test_Home(BaseTest):
    def test_users(self,):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login()
        self.loginPage.username(TestData.USERNAME)
        self.loginPage.submit()
        self.loginPage.password(TestData.PASSWORD)
        self.loginPage.login()
        self.select_user = HomePage(self.driver)
        self.select_user.sel_users()
        self.select_user.dropdown()
        self.select_user.select()


