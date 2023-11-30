from api.models.user_location import UserLocationModel
from models.location import LocationModel
from schemas.location import Location, LocationAdd, LocationId, UserLocation
from repositories.location import LocationRepository


class LocationService:
    def __init__(self, location_repo: LocationRepository):
        self.location_repo: LocationRepository = location_repo()

    async def get_locations(self) -> list[LocationModel]:
        res = await self.location_repo.find_all()
        return res

    async def get_favorite_user_locations(
        self, user_id
    ) -> list[LocationModel]:
        res = await self.location_repo.find_all_favorite_locations(
            user_id
            )
        return res

    async def post_location(
        self, location: LocationAdd
    ) -> LocationModel:
        res = await self.location_repo.insert_one(location.model_dump())
        return res

    async def post_location_to_user_favorite(
        self, location: UserLocation
    ) -> UserLocationModel:
        res = await self.location_repo.insert_one_to_favorite(**location.model_dump())
        return res

    async def delete_location_from_favorite(
        self, location: UserLocation
    ) -> UserLocationModel:
        res = await self.location_repo.delete_one_from_favorite(**location.model_dump())
        return res

    async def delete_location(self, location: LocationId) -> LocationModel:
        res = await self.location_repo.delete_one(**location.model_dump())
        return res

    async def put_location(self, location: Location) -> LocationModel:
        res = await self.location_repo.update_one(location.model_dump())
        return res
