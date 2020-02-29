from PyQt5.QtWidgets import *
import random
app = QApplication([])
button = QPushButton('Click Me')
label = QLabel('<font  color = "blue" size = "+3">Hello World </font>')

def updateText():
    colors = ['red', 'green', 'blue', 'orange', 'yellow', 'brown', 'violet']
    color = random.choice(colors)
    print(color)
    label.setText('<font  color = {0} size = "+3">Hello World </font>'.format(color))

window = QWidget()

box = QVBoxLayout()
box.addWidget(label)
box.addWidget(button)


button.clicked.connect(updateText)




window.setLayout(box)

window.show()
window.setWindowTitle('Hello World with Button')
app.exec_()