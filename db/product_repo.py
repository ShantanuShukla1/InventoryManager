from models.Product import Product
from db.database import get_connection

class ProductRepository:

    def save(self, product: Product):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO products (id, name, price) VALUES (?, ?, ?)",
            (product.id, product.name, product.price)
        )

        conn.commit()
        conn.close()

    def get_by_id(self, product_id: int) -> Product | None:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, name, price FROM products WHERE id = ?",
            (product_id,)
        )

        row = cursor.fetchone()
        conn.close()

        if row:
            return Product(*row)
        return None
