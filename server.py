#!/usr/bin/env python

import socket, threading


TCP_IP = '127.0.0.1'
TCP_PORT = 9009
BUFFER_SIZE = 64 

connectedClients = {};

# Thread to handle client connections
class ClientThread(threading.Thread):

    def __init__(self, ip, port, socket):
        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.socket = socket
        print "[+] New Client thread started for "+ip+":"+str(port)

    def run(self):       	
	while 1:
            data = self.socket.recv(BUFFER_SIZE)
             
	    if(data[0:4] == "4$LIST"):
                msg = "LIST"+"$"+str(connectedClients.keys()).lstrip('[').rstrip(']').replace(', ','$');
                self.socket.send(str(len(msg))+"$"+msg)
                continue
            elif(len(data.split('$'))!=2):
		if data == '':
                    break                    
		print "[+] Invalid data recieved: "+ data
                continue
            print data
	    msglen,dest, msg = data.split('$');
            print "[+] Message received from "+str(self.ip)+":"+str(self.port) + " To " + dest
	    if dest in connectedClients:
                msg = "RX$"+str(self.ip)+':'+str(self.port)+"$"+msg
	        connectedClients[dest].send(str(len(msg))+"$"+msg);  
                print "[+] Message proxied to "+ dest 
            else:
                print connectedClients
                print len(dest)
                print "[ERROR] "+dest+ " is not currently connected"           		
        self.socket.close()
        "[-] Connection with "+ip+":"+str(port) + " is terminated." 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

#Main server thread listens for client connections continously
print "[+] RPI Morse Code Server Started."
print "Waiting for connections ... "
while 1:
    (clientsock, (ip, port)) = s.accept()   
    newClient= ClientThread(ip, port, clientsock)
    newClient.start()
    connectedClients[str(ip)+':'+str(port)]  = clientsock
	
    
