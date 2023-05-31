from datetime import datetime, timedelta

def calculate_previous_date(date, n):
    date_format = '%y-%m-%d'
    current_date = datetime.strptime(date, date_format)
    previous_date = current_date - timedelta(days=n)
    return previous_date.strftime(date_format)

# Test the function
date = '16-12-10'
n = 11

result = calculate_previous_date(date, n)
print(result)
