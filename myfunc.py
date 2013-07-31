#!/usr/local/bin/python

# Create my first function
# Page 41 of exercise guide

## Define a function and set 'alist' to 'None' as default
# Uncommenting the below will keep appending to the list
#def myfunc(value, alist=[]):
def myfunc(value, alist=None):
    # This will check to see if it is set to none and reset the list if it is
    if alist == None:
        alist = []
    # Append the value to the list
    alist.append(value)
    return alist

# Rund the function a number of times
print myfunc(1)
print myfunc(1)
