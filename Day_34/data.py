import requests

parametros = {"amount": 10, "type": "boolean"}
data = requests.get(
    "https://opentdb.com/api.php?amount=10&type=boolean", params=parametros
)
data.raise_for_status()

question_data_all = data.json()
question_data = question_data_all["results"]
