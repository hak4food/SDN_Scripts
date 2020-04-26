# SDN_Scripts
SDN_Scripts


Setups to get the script working:

First, start up a mininet VM and collect the IP address.   

Secondm, Start a second VM which will host the controller.  Collect the IP address and start the controller. 
Starts up the Controller
>./bin/ryu-manager --verbose ryu/app/l2-learning-switch.py

 The command to start the ryu contoler with learning switch.  This means the controller will examine each packet and 
learn the source-port mapping. For example:  The source MAC address will be associated with a port. If the destination of the packet is already assoicated with some port, the packet will be sent to that port.  Else it will flooded on all ports of the switch. 

Now in the Mininet run this script with IP address from the controller. 

Now you can generate traffic on the SDN network. 
