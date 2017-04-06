# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\git\smalltools\windows_tool\hello\hey.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 320)
        Dialog.setSizeGripEnabled(True)
        self.time = QtWidgets.QLabel(Dialog)
        self.time.setGeometry(QtCore.QRect(200, 80, 80, 20))
        self.time.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.time.setObjectName("time")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 200, 100, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.time.setText(_translate("Dialog", "时间"))
        self.pushButton.setText(_translate("Dialog", "确定"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

