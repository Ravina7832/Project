import logging
import os

import requests

URL_DICT = {
    'QA': 'https://api-qa.viewcorp.xyz/api/v1/',
    'Demo': 'https://api-demo.viewcorp.xyz/api/v1/',
    'Staging': 'https://cloud-stage.view.com/api/v1/'
}
BASEURL = URL_DICT[os.getenv('Environment', "QA")]

logger = logging.getLogger()


class BaseAPI:
    api_headers = None

    def __init__(self, session=None):
        self.session = session if session else requests.session()
        self.is_logged_in = False

    def make_request(self, endpoint, method='GET', params=None, data=None, expected_response_code=200, files=None):
        res = self.session.request(method=method, url=BASEURL + endpoint, data=data, params=params,
                                   headers=self.api_headers, files=files)
        try:
            assert res.status_code == expected_response_code, f"Expected  {expected_response_code} got {res.status_code} error : {res.text}"
        except AssertionError as e:
            logger.error(res.text)
            logger.exception(e)
            raise Exception(e)
        return res.json()
