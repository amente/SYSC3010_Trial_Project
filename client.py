from PyQt4 import QtCore, QtGui
from gui import Ui_Dialog
import sys, socket, threading


TCP_IP = '127.0.0.1'
TCP_PORT = 9009
BUFFER_SIZE = 64

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

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
        print self.ui.cmbNodes.currentText()
        msg = str(client).lstrip("'").rstrip("'")+"$"+msg
	s.send(str(len(msg))+"$"+msg)

    def refreshClients(self):
	s.send("4$LIST")
        data = s.recv(BUFFER_SIZE)
        if(data[0:4] == "4$LIST"): 
            self.ui.cmbNodes.clear()
            for i in data.split('$')[1:]:
		self.ui.cmbNodes.addItem(i)

if __name__ == "__main__":
    app =  QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
