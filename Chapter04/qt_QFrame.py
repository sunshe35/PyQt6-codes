import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class FrameDemo(QWidget):
    def __init__(self, parent=None):
        super(FrameDemo, self).__init__(parent)
        self.resize(350,500)
        layout = QVBoxLayout()

        self.label = QLabel("1、QLabel使用QFrame效果")
        self.label.setMaximumHeight(50)
        self.label.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Raised)
        self.label.setLineWidth(2)
        layout.addWidget(self.label,stretch=0)

        self.frame = QFrame()
        label = QLabel('2、QFrame自身效果', self.frame)
        self.frame.setMinimumHeight(200)
        layout.addWidget(self.frame)

        formLayout = QFormLayout()
        self.comboBoxShape = QComboBox()
        self.comboBoxShape.addItems(['NoFrame','Box','Panel','StyledPanel','HLine','VLine','WinPanel'])
        self.comboBoxShape.setCurrentText('Box')
        self.comboBoxShape.currentIndexChanged.connect(self.updateFrame)
        formLayout.addRow('框架样式：',self.comboBoxShape)

        self.comboBoxShadow = QComboBox()
        self.comboBoxShadow.addItems(['Plain','Raised','Sunken'])
        self.comboBoxShadow.setCurrentText('Raised')
        formLayout.addRow('阴影样式：',self.comboBoxShadow)
        self.comboBoxShadow.currentIndexChanged.connect(self.updateFrame)

        spinBoxLineWidth = QSpinBox()
        spinBoxLineWidth.setMinimum(0)
        spinBoxLineWidth.setValue(5)
        spinBoxLineWidth.valueChanged.connect(lambda x:self.frame.setLineWidth(x))
        formLayout.addRow('线宽：',spinBoxLineWidth)

        spinBoxMidLineWidth = QSpinBox()
        spinBoxMidLineWidth.setMinimum(0)
        spinBoxMidLineWidth.setValue(3)
        spinBoxMidLineWidth.valueChanged.connect(lambda x:self.frame.setMidLineWidth(x))
        formLayout.addRow('中线宽：',spinBoxMidLineWidth)

        labelFrameWidth = QLabel('frameWidth:xx')
        buttonFrameWidth = QPushButton('获取frameWidth')
        formLayout.addRow(labelFrameWidth,buttonFrameWidth)
        buttonFrameWidth.clicked.connect(lambda :labelFrameWidth.setText('frameWidth:%s'%self.frame.frameWidth()))

        layout.addLayout(formLayout)

        self.updateFrame()
        self.frame.setLineWidth(spinBoxLineWidth.value())
        self.frame.setMidLineWidth(spinBoxMidLineWidth.value())

        self.setLayout(layout)
        self.setWindowTitle("QFrame 例子")

    def updateFrame(self):
        shape = getattr(QFrame.Shape,self.comboBoxShape.currentText())
        shadow = getattr(QFrame.Shadow, self.comboBoxShadow.currentText())
        self.frame.setFrameStyle(shape|shadow)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = FrameDemo()
    demo.show()
    sys.exit(app.exec())
