from modules.api_handler import request_latest, get_all_symbols
from modules.database_handler import show_history

currency_symbols = get_all_symbols()

def verify_user_input(symbol):
    if symbol in currency_symbols:
        return True
    else:
        return False



while True:
    user_input = input('Enter currency pair of which you want to see the exchange rate (example: eur usd):')
    first_currency = str.upper(user_input[:3])
    second_currency = str.upper(user_input[4:])

    currency_1 = verify_user_input(first_currency)
    currency_2 = verify_user_input(second_currency)

    
    if currency_1 == True and currency_2 == True:
        convert_rate = request_latest(first_currency, second_currency)
        print(f'1 {first_currency} = {convert_rate} {second_currency}')
        break
    elif currency_1 == True and currency_2 == False:
        print('Second currency symbol is incorrect')
        break
    elif currency_1 == False and currency_2 == True:
        print('First currency symbol is incorrect')
        break
    else:
        print('Both currency symbols are incorrect')
        break