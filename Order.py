from datetime import datetime
import OrderStatus
import Customer
import OrderItem

class Order:
    def __init__(self, order_id: int, customer: Customer, items: list[OrderItem], status: OrderStatus, created_at: datetime):
        self.order_id = order_id
        self.customer = customer
        self.items = items
        self.status = status
        self.created_at = created_at
        self.updated_at = created_at