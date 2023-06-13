from modules.input import get_input, unpack_input, verify_input, save_input
from modules.output import print_rate
from modules.database_handler import create_table
from modules.date_handler import get_date_time


while True:
    conversions_counter = 0
    user_input = get_input()
    
    if user_input == 'quit':
        print('...closing the app')
        break
    elif user_input == 'history':
        print('something')
    else:
        first_currency, second_currency = unpack_input(user_input)
        if verify_input(first_currency, second_currency):
            conversions_counter=+1 
            print_rate(first_currency, second_currency)
            print(print_rate())
            if conversions_counter == 1:
                create_table()

        else:
            print('wrong input')