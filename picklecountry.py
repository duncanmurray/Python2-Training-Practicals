#!/usr/local/bin/python
# Add the contents of a file to a dictionary and pickle it to a file 
# Exercise book page 36
import re, pickle
# Open our country file
countryfile = open('country.txt')
mydict = {}
# Loop through country file
for n in countryfile:
    # Spilit each line on a "," and remove the trailing new line
    x = re.split(',', n[:-1])
    # Add each line to a dictionary
    #mydict = {x[0]:x[1:]}
    mydict[x[0]] = x[1:]
    #print mydict
# Print out the dictionary
print mydict

# Open a pickle file as binary
picklefile = open('countrys.p', 'wb')
# Write the 'mydict' dictionary to a picklefile
pickle.dump(mydict, picklefile)
# Close the pickle file
picklefile.close
# Close the country file
countryfile.close()
