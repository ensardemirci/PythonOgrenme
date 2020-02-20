from PyQt5.QtWidgets import *


app = QApplication([])
window = QWidget()
label = QLabel('<font  color = "blue" size = "+3">Hello World </font>')
button = QPushButton('Click Me')
box = QVBoxLayout()
box.addWidget(label)
box.addWidget(button)
window.setLayout(box)
window.show()
window.setWindowTitle('Hello World with Button')
app.exec_()