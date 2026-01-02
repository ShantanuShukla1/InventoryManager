from models.Order import Order, OrderStatus
from db.database import get_connection

class OrderRepository:

    def save(self, order: Order):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO orders (id, customer_id, status) VALUES (?, ?, ?)",
            (order.order_id, order.customer_id, order.status.value)
        )

        conn.commit()
        conn.close()
