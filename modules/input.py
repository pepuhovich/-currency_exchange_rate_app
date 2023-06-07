from modules.api_handler import get_all_symbols
from modules.api_handler import request_latest, request_history, get_all_symbols
from colorama import Fore, Style


# Verify if input currency is supported in API
currency_symbols = get_all_symbols()

def verify_input(symbol_1, symbol_2):
    if symbol_1 in currency_symbols and symbol_2 in currency_symbols:
        return True
    else:
        return False
    

def get_input():
    user_input = input('Enter currency pair of which you want to see the exchange rate (example: eur usd):')
    first_currency = str.upper(user_input[:3])
    second_currency = str.upper(user_input[4:])
    
    return first_currency, second_currency


# Get printing color depenfing on higher/lower rate
def get_color(today_rate, yesterday_rate):
    if today_rate >= yesterday_rate:
        return Fore.GREEN
    else: 
        return Fore.RED
    

def get_conversion_rate(first_currency, second_currency):
    latest_convert_rate = request_latest(first_currency, second_currency)
    yesterday_convert_rate = request_history(first_currency, second_currency)
        
    return latest_convert_rate, yesterday_convert_rate
    

def print_rate(first_currency, second_currency):
    latest_convert_rate, yesterday_convert_rate = get_conversion_rate(first_currency, second_currency)
    printing_color = get_color(latest_convert_rate, yesterday_convert_rate)
    
    rounded_latest_rate = round(latest_convert_rate, 2)

    print(f'1 {first_currency} = ' + printing_color + f'{rounded_latest_rate}', end='')
    print(Style.RESET_ALL, end=' ')
    print(second_currency)