from PyQt5.QtWidgets import *


class FirstProgram(QWidget):
    def __init__(self, parent=None):
        super(FirstProgram, self).__init__(parent)
        self.label = QLabel('<font  color = "blue" size = "+3">Hello World </font>')
        button = QPushButton('Click Me')
        box = QVBoxLayout()
        box.addWidget(self.label)
        box.addWidget(button)
        button.clicked.connect(self.updateText)
        self.setLayout(box)
        self.setWindowTitle('PyQt Sınıfları')
        self.resize(300,100)
        self.move(550,400)
    def updateText(self):
        self.label.setText('<font  color = "blue" size = "+3"> Clicked </font>')


app = QApplication([])
window = FirstProgram()
window.show()
app.exec_()