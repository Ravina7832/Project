import allure

from tests.fixtures.api_fixtures import *
from faker import Faker

auth_api
fake = Faker()

user_id = None

def pytest_namespace():
    return {'user_id': None}

@allure.title("Validate User Creation")
def test_auth(auth_api):
    auth_api.authenticate()


@allure.title("Validate User Creation")
def test_create_user(user_api):
    user_data = {'firstName': fake.first_name(), 'lastName': fake.last_name(), 'email': fake.email(),
                 'password': 'password', 'roles': 'customer', 'companyId': 'companyId', 'authenticator': 'view'}
    user_creation_res = user_api.create_user(user_data=user_data)
    pytest.user_id = user_creation_res['data']['uniqueId']
    user = user_api.get_user(pytest.user_id)


@allure.title("Validate User Deletion")
def test_delete_user(user_api):
    user_creation_res = user_api.delete_user(pytest.user_id)
