from models.OrderItem import OrderItem
from db.database import get_connection

class OrderItemRepository:

    def save(self, order_id: int, item: OrderItem):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO order_items
            (order_id, product_id, quantity, unit_price)
            VALUES (?, ?, ?, ?)
            """,
            (order_id, item.product.id, item.quantity, item.unit_price)
        )

        conn.commit()
        conn.close()
