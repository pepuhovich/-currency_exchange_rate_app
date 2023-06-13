from datetime import datetime, date, timedelta

def get_yesterday_date():
    today = date.today()
    yesterday = today - timedelta(days = 1)
    yesterday_formatted = '{dt.year}/{dt.month}/{dt.day}'.format(dt = yesterday)

    return yesterday_formatted

def get_date_time():
    now = datetime.now()
    # Desired format
    formatted_date_time = now.strftime("%Y-%m-%d %H:%M")
    return formatted_date_time