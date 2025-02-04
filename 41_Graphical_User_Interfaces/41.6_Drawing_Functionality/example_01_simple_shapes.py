#!/usr/bin/env python

from PySide6 import QtWidgets, QtGui
import sys


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None): 
        super().__init__(parent)
        self.pen = QtGui.QPen(QtGui.QColor(0,0,0)) 
        self.pen.setWidth(3) 
        self.brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        
    def paintEvent(self, event): 
        painter = QtGui.QPainter(self) 
        painter.setPen(self.pen) 
        painter.setBrush(self.brush) 
        painter.drawRect(10, 10, 130, 130)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MyWidget()
    widget.resize(150, 150)
    widget.show()
    sys.exit(app.exec())
 
