from tests.fixtures.api_fixtures import *

firmware_api


def test_create_firmware(firmware_api: FirmwareAPI):
    firmware_api.crete_firmware()


def test_create_duplicate_firmware(firmware_api: FirmwareAPI):
    pass


def delete_firmware(firmware_api: FirmwareAPI):
    pass
