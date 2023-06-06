from modules.api_handler import request_api, get_symbols
from modules.database_handler import show_history

currency_symbols = get_symbols()

def verify_user_input(symbol):
    if symbol in currency_symbols:
        return True
    else:
        return False



while True:
    user_input = input('Enter currency pair of which you want to see the exchange rate (example: eur usd):')
    first_currency = str.casefold(user_input[:3])
    second_currency = str.casefold(user_input[4:])

    print(first_currency)
    print(second_currency)

    currency_1 = verify_user_input(first_currency)
    currency_2 = verify_user_input(second_currency)

    
    if currency_1 == True and currency_2 == True:
        print('Correct pair')
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