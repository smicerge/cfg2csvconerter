#! /usr/bin/python2.7
# create_switcher.py
# author smicerge

file = open('hostdef.cfg', 'r')
cfgdefs = file.read()
file.close()

cfglines = cfgdefs.splitlines()

print 'def add_to_list(name):'
print '     switcher = {'

count = int(0)

for line in cfglines:
    if 'define host' not in line:
        if '}' not in line:
            cfgdef = line.split()
            print "         '%s': %s," %(cfgdef[0], count)
            count +=1


print '         }'
print '     return int(switcher.get(name, 10))'
