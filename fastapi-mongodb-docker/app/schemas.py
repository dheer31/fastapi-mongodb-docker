from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    description: Optional[str] = Field(None, max_length=500)
    price: float = Field(0.0, ge=0)


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=120)
    description: Optional[str] = Field(None, max_length=500)
    price: Optional[float] = Field(None, ge=0)


class ItemOut(ItemBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
