from api.base_api import BaseAPI

BUILDING_URL = 'buildings'


class BuildingApi(BaseAPI):
    def __init__(self, session):
        super().__init__(session)

    def __get_buildings(self, building_id=''):
        return self.make_request(BUILDING_URL + building_id)

    def get_building(self, building_id):
        return self.__get_buildings(building_id)

    def get_buildings(self, ):
        return self.__get_buildings()
