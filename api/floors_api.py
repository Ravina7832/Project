from api.base_api import BaseAPI

PATH = 'floors/'


class FloorApi(BaseAPI):
    def __init__(self, session):
        super().__init__(session)

    def get_floors(self, building_id):
        params = {'buildingId': building_id}
        return self.make_request(PATH, method='GET', params=params)

    # def get_floor_id(self):
