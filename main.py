from modules.input import get_input, unpack_input, verify_input
from modules.output import get_rate, print_output_data
from modules.database_handler import send_to_db, print_from_db


def main():
    while True:
        user_input = get_input()

        if user_input == "quit":
            print("...closing the app")
            break
        elif user_input == "history":
            print_from_db()
            break
        else:
            first_currency, second_currency = unpack_input(user_input)
            if verify_input(first_currency, second_currency):
                output_data = get_rate(first_currency, second_currency)
                # Preparing data for printing
                base_currency = output_data["base_curr"]
                endpoint_currency = output_data["endpoint_curr"]
                rate = output_data["rate"]
                # Print data
                print_output_data(base_currency, endpoint_currency, rate)
                # Preparing date for saving in database
                datetime = output_data["date_time"]
                # Save data in database
                send_to_db(datetime, base_currency, endpoint_currency, rate)
            else:
                print("wrong input")


if __name__ == "__main__":
    main()
