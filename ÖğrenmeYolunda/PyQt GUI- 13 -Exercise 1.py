from PyQt5.QtWidgets import *


class FirstProgram(QDialog):
    def __init__(self, parent=None):
        super(FirstProgram, self).__init__(parent)
        box = QGridLayout()

        waylabel = QLabel('Gideceğiniz Yol (KM): ')
        self.way = QLineEdit()
        self.way.setInputMask('0000000000')
        box.addWidget(waylabel,0,0)
        box.addWidget(self.way,0,1)

        gasprlabel = QLabel('Yakıtın Litre Fiyatı: ')
        self.gaspr = QLineEdit()
        self.gaspr.setInputMask('0.00')
        box.addWidget(gasprlabel,1,0)
        box.addWidget(self.gaspr,1,1)

        gasconslabel = QLabel('100 KM de Tüketilen Yakıt: ')
        self.gascons = QLineEdit()
        self.gascons.setInputMask('00.0')
        box.addWidget(gasconslabel,2,0)
        box.addWidget(self.gascons,2,1)

        self.total = QLabel('<font  color = "blue" size = "+2"> Sonuç </font>')
        totallabel = QLabel('Toplam Tutar: ')

        box.addWidget(totallabel,3,0)
        box.addWidget(self.total,3,1)

        self.way.textChanged.connect(self.calculate)
        self.gascons.textChanged.connect(self.calculate)
        self.gaspr.textChanged.connect(self.calculate)

        self.setLayout(box)
        self.setWindowTitle('Yakıt Ücret Hesaplayıcı')
        self.resize(300,200)
        self.move(550,400)

    def calculate(self):
        iway = 0
        igascons = 0
        igaspr = 0
        itotal = 0
        try:
            iway = int(self.way.text())
        except:
            pass

        try:
            igaspr = float(self.gaspr.text())
        except:
            pass

        try:
            igascons = float(self.gascons.text())
        except:
            pass
        if not iway:
            self.total.setText('<font  color = "red" size = "+2"> KM Giriniz  </font>')

        elif not igaspr:
            self.total.setText('<font  color = "red" size = "+2"> Litre Fiyatı Giriniz  </font>')

        elif not igascons:
            self.total.setText('<font  color = "red" size = "+2"> Tüketimi Giriniz  </font>')

        else:
            itotal = igaspr*(iway*igascons)/100

            self.total.setText('<font  color = "green" size = "+2"> {0} ₺ </font>'.format(itotal))

app = QApplication([])
window = FirstProgram()
window.show()
app.exec_()