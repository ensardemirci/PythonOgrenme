from PyQt5.QtWidgets import *


class FirstProgram(QDialog):
    def __init__(self, parent=None):
        super(FirstProgram, self).__init__(parent)
        self.punto = 3
        self.label = QLabel('<font  color = "blue" size = "+3"> Biçimlendirilebilir Metin </font>')
        button1 = QPushButton('Küçültme Düğmesi')
        button2 = QPushButton('Büyültme Düğmesi')

        box = QGridLayout()
        box.addWidget(self.label, 0, 0, 2, 1)
        box.addWidget(button1, 0, 1, 1, 1)
        box.addWidget(button2, 1, 1, 1, 1)
        button1.clicked.connect(self.smallerText)
        button2.clicked.connect(self.biggerText)
        self.setLayout(box)
        self.setWindowTitle('PyQt Sınıfları')
        self.resize(600,200)
        self.move(550,400)
    def biggerText(self):
        if self.punto <= 3:
            self.punto = self.punto + 1
            self.label.setText('<font  color = "blue" size = "+{0}"> Biçimlendirilebilir Metin </font>'.format(self.punto))
            print(self.punto)
    def smallerText(self):
        if self.punto >= 1:
            self.punto = self.punto - 1
            self.label.setText('<font  color = "blue" size = "+{0}"> Biçimlendirilebilir Metin </font>'.format(self.punto))
            print(self.punto)

app = QApplication([])
window = FirstProgram()
window.show()
app.exec_()