import requests
import json


BASE_URL = "https://fakestoreapi.com"

response = requests.get(f"{BASE_URL}/users")
users = response.json()
print("\nПользователи:")
for user in users:
    print(f"- {user['name']['firstname']} {user['name']['lastname']}")