from modules.api_handler import request_api
from modules.database_handler import show_history

currency_pair = ''



while True:
    user_input = input(str.casefold('Enter currency pair of which you want to see the exchange rate (example: eur usd):'))
    
    if user_input is currency_pair:
        request_api()
    
    elif user_input is 'history':
        show_history()
        break

    elif user_input is 'quit':
        break

    