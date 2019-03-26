from PyQt5 import QtCore, QtGui, QtWidgets
from OtherWindow1 import Ui_Dialog
from OtherWindow2 import Ui_Dialog1
# from OtherWindow1 import Ui_OtherWindow


class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QLabel()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow2(self):
        self.window = QtWidgets.QLabel()
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Retirement Simulator")
        MainWindow.resize(354, 164)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(100, 80, 141, 21))
        self.btn_open.setObjectName("btn_open")

        
       

         
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily("Batang")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 100, 47, 13))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.btn_open_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open_2.setGeometry(QtCore.QRect(100, 120, 141, 21))
        self.btn_open_2.setObjectName("btn_open_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 40, 271, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_open_2.clicked.connect(self.openWindow2)
        self.btn_open.clicked.connect(self.openWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Retirement Simulator", "Retirement Simulator"))
        self.btn_open.setText(_translate("Retirement Simulator", "Simula tu jubilación"))
        self.label.setText(_translate("Retirement Simulator", "RETIREMENT SIMULATOR"))
        self.btn_open_2.setText(_translate("Retirement Simulator", "Estimar monto APV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

