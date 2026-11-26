from pydantic import BaseModel, Field


class RegisterRequest(BaseModel):
    username: str = Field(min_length=3)


class RegisterResponse(BaseModel):
    id: int
    username: str
    generated_password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class UserPublic(BaseModel):
    id: int
    username: str
    is_admin: bool
    is_blocked: bool


class PasswordChange(BaseModel):
    old_password: str
    new_password: str = Field(min_length=8)


class OrderLineCreate(BaseModel):
    product_id: int | None = None
    menu_id: int | None = None
    quantity: int = Field(default=1, gt=0)


class OrderCreate(BaseModel):
    pickup_date: str
    lines: list[OrderLineCreate]