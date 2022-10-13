#!/usr/bin/python
import subprocess

checkIP = subprocess.check_output('ip addr | grep "172.31.29.74"', shell=True)
if ("inet 172.31.19.0/24" in checkIP):
	services = ['san-mount', 'mysqld', 'httpd', 'vsftpd', 'nagios', 'crond', 'postfix', 'mysql', 'apache2'] 
	for service in services:
		status = subprocess.check_output("/etc/init.d/"+service+" status", shell=True)
		if ("is stopped" in status):
			print service + "  - Stopped"
			print service + "  - Trying to start"
			service_start = subprocess.check_output("/etc/init.d/"+service+" start", shell=True)
		else:
			print service + "  - Running "
else:
	print "Ip Address not mounted cannot execute further"