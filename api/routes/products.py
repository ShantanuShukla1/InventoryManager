from fastapi import APIRouter, HTTPException, status
from typing import List

from db.product_repo import ProductRepository
from models.Product import Product
from api.schemas import ProductCreate, ProductResponse

router = APIRouter()
repo = ProductRepository()

@router.get("/products", response_model=List[ProductResponse])
def get_products():
    return repo.get_all()

@router.post(
    "/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product(product: ProductCreate):
    try:
        p = Product(
            product.id,
            product.name,
            product.price,
            product.description,
            product.category
        )
        repo.save(p)
        return product
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
