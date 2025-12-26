import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

# Carrega as variáveis do arquivo .env
load_dotenv()

# --- Bloco completo de variáveis ---
STOCK_NAME = os.environ.get("STOCK_NAME")
COMPANY_NAME = os.environ.get("COMPANY_NAME")

STOCK_ENDPOINT = os.environ.get("STOCK_ENDPOINT")
NEWS_ENDPOINT = os.environ.get("NEWS_ENDPOINT")

STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")
MY_NUMBER = os.environ.get("MY_NUMBER")
# --- Fim do bloco de variáveis ---

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"Preço de ontem: {yesterday_closing_price}")

day_befere_yesterday_data = data_list[1]
day_befere_yesterday_closing_price = day_befere_yesterday_data["4. close"]
print(f"Preço de anteontem: {day_befere_yesterday_closing_price}")

difference = float(yesterday_closing_price) - float(day_befere_yesterday_closing_price)
print(f"Diferença: {difference}")

diff_percent = (difference / float(day_befere_yesterday_closing_price)) * 100
print(f"Diferença percentual: {diff_percent:.2f}%")

# --- ALTERAÇÃO FEITA AQUI ---
# O script agora só busca notícias se a variação (para cima ou para baixo) for maior que 5%
if abs(diff_percent) > 5:
    print("Variação maior que 5%. Buscando notícias...")

    direction_emoji = "🔺" if difference > 0 else "🔻"

    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }
    new_response = requests.get(NEWS_ENDPOINT, params=news_params)

    articles = new_response.json()["articles"]
    three_articles = articles[:3]  # Pega os 3 primeiros

    formatted_articles = [
        (
            f"{STOCK_NAME}: {direction_emoji}{diff_percent:.2f}%\n"
            f"Headline: {article['title']}.\n"
            f"Brief: {article['description']}"
        )
        for article in three_articles
    ]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=TWILIO_NUMBER,
            to=MY_NUMBER,
        )
        print(f"Mensagem enviada! SID: {message.sid}")
else:
    print("Variação menor que 5%. Nenhuma ação necessária.")
