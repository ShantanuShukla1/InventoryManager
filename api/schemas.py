from pydantic import BaseModel
from typing import List, Optional

class ProductCreate(BaseModel):
    id: int
    name: str
    price: float
    description: str
    category: str

class ProductResponse(ProductCreate):
    pass

class OrderItemCreate(BaseModel):
    product_id: int
    quantity: int

class OrderCreate(BaseModel):
    customer_id: int
    items: List[OrderItemCreate]

class OrderResponse(BaseModel):
    order_id: int
    customer_id: int
    status: str
