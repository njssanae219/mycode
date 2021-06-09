#!/usr/bin/env python3
ipchk = "192.168.0.1"

# a string tests as True
if ipchk:
   print("Looks like the IP address was set: " + ipchk)

ipchk = input("Apply an IP address: ") # this line now prompts the user for input

# a provided string will test true
if ipchk:
   print("Looks like the IP address was set: " + ipchk) # indented under if

