#Question 1: Add 3 More Products
from fastapi import FastAPI
app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB Hub", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor Stand", "price": 1999, "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Desk Lamp", "price": 799, "category": "Accessories", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}


# Question 2: Filter products by category
from fastapi import FastAPI
app = FastAPI()
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB Hub", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor Stand", "price": 1999, "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Desk Lamp", "price": 799, "category": "Accessories", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}
@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}
@app.get("/products/{category}")
def get_products_by_category(category: str):
    filtered = [p for p in products if p["category"].lower() == category.lower()]
    return {"category": category, "products": filtered, "total": len(filtered)}


#Question 3:Show Only In-Stock Products
from fastapi import FastAPI
app = FastAPI()

products = [
    {"id": 1, "name": "Wireless Mouse", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB Hub", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor Stand", "price": 1999, "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Desk Lamp", "price": 799, "category": "Accessories", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]
@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}

@app.get("/products/instock")
def get_instock():
    result = [p for p in products if p["in_stock"] == True]
    return {"in_stock_products": result, "count": len(result)}


#Question 4: Build a Store Info Endpoint
from fastapi import FastAPI
app = FastAPI()
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB Hub", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor Stand", "price": 1999, "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Desk Lamp", "price": 799, "category": "Accessories", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}

@app.get("/products/instock")
def get_instock():
    result = [p for p in products if p["in_stock"] == True]
    return {"in_stock_products": result, "count": len(result)}

@app.get("/store/summary")
def store_summary():
    total = len(products)
    in_stock = len([p for p in products if p["in_stock"] == True])
    out_of_stock = len([p for p in products if p["in_stock"] == False])
    categories = list(set([p["category"] for p in products]))
    return {
        "store_name": "My E-commerce Store",
        "total_products": total,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }



    
#Question 5: Search Products by Name
from fastapi import FastAPI
app = FastAPI()
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB Hub", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor Stand", "price": 1999, "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Desk Lamp", "price": 799, "category": "Accessories", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}

@app.get("/products/instock")
def get_instock():
    result = [p for p in products if p["in_stock"] == True]
    return {"in_stock_products": result, "count": len(result)}

@app.get("/store/summary")
def store_summary():
    total = len(products)
    in_stock = len([p for p in products if p["in_stock"] == True])
    out_of_stock = len([p for p in products if p["in_stock"] == False])
    categories = list(set([p["category"] for p in products]))
    return {
        "store_name": "My E-commerce Store",
        "total_products": total,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    results = [p for p in products if keyword.lower() in p["name"].lower()]
    if not results:
        return {"message": "No products matched your search"}
    return {"keyword": keyword, "results": results, "total_matches": len(results)}



#Question Bonus : Cheapest & Most Expensive Product
from fastapi import FastAPI
app = FastAPI()
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 999, "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB Hub", "price": 1499, "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Monitor Stand", "price": 1999, "category": "Accessories", "in_stock": False},
    {"id": 4, "name": "Desk Lamp", "price": 799, "category": "Accessories", "in_stock": True},
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]

@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}

@app.get("/products/instock")
def get_instock():
    result = [p for p in products if p["in_stock"] == True]
    return {"in_stock_products": result, "count": len(result)}

@app.get("/store/summary")
def store_summary():
    total = len(products)
    in_stock = len([p for p in products if p["in_stock"] == True])
    out_of_stock = len([p for p in products if p["in_stock"] == False])
    categories = list(set([p["category"] for p in products]))
    return {
        "store_name": "My E-commerce Store",
        "total_products": total,
        "in_stock": in_stock,
        "out_of_stock": out_of_stock,
        "categories": categories
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    results = [p for p in products if keyword.lower() in p["name"].lower()]
    if not results:
        return {"message": "No products matched your search"}
    return {"keyword": keyword, "results": results, "total_matches": len(results)}

@app.get("/products/deals")
def get_deals():
    best_deal = min(products, key=lambda p: p["price"])
    premium_pick = max(products, key=lambda p: p["price"])
    return {
        "best_deal": best_deal,
        "premium_pick": premium_pick
    }