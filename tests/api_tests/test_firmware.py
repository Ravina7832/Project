import os

from tests.fixtures.api_fixtures import *
import allure

firmware_api


@allure.title("Validate User Login")
def test_auth(auth_api):
    auth_api.authenticate()

@pytest.mark.parametrize("firmware_file", ['VIEW_SKYS_Gn10_MCU_2.0.438.tgz', 'VIEW_NtWC_Pr10_MCU_2.4.23.tgz'])
def test_create_firmware(firmware_api: FirmwareAPI, firmware_file):
    firmware_api.crete_firmware(firmware_file)


def test_create_duplicate_firmware(firmware_api: FirmwareAPI):
    pass


def delete_firmware(firmware_api: FirmwareAPI):
    pass
