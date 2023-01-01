import traceback

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from ....schemes.user import UserScheme
from ....services import user_service
from ....core import AuthController


router = APIRouter()


@router.post("/register")
def register(user: UserScheme):
    try:
        user_service.register(user_credentials=user)
        return JSONResponse(
            status_code=200,
            content={
                "msg": "SUCCESS"
            }
        )
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={
                "msg": f"An error occurred. Details {str(e)}"
            }
        )


@router.post("/login")
def login(email: str, password: str):
    try:
        encoded_token_response = user_service.login(email=email, password=password)
        return JSONResponse(
            status_code=200,
            content=encoded_token_response.to_dict()
        )
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={
                "msg": f"An error occurred. Details {str(e)}"
            }
        )


@router.get("/me")
def me(user=Depends(AuthController)):
    try:
        return JSONResponse(
            status_code=200,
            content=user.to_dict()
        )
    except Exception as e:
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={
                "msg": f"An error occurred. Details {str(e)}"
            }
        )
