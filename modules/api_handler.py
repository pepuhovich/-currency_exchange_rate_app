import requests

def request_latest(currency_1, currency_2):
    # Contacting the API
    response = requests.get(f'https://v6.exchangerate-api.com/v6/23c357f9e77fa0eb7d4495e4/pair/{currency_1}/{currency_2}')
    # Loading the API response into the dictionary
    load_response = response.json() 
    rate = load_response['conversion_rate']

    return '%.2f' % rate


def request_history(currency_1, currency_2):
    # Contacting the API
    response = requests.get(f'https://v6.exchangerate-api.com/v6/23c357f9e77fa0eb7d4495e4/pair/{currency_1}/{currency_2}')
    # Loading the API response into the dictionary
    load_response = response.json() 
    rate = load_response['conversion_rate']

    return '%.2f' % rate


def get_all_symbols():
    symbols = []

    # Contacting the API
    response = requests.get('https://v6.exchangerate-api.com/v6/23c357f9e77fa0eb7d4495e4/codes')
    # Loading the API response into the dictionary
    load_response = response.json() 
    symbols_list = load_response['supported_codes']
    # Parsing symbols into the list (skipping currency name)
    for symbol in symbols_list:
        symbols.append(symbol[0])

    return symbols