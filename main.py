from modules.input import get_input, unpack_input, verify_input, save_input
from modules.output import get_rate, print_output_data
from modules.database_handler import create_table, send_to_db
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
            output_data = get_rate(first_currency, second_currency)
            # Preparing data for printing
            base_currency = output_data['base_curr']
            endpoint_currency = output_data['endpoint_curr']
            rate = output_data['rate']
            color = output_data['printing_color']
            # Print data
            print_output_data(base_currency, endpoint_currency, rate, color)
            # Preparing data for database
            datetime = output_data['date_time']
            # Save data in database
            send_to_db(datetime, base_currency, endpoint_currency, rate)

            if conversions_counter == 1:
                create_table()

        else:
            print('wrong input')