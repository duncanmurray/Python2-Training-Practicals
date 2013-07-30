#!/usr/local/bin/python
# Chapter 5 Exercise 3
# Apply changes to a dictionary
             
machines = {'user100': 'yogi',
            'user1'  : 'booboo',
            'user2'  : 'rupert',
            'user3'  : 'teddy',
            'user4'  : 'care',
            'user5'  : 'winnie',
            'user6'  : 'sooty',
            'user7'  : 'padders',
            'user8'  : 'polar',
            'user9'  : 'grizzly',
            'user10' : 'baloo',
            'user11' : 'bungle',
            'user12' : 'fozzie',
            'user13' : 'huggy',
            'user14' : 'barnaby',
            'user15' : 'hair',
            'user16' : 'greppy'}

# (a)	user14 no longer has a machine assigned
print "Remover user 14"
del machines['user14']
print machines
 
# (b)	The name of user16's machine is changed to 'cinnamon' 
print "Change user16's machine to 'cinnamon'"
machines['user16'] = 'cinnamon'
print machines

# (c)	user16 is leaving the company,
# and a new user, user17, will be assigned his machine
print "switch user 16 to 17"
machines['user17'] = machines['user16']
del machines['user16'] 
print machines
# (d)	user4, user5, and user6 are all leaving at exactly the same time,
# but their machine names are to be stored in a list called unallocated.
print "Unallocate user4 user5 and user6' machines"
for user in ('user4','user5','user6'):
    unallocated = machines.pop(user)
    print unallocated

# (e) user8 gets another machine called 'kodiak' in addition to the one they already have.
print "Add a new machine for user8"
machines['user8'] = 'kodiak','polar'
print machines

# (f)	Print a list of all the users, with their machines, in any order.
print "Print all the user's machines in any order"
#for user in sorted(machines.keys()):
for user in machines.keys():
    print user,machines[user]
    

# (g)	Print a list of unallocated machines, sorted alphabetically.
print "users and machines in a sorted list"
#for user in sorted(machines.keys(), key=str):
print sorted(machines, key=lambda c: int(c[len('user'):]))
 

