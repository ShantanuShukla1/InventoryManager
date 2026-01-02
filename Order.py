from typing import List
from enum import Enum

from OrderItem import OrderItem


class OrderStatus(Enum):
    PENDING = "Pending"
    PAID = "Paid"
    SHIPPED = "Shipped"
    CANCELLED = "Cancelled"


class Order:
    def __init__(self, order_id: int, customer: Customer, items: list[OrderItem], status: OrderStatus, created_at: datetime):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.status = status
        self.created_at = created_at
        self.updated_at = created_at