from fastapi import FastAPI
from .endpoints.auth import router as auth_router

app = FastAPI()
app.mount("/api/v1", app)


app.include_router(auth_router, prefix="/auth", tags=["auth"])

