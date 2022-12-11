from app.api.api_v1 import app
import uvicorn


@app.get("/")
def hello():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)


# alembic  upgrade head
# alembic downgrade id
# alembic revision -m "<<declaration>>"
