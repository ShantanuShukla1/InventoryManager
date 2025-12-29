from Product import Product

class InventoryItem:
    def __init__(
            self,
            product: Product,
            quantity: int
    ):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.product = product
        self.quantity = quantity

    def increase_stock(self, amount: int):
        if amount > 0 & amount < self.quantity:
            self.quantity += amount

    def decrease_stock(self, amount: float):
        if amount > 0:
            self.quantity -= amount

    def is_available(self, requested_qty):
        if requested_qty > 0:
            return requested_qty >= self.quantity
        return False

    def __repr__(self) -> str:
        return f"InventoryItem(product={self.product.name}, quantity={self.quantity})"