import requests
import json
url = 'https://sms-spam-prediction.onrender.com/predict'


def req(message):
    response = requests.get(url, params={"message": message})
    return response.json()
