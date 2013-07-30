#!/usr/local/bin/python

# Page 15 of exercise quide
# Deterine if year is a leap year
# Ask for a year
year = int(input ('Please enter a year: '))

# If the year % by 4 is 0 and not divisable by one its num a leap year unless it's divisable by 400
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print "It's a leap year"      
else:
    print "Not a leap year" 
