from typing import Optional

from sqlmodel import Field, SQLModel


class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    store_id: int = Field()
    store_name: str = Field(index=True)
    title: str = Field()
    handle: int = Field(nullable=True)
    published: str = Field()
