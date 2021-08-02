import allure

from tests.fixtures.api_fixtures import *

firmware_api


@allure.title("Validate User Login")
def test_auth(auth_api):
    auth_api.authenticate()

@allure.title("Testing SKYS Firmware")
def test_SKYS_firmware(firmware_api: FirmwareAPI):
    firmware_api.crete_firmware('VIEW_SKYS_Gn10_MCU_2.0.438.tgz')

@allure.title("Testing NWC Firmware")
def test_NWC_firmware(firmware_api: FirmwareAPI):
    firmware_api.crete_firmware('VIEW_NtWC_Pr10_MCU_2.4.23.tgz')


def test_create_duplicate_firmware(firmware_api: FirmwareAPI):
    pass


def delete_firmware(firmware_api: FirmwareAPI):
    pass
