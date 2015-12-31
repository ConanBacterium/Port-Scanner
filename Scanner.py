__author__ = 'rohdehoved'

import socket

host = "No Server"

def wantedhost():
    global host
    host = raw_input("What server would you like to scan?\n")
    temp = 0
    try:
        host = socket.gethostbyname(host)
        temp = 1
    except:
        temp = 0
    if(temp == 0):
        print "Server not resolved! \n"
        wantedhost()
wantedhost()
print host + " successfully resolved."
howManyPorts = int(raw_input("How many ports would you like to scan? (number)\n"))
print "Alright, let's get to it (this might take a while)."

for port in range(1,howManyPorts):
    #print "loop" #Used when debugging/testing
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.2)
        temp = s.connect_ex((host, port))
        if temp == 0:
            print "Port " + str(port) + ": open"
    except socket.error:
        print "Couldn't connect to server"
    port = port + 1
    s.close()

print "\n\nScan done. (If no output was given, none of the ports were open)"