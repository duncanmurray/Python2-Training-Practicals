#!/usr/local/bin/python

# Page 41 of exercise guide
# Create a system timer
import os 
########################################################
# Insert your TIMER FUNCTIONS here
start = 0


def start_timer():
    global start
    start = os.times()
    (utime,stime) = start[:2]
    start = utime+stime
def end_timer():
    end = os.times()
    (utime,stime) = end[:2]
    end = utime+stime
    print end-start


#

start_timer()
lines = 0
for row in open("words"):
    lines += 1
    
end_timer()
print "Number of lines:",lines

