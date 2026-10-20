from fastapi import FastAPI

app = FastAPI()


products = [
    {"id": 1, "name": "Laptop", "category": "electronics", "price": 60000},
    {"id": 2, "name": "Mouse", "category": "electronics", "price": 1000},
    {"id": 3, "name": "Chair", "category": "furniture", "price": 5000},
    {"id": 4, "name": "Keyboard", "category": "electronics", "price": 3000},
    {"id": 5, "name": "Table", "category": "furniture", "price": 8000}
]


@app.get("/products/{product_id}")
def get_product(
    product_id: int,
    include_price: bool = True
):
    for product in products:
        if product["id"] == product_id:
            if not include_price:
                return {
                    "id": product["id"],
                    "name": product["name"],
                    "category": product["category"]
                }

            return product

    return {"message": "Product not found"}


@app.get("/products")
def get_products(
    category: str | None = None,
    max_price: int | None = None,
    limit: int = 10
):
    result = products

    if category is not None:
        result = [
            product
            for product in result
            if product["category"] == category
        ]

    if max_price is not None:
        result = [
            product
            for product in result
            if product["price"] <= max_price
        ]

    return result[:limit]