# Maker Faire Prague 2022

This is the code produced during the Maker Faire exposition of an old project of mine called ARACHNE ([for more info](https://www.youtube.com/channel/UCInXuTPAg9Gda9SzNKTq7eQ))

It was made in order to move 3 of the 6 legs remotely with some sliders. TCP sockets are used to communicate between two computers, one for the sliders and one connected to the robot

- **tcpServer** is the server, basically a socket to serial echo
- **tcpClient** is the slider application

Keep in mind that this code was written in just a couple of hours before the fair so it's not my proudest work :)
