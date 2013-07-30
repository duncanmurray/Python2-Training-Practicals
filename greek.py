#!/usr/local/bin/python
# Python 2 version
# Page 19 of the exercise guide

greek = ['Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta',
         'Iota','Kappa','Lambda','Mu','Nu','Xi','Omicron','Pi','Rho',
         'Sigma final','Sigma','Tau','Upsilon','Phi','Chi','Psi','Omega']

#Format required:
#    The hex value of the character
#    The character name (cname), left justified, maximum 12 characters
#    A colon separator
#    The lowercase Greek character
#    The uppercase Greek character

pos = 0x03B1         
for cname in greek:
    try:
        char = unichr(pos)
        pos += 1 

        hexpos = "%x" % (pos)
#        ucname = cname.upper()
        lchar = char.lower()
        uchar = char.upper()

# My first way of doing it 
        print "%s %-12s %s %s" % (hexpos,cname,lchar,uchar)# TODO: replace this statement
# A bit cleaner way
        print "%x %-12s %s %s" % (pos,cname,char.lower(),char.upper())

    except UnicodeEncodeError as err:
        print  cname, 'unknown'
