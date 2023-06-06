from modules.api_handler import request_latest, request_history, get_all_symbols
from modules.database_handler import show_history
from colorama import Fore


# Verify if input currency is supported in API
currency_symbols = get_all_symbols()

def verify_user_input(symbol):
    if symbol in currency_symbols:
        return True
    else:
        return False

# Get printing color depenfing on higher/lower rate
def get_color(today_rate, yesterday_rate):
    if today_rate >= yesterday_rate:
        return Fore.GREEN
    else: 
        return Fore.RED


while True:
    user_input = input('Enter currency pair of which you want to see the exchange rate (example: eur usd):')
    first_currency = str.upper(user_input[:3])
    second_currency = str.upper(user_input[4:])

    check_currency_1 = verify_user_input(first_currency)
    check_currency_2 = verify_user_input(second_currency)

    
    if check_currency_1 == True and check_currency_2 == True:
        latest_convert_rate = request_latest(first_currency, second_currency)
        yesterday_convert_rate = request_history(first_currency, second_currency)
        printing_color = get_color(latest_convert_rate, yesterday_convert_rate)

        print(f'1 {first_currency} = ' + printing_color + f'{latest_convert_rate} {second_currency}')
        break

    elif check_currency_1 == True and check_currency_2 == False:
        print('Second currency symbol is incorrect')
    elif check_currency_1 == False and check_currency_2 == True:
        print('First currency symbol is incorrect')
    else:
        print('Both currency symbols are incorrect')
        