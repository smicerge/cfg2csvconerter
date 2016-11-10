#! /usr/bin/python2.7
# Nagios_cfg2csv_converter.py
# require nagiosdefs.py
# Author = smicerge
# Hostdefinition from =
# https://assets.nagios.com/downloads/nagioscore/docs/nagioscore/3/en/objectdefinitions.html

import nagiosdefs

cfgfile = open('fin.cfg', 'r')
cfg = cfgfile.read()
cfgfile.close()

cfgsplit = cfg.splitlines()

countn = int(-1)
counte = int()

exp = open('cfg2csvnew.csv', 'w')

for lines in cfgsplit:
    countn += 1
    csvlist = [' '] * 44

    if 'define host{' in lines:
        counte = countn
        counte += 1
        # print 'convert Nr. %s' % countn
        while counte != 0:

            if counte < len(cfgsplit):
                linevalid = nagiosdefs.validatevalue(cfgsplit[counte])

                if linevalid == 'OK':

                    cfgline = cfgsplit[counte].split()
                    typ = nagiosdefs.conv_nag_hostdef(cfgline[0])

                    # noinspection PyBroadException
                    try:
                        csvlist[typ] = cfgline[1]
                        counte += 1
                    except:
                        counte += 1
                        if 'define host{' not in cfgsplit[counte]:
                            print 'OK'

                        else:
                            # print '66'
                            counte = 0

                elif linevalid == 'EMPTY':
                    counte += 1

                else:
                    # Wenn Programm hier wird counte resettet, Bedenke bei lesen des Outputs die 0
                    # print 'EXIT WHILE -> %s goto line %s from %s ' %(cfgsplit[counte], countn, counte)
                    counte = 0

            else:
                counte = 0
                print 'End of List'

        writecount = int(0)
        for data in csvlist:
            exp.write('%s;' % csvlist[writecount])
            writecount += 1

        exp.write('\n')

    del csvlist[:]

print 'converted =)'
exp.close()
