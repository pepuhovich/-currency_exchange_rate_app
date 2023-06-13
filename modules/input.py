from modules.api_handler import get_all_symbols

# Verify if input currency is supported in API
currency_symbols = get_all_symbols()

def get_input():
    user_response = input('Enter currency pair of which you want to see the exchange rate (example: eur usd):')

    if user_response == 'quit':
        return 'quit'
    elif user_response == 'history':
        return 'history'
    else:
        return user_response

def unpack_input(user_input):
    first_currency = str.upper(user_input[:3])
    second_currency = str.upper(user_input[4:])
    return first_currency, second_currency

def verify_input(symbol_1, symbol_2):
    if symbol_1 in currency_symbols and symbol_2 in currency_symbols:
        return True
    else:
        return False
    
def save_input(date_time, first_currency, second_currency, rate):
    data_for_database = {}
    data_for_database.update({'date_time', date_time, 'base_currency', first_currency, 'endpoint_currency', second_currency, 'conversion_rate', rate})
    print(data_for_database)