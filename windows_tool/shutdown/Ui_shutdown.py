# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\git\smalltools\windows_tool\shutdown\shutdown.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ShutDown(object):
    def setupUi(self, ShutDown):
        ShutDown.setObjectName("ShutDown")
        ShutDown.resize(600, 352)
        self.centralwidget = QtWidgets.QWidget(ShutDown)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(175, 30, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.label_hour = QtWidgets.QLabel(self.centralwidget)
        self.label_hour.setGeometry(QtCore.QRect(180, 100, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_hour.setFont(font)
        self.label_hour.setObjectName("label_hour")
        self.lineEdit_hour = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_hour.setGeometry(QtCore.QRect(250, 100, 120, 30))
        self.lineEdit_hour.setObjectName("lineEdit_hour")
        self.label_minute = QtWidgets.QLabel(self.centralwidget)
        self.label_minute.setGeometry(QtCore.QRect(180, 150, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_minute.setFont(font)
        self.label_minute.setObjectName("label_minute")
        self.lineEdit_minute = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_minute.setGeometry(QtCore.QRect(250, 150, 120, 30))
        self.lineEdit_minute.setObjectName("lineEdit_minute")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 220, 180, 40))
        self.pushButton.setObjectName("pushButton")
        ShutDown.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ShutDown)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 30))
        self.menubar.setObjectName("menubar")
        ShutDown.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ShutDown)
        self.statusbar.setObjectName("statusbar")
        ShutDown.setStatusBar(self.statusbar)

        self.retranslateUi(ShutDown)
        QtCore.QMetaObject.connectSlotsByName(ShutDown)

    def retranslateUi(self, ShutDown):
        _translate = QtCore.QCoreApplication.translate
        ShutDown.setWindowTitle(_translate("ShutDown", "ShutDown"))
        self.label_title.setText(_translate("ShutDown", "请输入关机的时间"))
        self.label_hour.setText(_translate("ShutDown", "小时："))
        self.label_minute.setText(_translate("ShutDown", "分钟："))
        self.pushButton.setText(_translate("ShutDown", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ShutDown = QtWidgets.QMainWindow()
    ui = Ui_ShutDown()
    ui.setupUi(ShutDown)
    ShutDown.show()
    sys.exit(app.exec_())

