from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class BKICalc(QDialog):
    def __init__(self, parent=None):
        super(BKICalc, self).__init__(parent)
        box = QGridLayout()

        kglabel = QLabel('Kilonuz (KG): ')
        self.kg = QLineEdit()
        self.kg.setInputMask('0000')
        box.addWidget(kglabel,0,0)
        box.addWidget(self.kg, 0, 1)

        lenlabel = QLabel('Boyunuz (M): ')
        self.len = QLineEdit()
        self.len.setInputMask('0.00')
        box.addWidget(lenlabel,1,0)
        box.addWidget(self.len, 1, 1)

        self.result = QLabel('<font  color = "blue" size = "+2"> Sonuç </font>')
        resullabel = QLabel('Sonuç: ')

        box.addWidget(resullabel,3,0)
        box.addWidget(self.result, 3, 1)

        self.kg.textChanged.connect(self.calculate)
        self.len.textChanged.connect(self.calculate)

        self.setLayout(box)
        self.setWindowTitle('Kütle Yağ Endeks Hesaplayıcı')
        self.resize(300,200)
        self.move(550,400)

    def calculate(self):
        ikg = 0
        ilen = 0
        iresult = 0
        try:
            ikg = int(self.kg.text())
        except:
            pass

        try:
            ilen = float(self.len.text())
        except:
            pass

        if not ikg:
            self.result.setText('<font  color = "red" size = "+2"> KG Giriniz  </font>')

        elif not ilen:
            self.result.setText('<font  color = "red" size = "+2"> Boy Giriniz  </font>')

        else:
            iresult = ikg/(ilen**2)

            if iresult < 18.5:
                self.result.setText('<font  color = "green" size = "+2"> Zayıf </font>')
                print(iresult)
            elif 18.5 < iresult < 24.9:
                self.result.setText('<font  color = "green" size = "+2"> Normal </font>')
                print(iresult)
            elif 25 < iresult < 29.9:
                self.result.setText('<font  color = "green" size = "+2"> Fazla Kilolu </font>')
                print(iresult)
            elif 30 < iresult < 39.9:
                self.result.setText('<font  color = "green" size = "+2"> Şişman </font>')
                print(iresult)
            elif iresult > 40:
                self.result.setText('<font  color = "green" size = "+2"> Obez </font>')
                print(iresult)




app = QApplication([])
window = BKICalc()
window.show()
app.exec_()