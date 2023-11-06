from modules.api_handler import get_conversion_rate
from modules.date_handler import get_date_time


def get_rate(first_currency, second_currency):
    # Get latest and yesterday conversion rate for currency pair
    latest_convert_rate = get_conversion_rate(first_currency, second_currency)
    # Prepare data for dictionary
    rounded_latest_rate = round(latest_convert_rate, 2)
    date_time = get_date_time()
    # Create dict from user input and API's output
    output_dict = {}
    output_dict.update(
        {
            "date_time": date_time,
            "base_curr": first_currency,
            "endpoint_curr": second_currency,
            "rate": rounded_latest_rate,
        }
    )

    return output_dict


def print_output_data(base_currency, endpoint_currency, rate):
    print(f"1 {base_currency} = {rate} {endpoint_currency}")
