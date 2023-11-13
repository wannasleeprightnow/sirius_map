from fastapi import APIRouter, Body, Depends, UploadFile, File
from PIL import Image
from io import BytesIO
import base64


router = APIRouter(prefix="/map", tags=["map"])


@router.get("/default")
async def get_default_map():
    image = Image.open("/home/wannasleep/code/sirius_map/backend/src/api/routers/a.png")
    imgByteArr = BytesIO()
    image.save(imgByteArr, format=image.format)
    imgByteArr = imgByteArr.getvalue()
    return {"map": base64.b64decode(imgByteArr)}


@router.get("/route")
async def get_map_with_route():
    return "endpoint for map with route"
