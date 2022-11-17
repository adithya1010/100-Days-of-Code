import requests
from datetime import datetime

# Creating new username with new key using pixela's user endpoint

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "adithya1010"
TOKEN = "P15EikSSJvRponh1qQd8H3vX3mujVnZj"
GRAPH_ID = "graph1"
# Setting parameters for the endpoint

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating a new graph using Pixela's Graph Endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Setting parameters for the graph endpoints

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# Adding pixels with Pixel creation endpoint
pixel_creation_endpoint = f"{pixela_endpoint}/adithya1010/graphs/graph1"

# Setting parameters for the pixel creation endpoints

today = datetime.now()

today_formatted = today.strftime("%Y%m%d")
print(today_formatted)

pixel_config = {
    "date": today_formatted,
    "quantity": input("How many kilometers did you cycle today?"),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_config, headers=headers)
print(response.text)

# Updating the pixel values present in the graph

# update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"
#
# updated_pixel_config = {
#     "quantity": "14.5"
# }
#
# put_response = requests.put(url=update_pixel_endpoint, json=updated_pixel_config, headers=headers)
# print(put_response)

# Deleting the pixel values present in the graph

# delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"
#
# delete_response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(delete_response)


