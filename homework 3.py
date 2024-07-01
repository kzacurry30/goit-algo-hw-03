from datetime import datetime


def get_days_from_today(date):
    try:
        date = datetime.strptime(date, '%Y-%m-%d')

        today = date.today()

        delta = today - date
        return delta.days
    except ValueError:
        return "Invalid date"
    except TypeError:
        return type(date)

print(get_days_from_today('2020-10-09'))