#!/usr/local/bin/python
import sys, glob, os

# Get the directory name
if sys.platform == 'win32':
    dir = os.environ['HOMEPATH']
else:
    dir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(dir,'*')
print pattern

# TODO: Use the glob.glob() function to obtain the list of filenames
for line,files in enumerate(glob.glob(pattern)):
    print line,files

# TODO: use os.path.getsize to find each file's size
for files in glob.glob(pattern):
    print "The file:", str(files), "is", os.path.getsize(files), "Bytes"

# TODO: Add a test to only display files that are not zero length
for files in glob.glob(pattern):
    if os.path.getsize(files) > 0:
        print files, "Is larger than 0 Bytes"

# TODO: Remove the leading directory name(s) from each filename before you print it - 
# using os.path.basename()

for files in glob.glob(pattern):
    print "The filename is:", os.path.basename(files)
