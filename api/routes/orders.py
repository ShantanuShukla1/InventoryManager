from fastapi import APIRouter, HTTPException, status

from db.order_repo import OrderRepository
from db.orderitem_repo import OrderItemRepository
from db.product_repo import ProductRepository
from models.Order import Order
from models.OrderItem import OrderItem
from api.schemas import OrderCreate, OrderResponse

router = APIRouter()

order_repo = OrderRepository()
item_repo = OrderItemRepository()
product_repo = ProductRepository()

@router.post(
    "/orders",
    response_model=OrderResponse,
    status_code=status.HTTP_201_CREATED
)
def create_order(order_data: OrderCreate):
    order = Order(order_data.customer_id)

    for item in order_data.items:
        product = product_repo.get_by_id(item.product_id)
        if not product:
            raise HTTPException(
                status_code=404,
                detail=f"Product {item.product_id} not found"
            )

        order.add_item(OrderItem(product, item.quantity))

    order_repo.save(order)

    for item in order.items:
        item_repo.save(order.order_id, item)

    return {
        "order_id": order.order_id,
        "customer_id": order.customer_id,
        "status": order.status
    }

@router.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(order_id: int):
    order = order_repo.get_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    return {
        "order_id": order.order_id,
        "customer_id": order.customer_id,
        "status": order.status
    }

@router.post("/orders/{order_id}/cancel")
def cancel_order(order_id: int):
    order = order_repo.get_by_id(order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")

    if order.status == "CANCELLED":
        raise HTTPException(status_code=400, detail="Order already cancelled")

    order.cancel()
    order_repo.update_status(order_id, order.status)

    return {"message": "Order cancelled"}
