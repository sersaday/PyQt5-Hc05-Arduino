# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pyqt5_Hc05.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import bluetooth

print ("Hc05 aranıyor.......")
print ("")

nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True,
                                            flush_cache=True, lookup_class=False)
print("{} Aygıt bulundu. ".format(len(nearby_devices)))

for addr, name in nearby_devices:
    try:
        print("   {} - {}".format(addr, name))
    except UnicodeEncodeError:
        print("   {} - {}".format(addr, name.encode("utf-8", "replace")))

  
    
class Ui_Form(object):

    port = 1
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((addr,port))

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(208, 124)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 0, 191, 71))
        self.label.setObjectName("label")
        self.LedYak = QtWidgets.QPushButton(Form)
        self.LedYak.setGeometry(QtCore.QRect(10, 60, 91, 25))
        self.LedYak.setObjectName("LedYak")
        self.LedYak.clicked.connect(self.Yak)

        self.LedSon = QtWidgets.QPushButton(Form)
        self.LedSon.setGeometry(QtCore.QRect(110, 60, 89, 25))
        self.LedSon.setObjectName("LedSon")
        self.LedSon.clicked.connect(self.Son)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 151, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "PyQt5 Hc05"))
        self.label.setText(_translate("Form", "<html><head/><body><p><span style=\" font-weight:600; color:#204a87;\">PyQt5 HC05 haberleşmesi</span></p></body></html>"))
        self.LedYak.setText(_translate("Form", "Led Yak"))
        self.LedSon.setText(_translate("Form", "Led Söndür"))
        self.label_2.setText(_translate("Form", "Author: Serhat Saday"))


    
     
        
    def Yak(self,LedYak):
    	#Send 'H' which the Arduino
    	#detects as turning the light on
        data = "A"
        self.sock.send(data)

    def Son(self,LedSon):
    	#Send 'L' to turn off the light
    	#attached to the Arduino
        data = "B"
        self.sock.send(data)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
