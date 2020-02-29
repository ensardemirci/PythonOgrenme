from PyQt5.QtWidgets import *
import random
app = QApplication([])
button1 = QPushButton('Click Me First')
button2 = QPushButton('Click Me Second')
label = QLabel('<font  color = "blue" size = "+3">Hello World </font>')

window = QWidget()

box = QHBoxLayout()
box.addWidget(label)
box.addWidget(button1)
box.addWidget(button2)


button1text = button1.text()
button2text = button2.text()
def updateText():
    label.setText('<font  color = "blue" size = "+3">{0} </font>'.format(button1text))


def updateText2():
    label.setText('<font  color = "red" size = "+3">{0}</font>'.format(button2text))

button1.clicked.connect(updateText)
button2.clicked.connect(updateText2)

window.setLayout(box)

window.show()
window.setWindowTitle('Hello World with Button')
app.exec_()