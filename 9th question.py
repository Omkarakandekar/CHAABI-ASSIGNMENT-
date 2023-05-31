from datetime import datetime, timedelta

def check_date_difference(from_date, to_date, difference):
    date_format = '%y-%m-%d'
    from_date_obj = datetime.strptime(from_date, date_format)
    to_date_obj = datetime.strptime(to_date, date_format)
    date_difference = to_date_obj - from_date_obj

    if date_difference <= timedelta(days=difference):
        return True
    else:
        return False

# Test the function
from_date = '21-05-20'
to_date = '21-06-01'
difference = 15

result = check_date_difference(from_date, to_date, difference)
print(result)
