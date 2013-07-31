#!/usr/local/bin/python

import sys, re

country_file = open('country.txt')

lines = []
for x in country_file:
    lines.append(x.rstrip())
    re.sub(r'[\']', '', x )

print lines
