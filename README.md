SYSC3010 Trial Project
======================

A morse code message system using RPI and Gert Board

Implementation

We chose to use Python as the main programing language for the implementation for 
this project. We also used the following additional libraries:

- PifacedigitalIo for interacting with the PiFace board
- PyQT4 for GUI implementation

A file named “client.py” will be running on client side and “server.py” will be on server For the implementation on the server, there will be a main thread that listens for client 
connections constantly. Meanwhile there will be another thread handling client requests as needed. Generally speaking, there are two kinds of client requests: message sending and client 
ist requesting. 

The message sending package contains three components: sender’s address, receiver’s address, and the message from sender. Each of the component will be handled by 
server thread, together with several error check for exceptions like connection lost or invalid data. When the client list is requested, the server will return a list of connected clients’ IP 
address and port to the requested client. In addition, there is no user control on the server, that is, anyone can connect to the server and each of the clients will be distinguished by IP address.

As for the client, a file named client.py will be running on the Raspberry Pi. After running the file, a simple user interface written by PyQt will pop up, together with a constant running 
thread listens to the receiving messages every 0.5 second. As stated in the design part, there are two kinds of events that will be handled on the client side: send button pressed and refresh icon pressed.

In addition, we establish a communication protocol on both the client side and the server side. For client messages, the format is:

Normal Message: $<destIP>":"<destPort>$<Message>
Query list of Clients: $<"LIST">

 Thus, the normal message contains the length of the message, destination’s IP address and port, and the actual message. After sending the query “LIST” from client to server, the server will reply with the following format:
Send list of connected clients: <"LIST">$<Client1>$<Client2> . . .

The replied message contains the IP address and port of all the connected clients which will be processed and shown in the drop-down list on the user interface. Last but not least, the 
received message from one client to another will be in the format of:

<"RX">$<srcIP>":"<sourcePort>$<Message>


In addition, the pins which are connected to the relays (Pin 0 and Pin 1) were selected to 
generate the clicking sound from the relay closing as the LEDs blink. This also considers the use 
of heavy load such us strobe lights instead of LEDs.
