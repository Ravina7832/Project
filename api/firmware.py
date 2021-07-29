import allure

from api.base_api import BaseAPI

FIRMWARE_URL = 'firmware/repository/'


class FirmwareAPI(BaseAPI):
    def __init__(self, session):
        super().__init__(session)
        self.user_id = None

    @allure.step("Creating Firmware")
    def crete_firmware(self, file_name):
        files = [
            ('firmware', (
                file_name, open(file_name, 'rb'),
                'application/octet-stream'))
        ]
        return self.make_request(FIRMWARE_URL, method='POST', expected_response_code=201, files=files)
