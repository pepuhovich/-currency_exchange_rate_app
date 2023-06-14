import os
from dotenv import load_dotenv
import requests
from modules.date_handler import get_yesterday_date

# Read API from .env file
load_dotenv()
API_KEY = os.getenv("KEY")


def request_latest(currency_1, currency_2):
    # Contacting the API
    response = requests.get(
        f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency_1}/{currency_2}"
    )
    # Loading the API response into the dictionary
    load_response = response.json()
    # Getting the specific value from dict
    rate = load_response["conversion_rate"]

    return rate


def request_history(currency_1, currency_2):
    # Getting yesterday date for using in API URL
    yesterday_date = get_yesterday_date()
    # Contacting the API for all base currency rates from yesterday
    response = requests.get(
        f"https://v6.exchangerate-api.com/v6/{API_KEY}/history/{currency_1}/{yesterday_date}"
    )
    # Loading the API response into the dictionary
    load_response = response.json()
    # Getting the specific endpoint currency from dict
    rate = load_response["conversion_rates"][currency_2]

    return rate


# Verify that given currency codes are supported in the API
def get_all_symbols():
    symbols = []
    # Contacting the API
    response = requests.get("https://v6.exchangerate-api.com/v6/{API_KEY}/codes")
    # Loading the API response into the dictionary
    load_response = response.json()
    symbols_list = load_response["supported_codes"]
    # Parsing symbols into the list (skipping currency name)
    for symbol in symbols_list:
        symbols.append(symbol[0])

    return symbols


def get_conversion_rate(first_currency, second_currency):
    latest_convert_rate = request_latest(first_currency, second_currency)
    yesterday_convert_rate = request_history(first_currency, second_currency)

    return latest_convert_rate, yesterday_convert_rate
