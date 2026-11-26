from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "user"
    
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    password: str
    is_admin: bool = Field(default=False)
    is_blocked: bool = Field(default=False)


class Product(SQLModel, table=True):
    __tablename__ = "product"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    price: float = Field(ge=0)
    stock: int = Field(default=0, ge=0)
    is_available: bool = Field(default=True)


class Menu(SQLModel, table=True):
    __tablename__ = "menu"
    id: int | None = Field(default=None, primary_key=True)
    name: str
    description: str | None = None
    price: float = Field(ge=0)
    available_from: str
    available_to: str


class MenuProduct(SQLModel, table=True):
    __tablename__ = "menu_product"
    menu_id: int = Field(foreign_key="menu.id", primary_key=True)
    product_id: int = Field(foreign_key="product.id", primary_key=True)


class Order(SQLModel, table=True):
    __tablename__ = "order"
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    pickup_date: str
    status: str = Field(default="en_attente")
    create_at: str | None = None


class OrderLine(SQLModel, table=True):
    __tablename__ = "order_line"
    id: int | None = Field(default=None, primary_key=True)
    order_id: int = Field(foreign_key="order.id")
    product_id: int | None = Field(default=None, foreign_key="product.id")
    menu_id: int | None = Field(default=None, foreign_key="menu.id")
    quantity: int = Field(default=1, gt=0)


class ClosureDay(SQLModel, table=True):
    __tablename__ = "closure_day"
    id: int | None = Field(default=None, primary_key=True)
    date: str
    description: str | None = None