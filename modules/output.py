from modules.api_handler import get_conversion_rate
from colorama import Fore, Style
from modules.date_handler import get_date_time

# Get printing color depenfing on higher/lower rate
def get_color(today_rate, yesterday_rate):
    if today_rate >= yesterday_rate:
        return Fore.GREEN
    else: 
        return Fore.RED
    
def save_to_dict(base_currency, endpoint_currency, rate):
    date_time = get_date_time()
    output_data = {}
    output_data.update({'date_time': date_time, 'base curr': base_currency, 'endpoint_curr': endpoint_currency, 'rate': rate})
    return output_data

def print_rate(first_currency, second_currency):
    latest_convert_rate, yesterday_convert_rate = get_conversion_rate(first_currency, second_currency)
    printing_color = get_color(latest_convert_rate, yesterday_convert_rate)
    
    rounded_latest_rate = round(latest_convert_rate, 2)

    print(f'1 {first_currency} = ' + printing_color + f'{rounded_latest_rate}', end='')
    print(Style.RESET_ALL, end=' ')
    print(second_currency)

    output_dict = save_to_dict(first_currency, second_currency, rounded_latest_rate)
    print(output_dict)
    return output_dict