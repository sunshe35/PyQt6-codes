# -*- coding: utf-8 -*-
"""
    【简介】
    绘图中QPen 的例子 ,使用不同样式的条线绘制
    
"""

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class QPenDemo(QWidget):
    def __init__(self):
        super().__init__()
        layout = QFormLayout()

        # width
        self.spinBox = QSpinBox(self)
        self.spinBox.setRange(0, 20)
        self.spinBox.setSpecialValueText("0 (cosmetic pen)")
        layout.addRow("Pen &Width:",self.spinBox)

        # style
        self.comboBoxStyle = QComboBox()
        self.comboBoxStyle.addItem("Solid", Qt.PenStyle.SolidLine)
        self.comboBoxStyle.addItem("Dash", Qt.PenStyle.DashLine)
        self.comboBoxStyle.addItem("Dot", Qt.PenStyle.DotLine)
        self.comboBoxStyle.addItem("Dash Dot", Qt.PenStyle.DashDotLine)
        self.comboBoxStyle.addItem("Dash Dot Dot", Qt.PenStyle.DashDotDotLine)
        self.comboBoxStyle.addItem("None", Qt.PenStyle.NoPen)
        layout.addRow("&Pen Style:", self.comboBoxStyle)

        # cap
        self.comboBoxCap = QComboBox()
        self.comboBoxCap.addItem("Flat", Qt.PenCapStyle.FlatCap)
        self.comboBoxCap.addItem("Square", Qt.PenCapStyle.SquareCap)
        self.comboBoxCap.addItem("Round", Qt.PenCapStyle.RoundCap)
        layout.addRow("Pen &Cap:",self.comboBoxCap)

        # join
        self.comboBoxJoin = QComboBox()
        self.comboBoxJoin.addItem("Miter", Qt.PenJoinStyle.MiterJoin)
        self.comboBoxJoin.addItem("Bevel", Qt.PenJoinStyle.BevelJoin)
        self.comboBoxJoin.addItem("Round", Qt.PenJoinStyle.RoundJoin)
        layout.addRow("Pen &Join:",self.comboBoxJoin)

        # signal and slot
        self.spinBox.valueChanged.connect(self.pen_changed)
        self.comboBoxStyle.activated.connect(self.pen_changed)
        self.comboBoxCap.activated.connect(self.pen_changed)
        self.comboBoxJoin.activated.connect(self.pen_changed)

        self.setLayout(layout)
        self.pen = QPen()
        self.setGeometry(300, 300, 280, 370)
        self.setWindowTitle('QPen案例')

    def paintEvent(self, e):
        rect = QRect(50, 140, 180, 160)
        painter = QPainter(self)
        painter.setPen(self.pen)
        painter.drawRect(rect)


    def pen_changed(self):
        width = self.spinBox.value()
        style = Qt.PenStyle(self.comboBoxStyle.currentData())
        cap = Qt.PenCapStyle(self.comboBoxCap.currentData())
        join = Qt.PenJoinStyle(self.comboBoxJoin.currentData())
        self.pen = QPen(Qt.GlobalColor.blue, width, style, cap, join)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = QPenDemo()
    demo.show()
    sys.exit(app.exec())
