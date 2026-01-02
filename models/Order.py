from typing import List
from enum import Enum

from models.OrderItem import OrderItem


class OrderStatus(Enum):
    PENDING = "Pending"
    PAID = "Paid"
    SHIPPED = "Shipped"
    CANCELLED = "Cancelled"


class Order:
    _id_counter = 1

    def __init__(
            self,
            customer_id: int
    ):
        self.order_id = Order._id_counter
        Order._id_counter += 1
        self.customer_id = customer_id
        self.items: List[OrderItem] = []
        self.status = OrderStatus.PENDING

    def add_item(self, item: OrderItem):
        self.items.append(item)

    def remove_item(self, product_id: int):
        self.items = [
            item for item in self.items
            if item.product.id != product_id
        ]

    def calculate_total(self) -> float:
        return sum(item.get_subtotal() for item in self.items)


    def mark_paid(self):
        if self.status != OrderStatus.PENDING:
            raise ValueError("Only pending orders can be paid")
        self.status = OrderStatus.PAID

    def ship(self):
        if self.status != OrderStatus.PAID:
            raise ValueError("Only paid orders can be shipped")
        self.status = OrderStatus.SHIPPED

    def cancel(self):
        if self.status == OrderStatus.SHIPPED:
            raise ValueError("Shipped orders cannot be cancelled")
        self.status = OrderStatus.CANCELLED


    def is_active(self) -> bool:
        return self.status in {OrderStatus.PENDING, OrderStatus.PAID}

    def __repr__(self) -> str:
        return (
            f"Order(id={self.order_id}, "
            f"customer_id={self.customer_id}, "
            f"status={self.status.value}, "
            f"total={self.calculate_total():.2f})"
        )

"""
Orders fail if any item is out of stock

Stock is reduced only after order confirmation

Cancelling an order restores stock

Orders cannot be modified after confirmation

Prices are locked at order time
"""