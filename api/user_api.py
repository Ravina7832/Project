import allure

from api.base_api import BaseAPI

USER_URL = 'users/'


class UserAPI(BaseAPI):
    def __init__(self, session):
        super().__init__(session)
        self.user_id = None

    @allure.step("Creating user")
    def create_user(self, user_data):
        return self.make_request(USER_URL, data=user_data, method='POST', expected_response_code=201)

    @allure.step("Deleting user")
    def delete_user(self, user_id):
        return self.make_request(USER_URL + '/' + user_id, method='DELETE')

    @allure.step("Getting user")
    def get_user(self, user_id):
        return self.make_request(USER_URL + '/' + user_id, method='GET', expected_response_code=204)
