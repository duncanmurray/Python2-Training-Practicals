#!/usr/local/bin/python

# Import Showcard module
import Showcard

# Read in a number from stdin
number = raw_input("Pick a card (1-52):")
# Generate a filename using concatination
filename = "BMP"+number+".GIF"

# Pass filename to mpdule and display it
Showcard.display_file(filename)

