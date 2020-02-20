from PyQt5.QtWidgets import *

app = QApplication([])
button = QPushButton('Click Me')
label = QLabel('<font  color = "blue" size = "+3">Hello World </font>')
def updateText():
    print('Pushed The Button')

window = QWidget()

box = QVBoxLayout()
box.addWidget(label)
box.addWidget(button)


button.clicked.connect(updateText)




window.setLayout(box)

window.show()
window.setWindowTitle('Hello World with Button')
app.exec_()