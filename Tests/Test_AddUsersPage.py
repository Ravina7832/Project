import allure
from faker import Faker

from Configuration.Context import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.Test_conf import BaseTest
from Pages.AddUsersPage import AddUsers


@allure.title("TEST SUITE 2")
@allure.feature("Users Module")
class Test_AddUsers(BaseTest):
    @allure.title("Add Users")
    @allure.severity(allure.severity_level.NORMAL)
    def test_addUsers(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(TestData.USERNAME, TestData.PASSWORD)
        self.click_user = HomePage(self.driver)
        self.click_user.sel_users()
        self.users = AddUsers(self.driver)
        self.users.users()
        self.users.add_users(TestData.FIRSTNAME, TestData.LASTNAME, TestData.EMAIL, TestData.PHONE,
                             TestData.PASSWORD1, TestData.CONFIRMPASSWORD, TestData.DATE)
        self.users.search_users(TestData.SEARCH_NAME, TestData.SEARCH_EMAIL, TestData.PHONE)
        self.users.edit_user(TestData.EDIT_FNAME, TestData.EDIT_LNAME, TestData.EDIT_EMAIL, TestData.EDIT_PHONE)
