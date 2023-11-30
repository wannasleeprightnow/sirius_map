from fastapi import APIRouter, HTTPException
from PIL import Image
from io import BytesIO
import base64


router = APIRouter(prefix="/map", tags=["map"])


@router.get("/default")
async def get_default_map():
    # image = Image.open("/home/wannasleep/code/sirius_map/backend/src/api/routers/a.png")
    # imgByteArr = BytesIO()
    # image.save(imgByteArr, format=image.format)
    # imgByteArr = imgByteArr.getvalue()
    # return {"map": base64.b64decode(imgByteArr)}
    raise HTTPException(
        status_code=501,
        detail="Not implemented"
    )


@router.get("/route")
async def get_map_with_route():
    raise HTTPException(
        status_code=501,
        detail="Not implemented"
    )
