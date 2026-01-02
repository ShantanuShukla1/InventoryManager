from models.Product import Product

class OrderItem:
    def __init__(
            self,
            product: Product,
            quantity: int
    ):
        self.product = product
        self.quantity = quantity
        self.unit_price = product.price

    def get_subtotal(self):
        return self.unit_price * self.quantity

    def __repr__(self) -> str:
        return (
            f"OrderItem(product={self.product.name}, "
            f"quantity={self.quantity}, "
            f"unit_price={self.unit_price:.2f})"
        )