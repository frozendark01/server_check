#!/usr/bin/python
from subprocess import call
 
command = raw_input('Please enter service name : ')
 
call(["/etc/init.d/"+command, "status"])
