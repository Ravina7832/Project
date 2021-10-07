import allure
from faker import Faker

from Configuration.Context import TestData
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Tests.test_conf import BaseTest
from Pages.AddUsersPage import AddUsers


@allure.title("TEST SUITE 2")
@allure.feature("Users Module")
class Test_AddUsers(BaseTest):
    @allure.title("Add Users")
    @allure.severity(allure.severity_level.NORMAL)
    def test_addUsers(self):
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
        self.users = AddUsers(self.driver)
        self.users.users()
        self.users.add_users()
        self.users.firstname(TestData.FIRSTNAME)
        self.users.lastname(TestData.LASTNAME)
        self.users.email(TestData.EMAIL)
        self.users.phone(TestData.PHONE)
        self.users.password(TestData.PASSWORD1)
        self.users.conf_password(TestData.CONFIRMPASSWORD)
        self.users.select_person()
        self.users.next()
        self.users.time()
        self.users.sel_date(TestData.DATE)
        self.users.zone()
        self.users.search_users()
        self.users.manager(TestData.SEARCH_NAME)
        self.users.csm_s(TestData.SEARCH_EMAIL)
        self.users.occupants(TestData.PHONE)
        self.users.edit_user()
        self.users.edit_fname(TestData.EDIT_FNAME)
        self.users.edit_lname(TestData.EDIT_LNAME)
        self.users.edit_email(TestData.EDIT_EMAIL)
        self.users.edit_phone(TestData.EDIT_PHONE)
        self.users.edit_save()
