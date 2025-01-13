import requests
import json


BASE_URL = "https://fakestoreapi.com"

response = requests.get(f"{BASE_URL}/products/category/jewelery")
jewelery_products = response.json()
print("\nПродукты из категории 'jewelery':")
for product in jewelery_products:
    print(f"- {product['title']} (${product['price']})")