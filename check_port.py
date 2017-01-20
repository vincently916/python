#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = raw_input("Enter the host name or ip address: ") 
port = int(raw_input("Enter the port number: "))
result = s.connect_ex((host,port))

if result == 0:
  print 'port ' + str(port) + ' is open'
else:
  print 'port ' + str(port) + ' is closed' 
