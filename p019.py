from math import floor

month_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
month_leap_dict = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}


def year_leap(year):
    if year % 4 != 0 or (year % 100 == 0 and not year % 400 == 0):
        return False
    else:
        return True


year_day_dict = {}

for year in range(1900, 2001):
    if year_leap(year):
        year_day_dict[year] = 366
    else:
        year_day_dict[year] = 365

number_of_days = sum(year_day_dict.values())

day_week_dict = {}
for i in range(1, number_of_days + 1):
    day_week_dict[i] = floor(i % 7)

month_days = []
for year in range(1900, 2001):
    if year_leap(year):
        month_days.extend(month_leap_dict.values())
    else:
        month_days.extend(month_dict.values())

cum_month_days = [0]
for day in month_days:
    prev = cum_month_days[-1]
    cum_month_days.append(prev + day)

cum_month_days_2 = [1 + day for day in cum_month_days]

first_day_dict = {}

for i in range(1, number_of_days + 1):
    if i in cum_month_days_2:
        first_day_dict[i] = 1
    else:
        first_day_dict[i] = 0

sundays_first = 0
for i in range(366, number_of_days + 1):
    if day_week_dict[i] == 0 and first_day_dict[i] == 1:
        sundays_first += 1

print(sundays_first)
