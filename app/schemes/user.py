from pydantic import BaseModel


class UserScheme(BaseModel):
    name: str
    password: str
    family_name: str
    email: str
    phone_number: str
    role_id: int
