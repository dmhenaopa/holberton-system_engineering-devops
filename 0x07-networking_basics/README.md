## :pencil2: Networking basics 1
This folder contains some useful scripts with basic commands  to display listening ports and pings an IP address. Also, some documents with answers about OSI model, LAN, WAN, MAC address and IP address, and UDP and TCP protocols.

### Requirements:
All commands were tested on Ubuntu 14.04 LTS. Although the commands might work fine on other distributions, versions or operative systems.

### Usage:
Verify that the files have execution permissions before being used! **If not, use the following command:**

    chmod u+x name_of_file ###To make the file executable

In all cases, all files, the way to execute them is by putting a period and a slash before the command name. As follows:

    ./name_of_file ###To execute the file

### Executable files:

Here a short description of each script/document:
+ [0-OSI_model](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x07-networking_basics/0-OSI_model): The OSI model is a conceptual model that characterizes the communication functions of a telecommunication system without regard to their underlying internal structure and technology. The OSI model is organized from the lowest to the highest level.
+ [1-types_of_network](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x07-networking_basics/1-types_of_network): The type of network a computer in local is connected to is LAN. The type of network could connect an office in one building to another office in a building a few streets away is WAN and the  network do you use when you browse a webpage from your smartphone (not connected to the Wifi) is Internet.
+ [2-MAC_and_IP_address](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x07-networking_basics/2-MAC_and_IP_address): A MAC address is the unique identifier of a network interface. An IP address is to devices connected to a network what postal address is to houses.
+ [3-UDP_and_TCP](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x07-networking_basics/3-UDP_and_TCP): The TCP is a protocol that is transfering data in a slow way but surely, so the protocol ensure that you are receiving all the packages x, y, z... The UDP is a protocol that is transfering data in a fast way and might loss data along in the process. There aren't a verification or confirmation.
+ [4-TCP_and_UDP_ports](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x07-networking_basics/4-TCP_and_UDP_ports): Bash script that displays listening ports. Only shows listening sockets and shows the PID and name of the program to which each socket belongs.
+ [5-is_the_host_on_the_network](https://github.com/dmhenaopa/holberton-system_engineering-devops/blob/master/0x07-networking_basics/5-is_the_host_on_the_network): Script that pings an IP address passed as an argument. Accepts a string as an argument and ping the IP 5 times.
<!--stackedit_data:
eyJoaXN0b3J5IjpbODAxOTk3MTc0XX0=
-->