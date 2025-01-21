import calendar as c

#print(c.month(2002,7))

#print(c.calendar(2002))

# List of all month names
# x = list(c.month_name)
# print(x)

# x= list(c.day_name)
# print(x)

# print(c.isleap(2002))

# print(c.isleap(1876))

#print(c.leapdays(2000, 2025))

import calendar

#First day of January 2025 (0 = Monday, 6 = Sunday)

# first_weekday, num_days = calendar.monthrange(2025, 1)
# print("First weekday:", first_weekday)  # Output: 2 (Wednesday)
# print("Number of days:", num_days)  # Output: 31

# x,y = calendar.monthrange(2025, 1)
# print(x)

# # Day of the week for January 19, 2025
# print(calendar.weekday(2025, 1, 19))  # Output: 6 (Sunday)



# # Calendar for January 2025
# month = calendar.monthcalendar(2025, 1)
# for week in month:
#     print(week)

x = calendar.monthcalendar(2025,4)
print(x)
a = x[calendar.FRIDAY]
print(a)

# Create a calendar starting with Sunday
# cal = calendar.TextCalendar(calendar.MONDAY)
# print(cal.formatmonth(2025, 1))

# # Create an HTML calendar
# html_cal = calendar.HTMLCalendar(calendar.MONDAY)
# print(html_cal.formatmonth(2025, 1))


# def find_fridays(year, month):
#     cal = calendar.monthcalendar(year, month)
#     fridays = [week[calendar.FRIDAY] for week in cal if week[calendar.FRIDAY] != 0]
#     return fridays

# print(find_fridays(2025, 1))  # Output: [3, 10, 17, 24, 31]


# def all_mondays(year):
#     mondays = []
#     for month in range(1, 13):
#         cal = calendar.monthcalendar(year, month)
#         for week in cal:
#             if week[calendar.MONDAY] != 0:
#                 mondays.append((month, week[calendar.MONDAY]))
#     return mondays

# print(all_mondays(2025))



# def fun(year):
#     for i in range(1,13):
#         first_weekday,days_in_month = calendar.monthrange(year, i)
#         cal = calendar.monthcalendar(year,i)
#         monday = [week[calendar.MONDAY] for week in cal if week[calendar.MONDAY] != 0]
#         x = list(c.month_name)
#         y = list(c.day_name)
#         if first_weekday == c.MONDAY:
#             print(f"\n{x[i]} 1 {year} is monday")
#             print(f"Your salary will credit on: {x[i]} - 1")
#         else:
#             print(f"\n{x[i]} 1 {year} is a {y[first_weekday]}. Next Monday is {x[i]} {monday[0]}")
#             print(f"Your salary will credit on this day: {x[i]} - {monday[0]}")


# y = int(input("Enter the year: "))
# fun(y)


