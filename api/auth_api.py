import logging
import os

from api.base_api import BaseAPI

logger = logging.getLogger()
AUTH_URL = 'auth/login'

user_creds = {
    'QA': {
        "email": "qa@view.com",
        "password": "viewnet195",
        "role": "customer"},
    'Staging': {
        "email": "hq@view.com",
        "password": "viewnet195",
        "role": "customer"
    }
}


class AuthApi(BaseAPI):
    def __init__(self, session):
        super().__init__(session)

    def authenticate(self):
        data = user_creds[os.getenv('Environment', 'QA')]
        response = self.make_request(AUTH_URL, method='POST', data=data)
        assert response.get('data', {}).get('access_token')
        # self.session.headers.update({'Authorization': 'Bearer ' + response.get('data', {}).get('access_token')})
        BaseAPI.api_headers = {'Authorization': 'Bearer ' + response.get('data', {}).get('access_token')}
        return response
