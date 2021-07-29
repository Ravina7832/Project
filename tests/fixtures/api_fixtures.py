import pytest
import requests

from api import FloorApi, FirmwareAPI
from api.auth_api import AuthApi
from api.buildings_api import BuildingApi
from api.device_api import DeviceAPI
from api.user_api import UserAPI


@pytest.fixture()
def session():
    return requests.session()


@pytest.fixture()
def auth_api(session):
    return AuthApi(session)


@pytest.fixture()
def device_api(session):
    return DeviceAPI(session)


@pytest.fixture()
def user_api(session):
    return UserAPI(session)


@pytest.fixture()
def building_api(session):
    return BuildingApi(session)


@pytest.fixture()
def floor_api(session):
    return FloorApi(session)


@pytest.fixture()
def firmware_api(session):
    return FirmwareAPI(session)
