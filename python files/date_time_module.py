# Classes in datetime Module
# datetime.date: Represents a date (year, month, day).
# datetime.time: Represents a time (hour, minute, second, microsecond).
# datetime.datetime: Combines date and time into a single object.
# datetime.timedelta: Represents a duration (difference between two dates or times).
# datetime.tzinfo: Base class for dealing with time zones.

import datetime 
# x = d.date.today()
# print(x)

# x = '2024/6/4'.replace('/',',')
# z =int(x)
# print(d.date(x))

# import datetime as d

# Original string
# x = '2024/6/4'.replace('/',',')
# print(x)

# print(d.date(2024,8,7))

# year, month, day = map(int, x.split('/'))
# print(day)

#date_obj = d.date(year, month, day)

#print(date_obj)


# print(y.year)
# print(x.month)
# print(x.day)

#time
# x = d.time(14, 30, 15)
# print(x)

#datetime
# x = d.datetime.now()
# print(x)
# y = d.datetime(2020,6,8,22,30,9)
# print(y)

# n = d.datetime.now()

# # Format datetime as a string
# formated_date = n.strftime("%d-%m-%Y %H:%M:%S")
# print(formated_date)

# # Common format codes:
# # %Y - Year (4 digits), %m - Month (2 digits), %d - Day (2 digits)
# # %H - Hour (24-hour), %M - Minute, %S - Second

#time delta

# delta = d.timedelta(7)
# today = '2025-01-28'

# future = today + delta
# print("future",future)

# past = today - delta
# print("Past",past)

# import datetime

# date1 = datetime.date(2025, 1, 19)
# date2 = datetime.date(2025, 1, 25)

# print(date1 < date2)  
# print(date1 == date2)  

# Calculate the next Monday
# today = d.date.today()
# days_until_monday = (7 - today.weekday()) % 7
# next_monday = today + d.timedelta(days=days_until_monday)
# print("Next Monday:", next_monday)


# import datetime
# start_date = datetime.date(2025, 1, 1)
# end_date = datetime.date(2025, 1, 10)
# delta = datetime.timedelta(days=1)

# current_date = start_date
# while current_date <= end_date:
#     print(current_date)
#     current_date += delta

# x = d.datetime.now()

# y = x.strftime("%B")
# print(y)

# from datetime 
import datetime

# Example string date
date_string = "01-21-25"

# Convert string to date object
date_obj = datetime.datetime.strptime(date_string, "%m-%d-%y")

# Print the result
print(date_obj)


# from datetime import datetime

# # Example string date
# date_string = "01-21-2025"

# # Convert string to date object (adjust year format to %Y for four-digit year)
# date_obj = datetime.strptime(date_string, "%m-%d-%Y")

# # Print the result
# print(date_obj)
