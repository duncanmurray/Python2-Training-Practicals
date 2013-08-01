#!/usr/local/bin/python

import sys, re

country_file = open('country.txt')

lines = []
for x in country_file:
    re.sub(r'[\']', '', x )    
    re.sub(r'^', '\'', x )
    lines.append(x.rstrip())

print lines
