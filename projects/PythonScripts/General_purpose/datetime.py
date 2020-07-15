# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:23:15 2020



@author: U42163
"""

# Python datetime


# Example 1: Get Current Date and Time


from datetime import datetime, date, time, timedelta

datetime_object = datetime.now()

print(datetime_object)  # 2020-07-14 08:55:52.514037

# Example 2: Get Current Date


date_objetc = date.today()

print(date_objetc)  # 2020-07-14

# Example 3: Date object to represent a date


d = date(2019, 4, 13)

print(d)  # 2019-04-13

# Example 5: Get date from a timestamp


timestamp = date.fromtimestamp(1326244364)

print(f"Date = {timestamp}")  # Date = 2012-01-10

# Example 6: Print today's year, month and day
today = date.today()
print("Current year: ", today.year)  # Current year:  2020
print("Current month: ", today.month)  # Current month:  7
print("Current day: ", today.day)  # Current day:  14

# Example 7: Time object to represent time


# time(hour = 0, minute = 0, second = 0)
a = time()
print(f"a = {a}")  # a = 00:00:00

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)

# time(hour, minute and second)
c = time(hour=11, minute=34, second=56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

a = time(11, 34, 56)

print("hour =", a.hour)
print("minute =", a.minute)
print("second =", a.second)
print("microsecond =", a.microsecond)

# Example 9: Python datetime object
# datetime(year, month, day)
a = datetime(2018, 11, 28)
print(a)

# datetime(year, month, day, hour, minute, second, microsecond)
b = datetime(2017, 11, 28, 23, 55, 59, 342380)
print(b)

# Example 10: Print year, month, hour, minute and timestamp
a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

# Example 11: Difference between two dates and times


t1 = date(year=2018, month=7, day=12)
t2 = date(year=2019, month=7, day=12)
t3 = t2 - t1
print(f"t3 = {t3}")

t1 = timedelta(weeks=2, days=5, hours=1, seconds=33)
t2 = timedelta(days=4, hours=11, minutes=4, seconds=54)
t3 = t1 - t2

print("t1 =", t1)
print("t2 =", t2)
print("t3 =", t3)

t1 = timedelta(days=30)
print(datetime.now() + t1)

print(t1.total_seconds())

# Python format datetime
# Example 15: Format date using strftime()
now = datetime.now()

t = now.strftime("%d-%m-%y-%H-%M-%S")

print(t)

startDate = date.today()
startDate = date(year=2020, month=7, day=27)
endDate = startDate + timedelta(weeks=2)

print(f"startDate = {startDate}")
print(f"endDate = {endDate}")

day_count = (endDate - startDate).days + 1
print(day_count)

for i in range(0, day_count):
    temp_date = startDate + timedelta(days=i)
    print(temp_date.strftime("%m/%d/%y20 9:00 am"))