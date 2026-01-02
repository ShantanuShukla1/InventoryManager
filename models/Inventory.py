from InventoryItem import InventoryItem
from Product import Product

class Inventor:
    def __init__(
            self,
    ):
        self.items = {}

    def add_product(self, product: Product, qty: int):
        if qty < 0:
            raise ValueError("Quantity cannot be negative")
        if product.product_id in self.items:
            self.items[product.product_id].increase_stock(qty)
        else:
            self.items[product.product_id] = InventoryItem(product, qty)

    def check_availability(self, product_id: int, qty: int):
        return self.items[product_id].is_available(qty)

    def reduce_stock(self, product_id: int, qty: int):
        self.items[product_id].decrease_stock(qty)