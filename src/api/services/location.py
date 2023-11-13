from models.location import LocationModel
from schemas.location import Location, LocationId, UserLocation
from repositories.location import LocationRepository


class LocationService:
    def __init__(self, location_repo: LocationRepository):
        self.location_repo: LocationRepository = location_repo()

    async def get_locations(self) -> list[LocationModel]:
        locations = await self.location_repo.find_all()
        return locations

    async def get_favorite_user_locations(
        self, user_id
    ) -> list[LocationModel]:
        locations = await self.location_repo.find_all_favorite_locations(
            user_id
            )
        return locations

    async def post_location(
        self, location: Location
    ) -> LocationModel:
        location = location.model_dump()
        location = await self.location_repo.insert_one(location)
        return location

    async def post_location_to_user_favorite(
        self, location: UserLocation
    ) -> LocationModel:
        location = await self.location_repo.insert_one_to_favorite(
            **dict(location)
            )
        return location

    async def delete_location_from_favorite(
        self, location: UserLocation
    ) -> dict:
        return await self.location_repo.delete_one_from_favorite(
            **dict(location)
            )

    async def delete_location(self, location: LocationId) -> dict:
        return await self.location_repo.delete_one(**dict(location))

    async def put_location(self, location: Location) -> LocationModel:
        location = await self.location_repo.update_one(dict(location))
