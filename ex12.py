#!/usr/local/bin/python
import mytimer
#import mymodules.mytimer2 as mytimer

mytimer.start_timer()
lines = 0
for row in open("words"):
    lines += 1
    
mytimer.end_timer()
print "Number of lines:",lines

# Added for Exercise 11, should crash
# This will cause an error because 'start_timer()' is not called
mytimer.end_timer()

# Now handle the exception


print "We are all done"

