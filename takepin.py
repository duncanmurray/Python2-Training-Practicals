#!/usr/local/bin/python

# Page 13 of exercise quide
# Emulate a bank machine

# Set the correct pin
correct_pin = "1234" 

# Set number of chances and counter
chances = 3
counter = 0

# While counter is less than chances keep going
while counter < chances:
# Ask for user input
    supplied_pin = raw_input("Please enter your pin: ")
# Compare supplied pin to correct one and break if correct
    if supplied_pin == correct_pin: 
        print "Very Good!!"
        break
# If pin is incorrect loop back up
    if supplied_pin != correct_pin:
        print "You have 3 chances to get it right"
        counter += 1
# Say goodbye
print "Goodbye"

