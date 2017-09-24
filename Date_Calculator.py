"""" I am BalaVignesh. here i created a program for known exact day by using given input date.
  So please enter the Date in a format of DD/MM/YYYY . This is used to find a day from 1901 to 2999 but i am prepared this based on
  gregorian Calendar. If any change in future calendar this program not applicable from greater then still present year
   but i am sure this is well working from 1901 to 1999......:)"""

import math
from datetime import datetime  # FOR IMPORT THE DATETIME FOR EVALUATE THE DATE
days = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]
month_code = {1: 0, 2: 3, 3: 3, 4: 6, 5: 1, 6: 4, 7: 6, 8: 2, 9: 5, 10: 0, 11: 3, 12: 5}  # THIS IS A UNIQUE SET FOR EACH MONTH CODE
date = input("")
dt = datetime.strptime(date, '%d/%m/%Y')  # TAKE THE DATE AS THE FORMAT OF DD-MM-YYYY
day = dt.day % 7
month = dt.month
year = dt.year
print(dt)
if year < 1999 or year == 1999:
    year_list = [int(d) for d in str(year)]
    split_1 = [year_list[2], year_list[3]]
    merged_last_yr = int(''.join((str(x) for x in split_1)))
    remain_merge_yr = merged_last_yr % 7
    divided_year = math.floor(merged_last_yr / 4)
    remain_day_yr = divided_year % 7
    if month == 1:
        ddd = remain_merge_yr + remain_day_yr + month_code[1] + day
        target = ddd % 7
        destiny = days[target]
        print(destiny)
    if month == 2:
        ddd = remain_merge_yr + remain_day_yr + month_code[2] + day
        target = ddd % 7
        destiny = days[target]
        print(destiny)
    if month == 3:
        ddd = remain_merge_yr + remain_day_yr + month_code[3] + day
        target = ddd % 7
        destiny = days[target]
        print(destiny)
    if month == 4:
        ddd = remain_merge_yr + remain_day_yr + month_code[4] + day
        target = ddd % 7
        destiny = days[target]
        print(destiny)
    if month == 5:
        ddd = remain_merge_yr + remain_day_yr + month_code[5] + day
        target = ddd % 7
        destiny = days[target]
        print(destiny)
    if month == 6:
        ddd = remain_merge_yr + remain_day_yr + month_code[6] + day
        target = ddd % 7
        destiny = days[target]
        print(destiny)
    if month == 7:
        ddd = remain_merge_yr + remain_day_yr + month_code[7] + day
        target = ddd % 7
        destiny = days[target]
        print(destiny)
    if month == 8:
        ddd = remain_merge_yr + remain_day_yr + month_code[8] + day
        target = ddd % 7
        destiny = days[target]
        print(destiny)
    if month == 9:
        ddd = remain_merge_yr + remain_day_yr + month_code[9] + day
        target = ddd % 7
        destiny = days[target]
        print(destiny)
    if month == 10:
        ddd = remain_merge_yr + remain_day_yr + month_code[10] + day
        target = ddd % 7
        destiny = days[target]
        print(destiny)
    if month == 11:
        ddd = remain_merge_yr + remain_day_yr + month_code[11] + day
        target = ddd % 7
        destiny = days[target]
        print(destiny)
    if month == 12:
        ddd = remain_merge_yr + remain_day_yr + month_code[12] + day
        target = ddd % 7
        destiny = days[target]
        print(destiny)
elif year > 1999 or year == 2999:
    year_list = [int(d) for d in str(year)]
    split_1 = [year_list[2], year_list[3]]
    merged_last_yr = int(''.join((str(x) for x in split_1)))
    remain_merge_yr = merged_last_yr % 7
    divided_year = math.floor(merged_last_yr / 4)
    remain_day_yr = divided_year % 7
    if month == 1:
        ddd = remain_merge_yr + remain_day_yr + month_code[1] + day
        target = ddd % 7
        destiny = days[target-1]
        print(destiny)
    if month == 2:
        ddd = remain_merge_yr + remain_day_yr + month_code[2] + day
        target = ddd % 7
        destiny = days[target-1]
        print(destiny)
    if month == 3:
        ddd = remain_merge_yr + remain_day_yr + month_code[3] + day
        target = ddd % 7
        destiny = days[target-1]
        print(destiny)
    if month == 4:
        ddd = remain_merge_yr + remain_day_yr + month_code[4] + day
        target = ddd % 7
        destiny = days[target-1]
        print(destiny)
    if month == 5:
        ddd = remain_merge_yr + remain_day_yr + month_code[5] + day
        target = ddd % 7
        destiny = days[target-1]
        print(destiny)
    if month == 6:
        ddd = remain_merge_yr + remain_day_yr + month_code[6] + day
        target = ddd % 7
        destiny = days[target-1]
        print(destiny)
    if month == 7:
        ddd = remain_merge_yr + remain_day_yr + month_code[7] + day
        target = ddd % 7
        destiny = days[target-1]
        print(destiny)
    if month == 8:
        ddd = remain_merge_yr + remain_day_yr + month_code[8] + day
        target = ddd % 7
        destiny = days[target-1]
        print(destiny)
    if month == 9:
        ddd = remain_merge_yr + remain_day_yr + month_code[9] + day
        target = ddd % 7
        destiny = days[target-1]
        print(destiny)
    if month == 10:
        ddd = remain_merge_yr + remain_day_yr + month_code[10] + day
        target = ddd % 7
        destiny = days[target-1]
        print(destiny)
    if month == 11:
        ddd = remain_merge_yr + remain_day_yr + month_code[11] + day
        target = ddd % 7
        destiny = days[target-1]
        print(destiny)
    if month == 12:
        ddd = remain_merge_yr + remain_day_yr + month_code[12] + day
        target = ddd % 7
        destiny = days[target-1]
        print(destiny)