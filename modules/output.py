from modules.api_handler import get_conversion_rate
from colorama import Fore, Style
from modules.date_handler import get_date_time

# Get printing color depending on higher/lower rate
def get_color(today_rate, yesterday_rate):
    if today_rate >= yesterday_rate:
        return Fore.GREEN
    else: 
        return Fore.RED

def get_rate(first_currency, second_currency):
    # Get latest and yesterday conversion rate for currency pair
    latest_convert_rate, yesterday_convert_rate = get_conversion_rate(first_currency, second_currency)
    printing_color = get_color(latest_convert_rate, yesterday_convert_rate)
    # Prepare data for dictionary
    rounded_latest_rate = round(latest_convert_rate, 2)
    date_time = get_date_time()
    # Create dict from user input and API's output
    output_dict = {}
    output_dict.update({'date_time': date_time, 'base_curr': first_currency, 'endpoint_curr': second_currency, 'rate': rounded_latest_rate, 'printing_color': printing_color})
    return output_dict

def print_output_data(base_currency, endpoint_currency, rate, printing_color):
    print(f'1 {base_currency} = ' + printing_color + f'{rate}', end='')
    print(Style.RESET_ALL, end=' ')
    print(endpoint_currency)