import requests as req
from datetime import date

# https://pixe.la/@tester2000 (website)

TOKEN = "fRvb484TB45VRT5e471b41e94tR"
USERNAME = "tester2000"

pixela_endpoint = "https://pixe.la/v1/users"
pixela_user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = req.post(pixela_endpoint, json=pixela_user_params)
# print(response.text)


# https://pixe.la/v1/users/tester2000/graphs/graph2000.html (To View graph)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_header = {
    "X-USER-TOKEN": TOKEN
}
graph_params = {
    "id": "graph2000",
    "name": "Coding Hours",
    "unit": "min",
    "type": "int",
    "color": "kuro"
}

# response = req.post(graph_endpoint, headers=graph_header, json=graph_params)
# print(response.text)

# input response to the graph
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph2000"
update_header = {
    "X-USER-TOKEN": TOKEN
}
update_params = {
    "date": "20220814",
    "quantity": "130"
}

response = req.post(update_endpoint, headers=update_header, json=update_params)
print(response.text)






