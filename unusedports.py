#!/usr/local/bin/python
# List all the unused ports between 1-200
# Exercise guide page 25

import re

services = open('/etc/services')

# Compile regex to search for valid lines in "/etc/services"
rex = re.compile(r"""
                 ^         # The begining of the line
                 [^#]      # Not commented out
                 .*        # Any character one or more times
                 \s        # White space
                 ([0-9]+)  # Digits 0-9 one or more times (perenthesis for back reference)
                 /         # A forward slash
                 (tcp|udp) # Either "tcp" or "udp"
                 .*        # Any character one or more times
                 $         # The end of the line
                  """, re.VERBOSE)
# Loop through file and put into a dictionary
# Create an empty set
myset = set('')
# Loop through file
for line in services:
    # Apply regex from earlier to search for ports
    n = rex.search(line)
    # If you get a result
    if n:
        # Add it to the empty set as an integer
        myset.add(int(n.group(1)))
# Define the range or ports we want to search for
x = set(range(1, 201))
# Subtract found ports from ports the entire range or ports
y = (x - myset)
# Front out the unused ports
for i in y:
    print "Unused Port: ", i
# Close file
services.close()
