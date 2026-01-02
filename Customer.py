import Order

class Customer:
    def __init__(
            self,
            customer_id: int,
            name: str,
            email: str,
            orders: list[Order]
    ):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.orders = orders

    def place_order(self, order):
        self.orders.append(order)

    def get_order_history(self):
        return self.orders

    def get_total_spent(self) -> float:
        """Return total money spent by the customer."""
        return sum(order.calculate_total() for order in self.orders)

    def __repr__(self) -> str:
        return (
            f"Customer(id={self.customer_id}, "
            f"name='{self.name}', "
            f"email='{self.email}')"
        )