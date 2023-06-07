from datetime import date, timedelta

def get_yesterday_date():
    today = date.today()
    yesterday = today - timedelta(days = 1)
    yesterday_formatted = '{dt.year}/{dt.month}/{dt.day}'.format(dt = yesterday)

    return yesterday_formatted