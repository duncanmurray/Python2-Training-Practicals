#!/usr/local/bin/python

# Take input from user
uservar = raw_input("Please enter an integer:")
# Test if the input is an integer
if uservar.isdigit():
# print the sequence of number form the given number to 1 or 0 in spets of 2
    for uservar in xrange(int(uservar),-1,-2):
        print uservar
