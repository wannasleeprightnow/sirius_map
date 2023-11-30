from fastapi import APIRouter, Body, Depends

from dependencies import location_service
from services.location import LocationService
from schemas.location import Location, LocationAdd, LocationId, UserLocation

router = APIRouter(prefix="/location", tags=["location"])


@router.get("", response_model=list[Location])
async def get_locations(
    location_service: LocationService = Depends(location_service)
):
    res = await location_service.get_locations()
    return res


@router.post("/favorite/", response_model=UserLocation)
async def post_location_to_user_favorite(
     location: UserLocation = Body(),
     location_service: LocationService = Depends(location_service),
):
    res = await location_service.post_location_to_user_favorite(location)
    return res


@router.get("/favorite/{user_id}", response_model=list[Location])
async def get_favorite_user_locations(
    user_id: int,
    location_service: LocationService = Depends(location_service),
):
    res = await location_service.get_favorite_user_locations(user_id)
    return res


@router.delete("/favorite", response_model=UserLocation)
async def delete_location_from_favorite(
    location: UserLocation = Body(),
    location_service: LocationService = Depends(location_service)
):
    res = await location_service.delete_location_from_favorite(location)
    return res


@router.post("", response_model=Location)
async def post_location(
    location: LocationAdd = Body(),
    location_service: LocationService = Depends(location_service)
):
    res = await location_service.post_location(location)
    return res


@router.put("", response_model=Location)
async def put_location(
    location: Location = Body(),
    location_service: LocationService = Depends(location_service)
):
    res = await location_service.put_location(location)
    return res


@router.delete("", response_model=Location)
async def delete_location(
    location: LocationId = Body(),
    location_service: LocationService = Depends(location_service)
):
    res = await location_service.delete_location(location)
    return res
