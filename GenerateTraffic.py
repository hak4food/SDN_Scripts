
#!/usr/bin/python
import sys
from scapy.all import sr1,IP,ICMP
from mininet.net import Mininet
from mininet.topolib import TreeTopo
from mininet.node import Controller,RemoteController,OVSController
import threading, time

def my_ping_func():
	h1, h4  = net.hosts[0], net.hosts[3]
	print h1.cmd('ping -c1 %s' % h4.IP())

def my_ping_all_func():
	net.pingAll()

def ping_scapy(dest):
	p=sr1(IP(dst=dest)/ICMP())
	if p:
    		p.show()
		
c0 = RemoteController('c0', ip="192.168.1.54",port=6633)		
tree4 = TreeTopo(depth=3,fanout=4)
net = Mininet(topo=tree4, controller=c0 )
net.start()
h1, h4  = net.hosts[0], net.hosts[3]

print ("Red Path:")
print h1.cmd('ping -c1 %s' % h4.IP())
print ("End of Red Path")

print("Blue Path:")
print h1.cmd('ping -c1 %s' % h4.IP())
print ("End of Blue Path")


print("Blue Path Retest:")
for i in range(10):
	my_ping_func()

print ("End of Blue Path Retest")


thread1 = threading.Thread(target=my_ping_all_func)
thread1.start()
#sleep to wait for the table to fill up with pingAll
time.sleep(60)

print("Green Path:")
print h1.cmd('ping -c1 %s' % h4.IP())
print("End of Green Path:")

print("Proof of Green Path")

print h1.cmd('ping -c1 %s' % h4.IP())
print h1.cmd('ping -c1 %s' % h4.IP())
print h1.cmd('ping -c1 %s' % h4.IP())

print("End Proof of Green Path")

net.stop()

