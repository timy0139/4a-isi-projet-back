from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "user"

    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    password: str
    is_admin: bool = Field(default=False)
    is_blocked: bool = Field(default=False)