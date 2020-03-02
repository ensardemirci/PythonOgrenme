from PyQt5.QtWidgets import *


class FirstProgram(QDialog):
    def __init__(self, parent=None):
        super(FirstProgram, self).__init__(parent)
        self.punto = 3
        self.label = QLabel('<font  color = "blue" size = "+3" face = "Times New Roman" > Biçimlendirilebilir Metin </font>')

        box = QGridLayout()

        self.spinbox = QSpinBox()
        self.spinbox.setRange(0,4)
        self.spinbox.setValue(self.punto)

        box.addWidget(self.spinbox,0,2)

        self.combobox = QComboBox()
        self.combobox.addItem("Comic Sans MS")
        self.combobox.addItem('Times New Roman')
        self.combobox.addItem('Verdana')
        self.combobox.addItem('Arial')


        box.addWidget(self.combobox,1,2)

        box.addWidget(self.label, 0, 0, 2, 1)

        self.spinbox.valueChanged.connect(self.changeFP)
        self.combobox.currentIndexChanged.connect(self.changeFP)
        
        ### Klavye kısayolları ekleme kısmı
        puntoLabel = QLabel('&Yazı Boyu: ')
        puntoLabel.setBuddy(self.spinbox)
        fontLabel = QLabel('&Tipi değiştir')
        fontLabel.setBuddy(self.combobox)
        box.addWidget(puntoLabel,0,1)
        box.addWidget(fontLabel,1,1)

        self.setLayout(box)
        self.setWindowTitle('PyQt Combo & Spin Box')
        self.resize(400,200)
        self.move(550,400)
    def changeFP(self):
            self.label.setText('<font  color = "blue" size = "+{1}" face = "{0}"> Biçimlendirilebilir Metin </font>'.format(self.combobox.currentText(),self.spinbox.value()))
            print('Font: ',self.combobox.currentText())
            print('Punto: ',self.spinbox.value())

app = QApplication([])
window = FirstProgram()
window.show()
app.exec_()