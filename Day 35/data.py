import requests as req

api = "https://opentdb.com/api.php"
params = {
        "amount": 10,
        "type": "boolean",
    }

response = req.get(url=api, params=params)
data_response = response.json()
question_data = data_response["results"]
