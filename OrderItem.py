from Product import Product

class OrderItem:
    def __init__(
            self,
            product: Product,
            quantity: int
    ):
        self.product = product
        self.quantity = quantity