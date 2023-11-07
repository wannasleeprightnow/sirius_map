from fastapi import APIRouter, Body, Depends

from config import API_VERSION
from dependencies import location_service
from services.location import LocationService
from schemas.location import Location, LocationId, UserLocation

router = APIRouter(prefix=API_VERSION + "location", tags=["location"])


@router.get("")
async def get_locations(
    location_service: LocationService = Depends(location_service)
):
    locations = await location_service.get_locations()
    return locations


@router.post("/favorite/")
async def post_location_to_user_favorite(
     location: UserLocation = Body(),
     location_service: LocationService = Depends(location_service),
):
    location = await location_service.post_location_to_user_favorite(location)
    return location


@router.get("/favorite/{user_id}")
async def get_favorite_user_locations(
    user_id: int,
    location_service: LocationService = Depends(location_service),
):
    locations = await location_service.get_favorite_user_locations(user_id)
    return locations


@router.delete("/favorite")
async def delete_location_from_favorite(
    location: UserLocation = Body(),
    location_service: LocationService = Depends(location_service)
):
    return await location_service.delete_location_from_favorite(location)


@router.post("")
async def post_location(
    location: Location = Body(),
    location_service: LocationService = Depends(location_service)
):
    return await location_service.post_location(location)


@router.put("")
async def put_location(
    location: Location = Body(),
    location_service: LocationService = Depends(location_service)
):
    return await location_service.put_location(location)


@router.delete("")
async def delete_location(
    location: LocationId = Body(),
    location_service: LocationService = Depends(location_service)
):
    return await location_service.delete_location(location)
