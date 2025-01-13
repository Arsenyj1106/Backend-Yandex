import requests
import json


BASE_URL = "https://fakestoreapi.com"

response = requests.get(f"{BASE_URL}/products")
products = response.json()
print("Продукты с ценой < 20:")
for product in products:
    if product['price'] < 20:
        print(f"- {product['title']} (${product['price']})")
