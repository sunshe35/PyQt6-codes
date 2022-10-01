# -*- coding: utf-8 -*-


import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt


class FormLayoutDemo(QWidget):
    def __init__(self, parent=None):
        super(FormLayoutDemo, self).__init__(parent)
        self.setWindowTitle("QFormLayout布局管理例子")
        self.resize(400, 100)

        formLayout = QFormLayout()

        nameLineEdit = QLineEdit()
        emailLineEdit = QLineEdit()
        ageSpinBox = QSpinBox()
        formLayout.addRow("&Name:", nameLineEdit)
        formLayout.addRow("&Email:", emailLineEdit)
        formLayout.addRow("&Age:", ageSpinBox)

        # 模拟macStyle表单布局外观，但使用左对齐的标签
        formLayout.setRowWrapPolicy(QFormLayout.RowWrapPolicy.DontWrapRows)
        formLayout.setFieldGrowthPolicy(QFormLayout.FieldGrowthPolicy.FieldsStayAtSizeHint)
        formLayout.setFormAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        formLayout.setLabelAlignment(Qt.AlignmentFlag.AlignLeft)

        formLayout.addItem(QSpacerItem(30,30))
        formLayout.addRow(QPushButton('确认'),QPushButton('取消'))

        self.setLayout(formLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = FormLayoutDemo()
    form.show()
    sys.exit(app.exec())
