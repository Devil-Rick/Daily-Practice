import requests as req
from datetime import datetime

# ------------------- Getting the date ----------------------- #
today = datetime.now()
today_date = today.strftime("%Y%m%d")
print(today_date)

# ------------------- creating the User ----------------------- #
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

response_user = req.post(pixela_endpoint, json=pixela_user_params)
print(response_user.text)


# ------------------- Creating the Graph ----------------------- #
# https://pixe.la/v1/users/tester2000/graphs/graphcode.html (To View graph)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_header = {
    "X-USER-TOKEN": TOKEN
}
graph_params = {
    "id": "graphcode",
    "name": "Coding Hours",
    "unit": "mins",
    "type": "int",
    "color": "kuro"
}

response_graph = req.post(graph_endpoint, headers=graph_header, json=graph_params)
print(response_graph.text)


# ------------------- Giving the graph initial data ----------------------- #

input_hours = f"{pixela_endpoint}/{USERNAME}/graphs/graphcode"
input_header = {
    "X-USER-TOKEN": TOKEN
}
input_params = {
    "date": today_date,
    "quantity": "4"
}

response_input = req.post(input_hours, headers=input_header, json=input_params)
print(response_input.text)


# ------------------- Updating the data Daily ----------------------- #
# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd> (To Update Data)

update_hours = f"{pixela_endpoint}/{USERNAME}/graphs/graphcode/{today_date}"
update_header = {
    "X-USER-TOKEN": TOKEN
}
update_params = {
    "quantity": "2"
}

response_update = req.put(update_hours, headers=update_header, json=input_params)
print(response_update.text)


# ------------------- Deleting the data if not Required ----------------------- #
# /v1/users/<username>/graphs/<graphID>/

del_graph = f"{pixela_endpoint}/{USERNAME}/graphs/graphcode/{today_date}"
del_header = {
    "X-USER-TOKEN": TOKEN
}
response_del = req.delete(del_graph, headers=del_header)
print(response_del.text)
