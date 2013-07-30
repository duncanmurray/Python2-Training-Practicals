#!/usr/local/bin/python

from math import pi, tan, cos

# aceleration due to gravity
g = 9.81
# The initial velocity
vo = 44
# elevation in degrees
deg = 80
# convert degrees to radians
theta = deg * pi/180
# Horizontal distance travelled
x = 0.5
# Height of barrel
y0 = 1

# Find the height of the projectile
y = y0 + x*tan(theta) - (g*x**2)/(2*((vo*cos(theta))**2))
z = y0 + x*tan(theta) - (g*pow(x,2))/(2*pow(vo*cos(theta),2))

# Print them out
print y
print z
