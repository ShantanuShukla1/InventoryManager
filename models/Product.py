class Product:
    def __init__(
            self,
            product_id: int,
            name: str,
            price: float,
            description: str,
            category: str
    ):
        if price < 0:
            raise ValueError("Price cannot be negative")

        self.product_id = product_id
        self.name = name
        self.price = price
        self.description = description
        self.category = category

    @property
    def id(self):
        return self.product_id

    def update_price(self, new_price: float):
        if new_price < 0:
            raise ValueError("Price cannot be negative")
        self.price = new_price

    def to_dict(self):
        return {
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "description": self.description,
            "category": self.category
        }

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return self.product_id == other.product_id

    def __repr__(self) -> str:
        return (
            f"Product(id={self.product_id}, "
            f"name='{self.name}', "
            f"price={self.price:.2f})"
        )

