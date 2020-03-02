from PyQt5.QtWidgets import *


class FirstProgram(QDialog):
    def __init__(self, parent=None):
        super(FirstProgram, self).__init__(parent)
        self.punto = 3
        self.label = QLabel('<font  color = "blue" size = "+3" face = "Times New Roman" > Biçimlendirilebilir Metin </font>')

        box = QGridLayout()
        bbox = QHBoxLayout()

        self.spinbox = QSpinBox()
        self.spinbox.setRange(0,4)
        self.spinbox.setValue(self.punto)

        bbox.addWidget(self.spinbox)

        self.combobox = QComboBox()
        self.combobox.addItem("Comic Sans MS")
        self.combobox.addItem('Times New Roman')
        self.combobox.addItem('Verdana')
        self.combobox.addItem('Arial')

        bbox.addWidget(self.combobox)

        self.chb1 = QCheckBox('Kalın')
        self.chb2 = QCheckBox('İtalik')
        self.chb3 = QCheckBox('Altı Çizgili')



        bbox.addWidget(self.chb1)
        bbox.addWidget(self.chb2)
        bbox.addWidget(self.chb3)

        self.chb1.stateChanged.connect(self.changeFP)
        self.chb2.stateChanged.connect(self.changeFP)
        self.chb3.stateChanged.connect(self.changeFP)


        box.addWidget(self.label, 0, 0)
        box.addLayout(bbox,1,0)

        self.spinbox.valueChanged.connect(self.changeFP)
        self.combobox.currentIndexChanged.connect(self.changeFP)

        self.setLayout(box)
        self.setWindowTitle('PyQt Combo & Spin Box')
        self.resize(600,200)
        self.move(550,400)


    def changeFP(self):
        boldf = ''; boldl= ''
        italicf = ''; italicl = ''
        undersf = '' ; undersl = ''

        if self.chb1.isChecked():
            boldf = '<b>'
            boldl ='</b>'

        elif self.chb1.isChecked() == False:
            boldf = ''
            boldl = ''
        if self.chb2.isChecked():
            italicf = '<i>'
            italicl = '</i>'
        elif self.chb2.isChecked() == False:
            italicf = ''
            italicl = ''
        if self.chb3.isChecked():
            undersf = '<u>'
            undersl = '</u>'
        elif self.chb3.isChecked() == False:
            undersf = ''
            undersl = ''

        line = '{0}{1}{2}Biçimlendirilebilir Metin{3}{4}{5}'.format(boldf,italicf,undersf,boldl,italicl,undersl)
        self.label.setText('<font  color = "blue" size = "+{1}" face = "{0}"> {2} </font>'.format(self.combobox.currentText(),self.spinbox.value(),line))
        print('Font: ',self.combobox.currentText())
        print('Punto: ',self.spinbox.value())

app = QApplication([])
window = FirstProgram()
window.show()
app.exec_()
