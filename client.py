#!/usr/bin/python

from PyQt4 import QtCore, QtGui
from gui import Ui_Dialog
import sys, socket, threading
from time import sleep
from morse import send

TCP_PORT = 9009
BUFFER_SIZE = 64

if len(sys.argv) < 2:
    sys.argv.append('127.0.0.1')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((sys.argv[1], TCP_PORT))

socketLock  = False;

class RecieveThread(threading.Thread):

    def __init__(self,socket,app):
        threading.Thread.__init__(self)
        self.socket = socket
        self.app = app

    def run(self):
        global socketLock
        while(1):
            if not socketLock:
                socketLock = True
                self.socket.settimeout(0.5)
                try:
                    data = self.socket.recv(BUFFER_SIZE)
                except socket.timeout:
                    print "Timeout"
                    socketLock = False
                    sleep(0.5)
                    continue
            
                recvmsg = data
                if(str(recvmsg[0:2]).lstrip("['").rstrip("']") == 'RX'):                
                    print 'RX', recvmsg
                    continue
              
class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.btnSend.clicked.connect(self.sendClicked)
        self.ui.btnRefresh.clicked.connect(self.refreshClients)

        self.ui.btnRefresh.setIcon(QtGui.QIcon(QtGui.QPixmap('refresh.png')))

        self.ui.lblStatus.setVisible(False)

    def sendClicked(self):
        msg = self.ui.txtMessage.text()
        client = self.ui.cmbNodes.currentText()
        print 'client', client
        print self.ui.cmbNodes.currentText()
        msg = str(client).lstrip("'").rstrip("'")+"$"+str(msg)
        print msg

        s.send(msg)         
             

    def refreshClients(self):

        global socketLock
         
        while(socketLock):
            print socketLock
            sleep(0.5)
            a=1
        socketLock = True 
        s.send("LIST")
        data = s.recv(BUFFER_SIZE)
        socketLock = False
        
        print data[0:4].lstrip("['").rstrip("']")
        if(data[0:4].lstrip("['").rstrip("']") == "LIST"): 
            self.ui.cmbNodes.clear()
            for i in data.split('$')[1:]:
                self.ui.cmbNodes.addItem(i)
        

if __name__ == "__main__":
    app =  QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    recieveThread = RecieveThread(s,myapp)
    recieveThread.start()
    myapp.show()
    sys.exit(app.exec_())
