from fastapi import FastAPI

from api.routes.products import router as product_router
from api.routes.orders import router as order_router
from db.database import initialize_db

app = FastAPI(title="Inventory Manager API")

initialize_db()

app.include_router(product_router)
app.include_router(order_router)
