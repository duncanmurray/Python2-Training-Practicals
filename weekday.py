#!/usr/local/bin/python
# Python 2 version

# Code for reading in the date */
date = raw_input("Please enter date (DD/MM/YYYY): ")
d,m,y = date.split('/')
d = int(d)
m = int(m)
y = int(y)

"""
  Add Your Code Here: to adjust the values of
  d, m and y under certain circumstances

             d contains the day
             m contains the month
             y contains the year
"""

# Id month is 1 or 2
if m == 1 or m == 2:
# Add 12 to the month
    m += 12
# If it's a leap year 
    if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
# Subtract 2 from the day
        d -= 2
# Else if it's not a leap year subtract 1 from day
    else:
        d -= 1

z = 1 + d + (m * 2) + (3 * (m + 1) // 5) + y + y//4 - y//100 + y//400

z %= 7

days = ["Sun","Mon","Tues","Wednes","Thurs","Fri","Satur"]

print days[z]+'day' 

