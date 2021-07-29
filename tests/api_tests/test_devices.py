import allure

from tests.fixtures.api_fixtures import *
from utils.constants import device_type

auth_api
building_id = '910005'
floor_id = 'AQvUzGnlVLScz2FXUxT4hA'

device_schema = {

}


@allure.title("Validate User Login")
def test_auth(auth_api):
    auth_api.authenticate()


@allure.title("Test Building API")
def test_buildings(building_api: BuildingApi):
    buildings = building_api.get_buildings()
    # raise Exception(buildings.get('data'))
    assert buildings.get('data')
    # for building in buildings:

@allure.title("Test Floors API")
def test_floors(floor_api: FloorApi):
    floors = floor_api.get_floors(building_id)


def raise_for_disconnected(disconnected_devices):
    if disconnected_devices: raise AssertionError(
        f"{','.join(disconnected_devices)} {'is' if len(disconnected_devices) == 1 else 'are'} offline")


@pytest.mark.parametrize("device_type_", [device_type.MANTIS, device_type.IGU, device_type.CONTROLLERS, device_type.NW,
                                          device_type.SKY_SENSOR, device_type.CPHE, device_type.FANC, device_type.PDU,
                                          device_type.CP])
def test_devices(device_api, device_type_):
    allure.dynamic.title(f"""Validating {device_type_.replace('_', ' ').capitalize()}""")
    devices_response = device_api.get_devices(device_type_, params={'buildingId': 910005})
    devices = devices_response.get('data') if isinstance(devices_response, dict) else devices_response
    disconnected_devices = []
    for device in devices:
        if device.get('status') != 'connected':
            disconnected_devices.append(device.get('logicalId'))
    raise_for_disconnected(disconnected_devices)
