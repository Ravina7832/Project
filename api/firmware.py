import allure

from api.base_api import BaseAPI

FIRMWARE_URL = 'firmware/repository/'


class FirmwareAPI(BaseAPI):
    def __init__(self, session):
        super().__init__(session)
        self.user_id = None

    @allure.step("Creating Firmware")
    def crete_firmware(self, ):
        files = [
            ('firmware', (
                'VIEW_SKYS_Gn10_MCU_2.0.438.tgz', open('VIEW_SKYS_Gn10_MCU_2.0.438.tgz', 'rb'),
                'application/octet-stream'))
        ]
        return self.make_request(FIRMWARE_URL, method='POST', expected_response_code=201, files=files)
