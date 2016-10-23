#!/usr/bin/python
# -*- coding:UTF-8 -*-
import os
import sys
import time
import random

lockfile='/var/lock/LCK..ttyS1'
gnokii='/usr/local/bin/gnokii'


if len(sys.argv) !=3:
	print "Usages:" + sys.argv[0] + " phone smstext";
	sys.exit(0);
print "Waiting for the MODEM not busy......";
while 1 :
	rand=random.uniform(0,3)
	time.sleep(rand)
	if os.path.exists(lockfile):
		if os.popen('ps -eo comm | grep -e ^gnokii$').read().count('gnokii') == 0:
			os.system('rm -f ' + lockfile)
	else:
		if os.system('/usr/bin/printf "%b" "' + sys.argv[2] + '" | ' + gnokii + ' --sendsms ' + sys.argv[1]) == 0:
			print "Message sent successfully!";
		else:
			print "Message sent faild!";
		sys.exit(0)