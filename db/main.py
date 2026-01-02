from db.database import initialize_db
from db.product_repo import ProductRepository
from db.order_repo import OrderRepository
from db.orderitem_repo import OrderItemRepository
from models.Product import Product
from models.Order import Order
from models.OrderItem import OrderItem

initialize_db()

product_repo = ProductRepository()
order_repo = OrderRepository()
item_repo = OrderItemRepository()

p = Product(1, "Keyboard", 49.99, "Mechanical keyboard", "Electronics")

product_repo.save(p)

order = Order(customer_id=101)
order.add_item(OrderItem(p, 2))

order_repo.save(order)
for item in order.items:
    item_repo.save(order.order_id, item)
