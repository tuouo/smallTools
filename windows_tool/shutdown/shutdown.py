# -*- coding: utf-8 -*-

"""
Module implementing ShutDown.
"""
import os
import time
from PyQt5.QtCore import pyqtSlot, QCoreApplication
from PyQt5.QtWidgets import QMainWindow
from Ui_shutdown import Ui_ShutDown


class ShutDown(QMainWindow, Ui_ShutDown):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ShutDown, self).__init__(parent)
        self.setupUi(self)
        self.hour, self.minute = False, False
        self.work = r'schtasks /create /tn "关机" /tr "shutdown /s" /sc once /st {}:{}'
        self.error, self.info, self.end = "请输入正确的数字",  "关机时间为24小时制", "将设置{}:{}关机"
    
    @pyqtSlot(str)
    def on_lineEdit_hour_textEdited(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        self.hour = self.check_set_time(self.lineEdit_hour.text(), 0, 23)

        if not (self.hour is False or self.minute is False):
            self.label_title.setText(self.end.format(self.hour, self.minute))
    
    @pyqtSlot(str)
    def on_lineEdit_minute_textEdited(self, p0):
        """
        Slot documentation goes here.
        
        @param p0 DESCRIPTION
        @type str
        """
        self.minute = self.check_set_time(self.lineEdit_minute.text(), 0, 59)
        if not (self.hour is False or self.minute is False):
            self.label_title.setText(self.end.format(self.hour, self.minute))
    
    @pyqtSlot()
    def on_pushButton_clicked(self):
        """
        Slot documentation goes here.
        """
        if not (self.hour is False or self.minute is False):
            os.popen(self.work.format(self.hour, self.minute))
            time.sleep(3)
            QCoreApplication.quit()
        else:
            self.label_title.setText(self.error)

    def check_set_time(self, item, start, end):
        try:
            item = int(item)
        except ValueError:
            self.label_title.setText(self.error)
            item = False
        else:
            if item < start or item > end:
                self.label_title.setText(self.error)
                item = False
            else:
                self.label_title.setText(self.info)
        return item


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = ShutDown()
    dlg.show()
    sys.exit(app.exec_())
