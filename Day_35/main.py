import requests
from twilio.rest import Client

# === CONFIGURAÇÕES ===
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "SUA_API_KEY"

ACCOUNT_SID = "SEU_ACCOUNT_SID"
AUTH_TOKEN = "SEU_AUTH_TOKEN"
NUMERO_TWILIO = "whatsapp:+14155238886"  # número do sandbox Twilio WhatsApp
NUMERO = "whatsapp:+55SEUNUMERO"  # seu número (ex: whatsapp:+5585987654321)

# Coordenadas (exemplo: Fortaleza)
weather_params = {
    "lat": -3.71722,
    "lon": -38.5433,
    "appid": API_KEY,
    "cnt": 4,  # próximas 12h
}

# === OBTÉM PREVISÃO ===
response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# === ENVIA MENSAGEM WHATSAPP ===
client = Client(ACCOUNT_SID, AUTH_TOKEN)

if will_rain:
    body_msg = "☔ Vai chover nas próximas horas em Fortaleza! Leve um guarda-chuva!"
else:
    body_msg = "🌤️ Sem chuva prevista nas próximas horas em Fortaleza!"

message = client.messages.create(body=body_msg, from_=NUMERO_TWILIO, to=NUMERO)

print("Mensagem enviada com status:", message.status)
