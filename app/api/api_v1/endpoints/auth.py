from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.get("/login")
def login():
    return JSONResponse(
        status_code=200,
        content={
            "msg": "SUCCESS"
        }
    )
