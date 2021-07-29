import allure

from api.base_api import BaseAPI

DEVICE_URL = 'devices/'


class DeviceAPI(BaseAPI):
    def __init__(self, session):
        super().__init__(session)

    @allure.step("Getting Device")
    def get_devices(self, device_type, params=""):
        if params and isinstance(params, dict):
            params.update({'limit': 2000})
        return self.make_request(DEVICE_URL + device_type, params=params, method='GET').get('data')
