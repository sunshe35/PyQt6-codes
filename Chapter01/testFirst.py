import sys
from PyQt6 import QtWidgets

'''
    【简介】
	第一个PyQt例子
   
    
'''

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("hello, PyQt6")
widget.show()
sys.exit(app.exec())
