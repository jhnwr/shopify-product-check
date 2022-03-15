from typing import Optional

from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    # Optional because if we use this field as auto id increment
    # the value would be None before it gets to the database
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    store_id: int = Field()
    store_name: str = Field(index=True)
    title: str = Field()
    handle: str = Field(nullable=True)
    published: str = Field()
