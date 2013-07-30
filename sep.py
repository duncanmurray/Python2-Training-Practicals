#!/usr/local/bin/python
# Page 19 of exercise quide
# 
# Import print function
from __future__ import print_function
# Set variable
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# Print a "-" for each character in the string
for x in Belgium:
    print("-", sep='', end='')
print("\n")
# Replace the "," with a ":"
elem = Belgium.split(',')
line = ':'.join(elem)
print(line)
# Print the population of Belgium and Brussels
pops = Belgium.split(',')
print("The population is: ", int(pops[1]) + int(pops[3]))
# Print a "-" for each character in the string
for x in Belgium:
    print("-", sep='', end='')
print("\n")



