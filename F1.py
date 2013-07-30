#!/usr/local/bin/python

laps = 45
consumption = 2.25
#Print minimum fuel consumption
FuelRequirement = laps*consumption
print FuelRequirement
# Set a safe fuel requirement
safeFuelRequirement = FuelRequirement*1.5
print safeFuelRequirement

# Fuel in the car at qualifying time
qualfuel = 5
# Qualifying lap time
qualtime = 80.45
# time increase per lap for each 10KG of fuel
qualadd = 0.35
# Calculate initial lap with full fuel
firstlap = safeFuelRequirement/10*0.35+qualtime

print firstlap
