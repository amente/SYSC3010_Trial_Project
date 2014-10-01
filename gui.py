# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Wed Oct  1 11:13:37 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(440, 149)
        self.btnSend = QtGui.QPushButton(Dialog)
        self.btnSend.setGeometry(QtCore.QRect(330, 60, 98, 41))
        self.btnSend.setObjectName(_fromUtf8("btnSend"))
        self.txtMessage = QtGui.QLineEdit(Dialog)
        self.txtMessage.setGeometry(QtCore.QRect(20, 16, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txtMessage.setFont(font)
        self.txtMessage.setText(_fromUtf8(""))
        self.txtMessage.setObjectName(_fromUtf8("txtMessage"))
        self.cmbNodes = QtGui.QComboBox(Dialog)
        self.cmbNodes.setGeometry(QtCore.QRect(40, 80, 121, 31))
        self.cmbNodes.setObjectName(_fromUtf8("cmbNodes"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 60, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lblStatus = QtGui.QLabel(Dialog)
        self.lblStatus.setGeometry(QtCore.QRect(140, 130, 171, 17))
        self.lblStatus.setText(_fromUtf8(""))
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.btnRefresh = QtGui.QPushButton(Dialog)
        self.btnRefresh.setGeometry(QtCore.QRect(170, 80, 31, 31))
        self.btnRefresh.setText(_fromUtf8(""))
        self.btnRefresh.setIconSize(QtCore.QSize(50, 24))
        self.btnRefresh.setObjectName(_fromUtf8("btnRefresh"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "PI Morse Sender", None, QtGui.QApplication.UnicodeUTF8))
        self.btnSend.setText(QtGui.QApplication.translate("Dialog", "Send", None, QtGui.QApplication.UnicodeUTF8))
        self.txtMessage.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Type your message here", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Clients", None, QtGui.QApplication.UnicodeUTF8))

