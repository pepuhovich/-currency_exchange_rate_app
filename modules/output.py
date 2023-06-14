from modules.api_handler import get_conversion_rate
from colorama import Fore, Style
from modules.date_handler import get_date_time


# Compare two rate values
def is_higher(today_rate, yesterday_rate):
    if today_rate >= yesterday_rate:
        return True
    else:
        return False


def get_rate(first_currency, second_currency):
    # Get latest and yesterday conversion rate for currency pair
    latest_convert_rate, yesterday_convert_rate = get_conversion_rate(
        first_currency, second_currency
    )
    # Prepare data for dictionary
    rounded_latest_rate = round(latest_convert_rate, 2)
    date_time = get_date_time()
    rates_compare_result = is_higher(latest_convert_rate, yesterday_convert_rate)
    # Create dict from user input and API's output
    output_dict = {}
    output_dict.update(
        {
            "date_time": date_time,
            "base_curr": first_currency,
            "endpoint_curr": second_currency,
            "rate": rounded_latest_rate,
            "is_higher": rates_compare_result,
        }
    )

    return output_dict


def get_color(is_rate_higher):
    if is_rate_higher == True:
        return Fore.GREEN
    elif is_rate_higher == False:
        return Fore.RED


def print_output_data(base_currency, endpoint_currency, rate, is_rate_higher):
    printing_color = get_color(is_rate_higher)
    print(f"1 {base_currency} = " + printing_color + f"{rate}", end="")
    print(Style.RESET_ALL, end=" ")
    print(endpoint_currency)
