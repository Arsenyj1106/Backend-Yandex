import requests
BASE_URL = 'https://fakestoreapi.com'

new_user = {
    "email": 'pirogovarceniy@yandex.ru',
    "username": 'Arsenyj1106',
    "password": 'fy3gw8o',
    "name": {
        "firstname": 'Arseny',
        "lastname": 'Pirogov'
    },
    "address": {
        "city": 'Ekaterinburg',
        "street": 'Komsomolskaya',
        "number": 70,
        "zipcode": '12926-3874',
        "geolocation": {
            "lat": '-37.3159',
            "long": '81.1496'
        },
        "phone": '1-570-236-7033'
    }
}

response = requests.post(f"{BASE_URL}/users", params=new_user)
print(response.json())