import requests
import json


BASE_URL = "https://fakestoreapi.com"

response = requests.get(f"{BASE_URL}/products/categories")
categories = response.json()
print("\nКатегории:")
for category in categories:
    print(f"- {category}")