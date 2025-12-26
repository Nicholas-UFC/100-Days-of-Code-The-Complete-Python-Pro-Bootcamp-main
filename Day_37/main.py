from datetime import datetime

import requests

TOKEN = "meutokensecreto12345"
USERNAME = "bryan12345678910"
ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5.00",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime("%Y%m%d")}"

new_pixel_data = {"quantity": "4.5"}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime("%Y%m%d")}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
