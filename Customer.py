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