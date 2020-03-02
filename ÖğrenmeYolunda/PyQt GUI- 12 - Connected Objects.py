from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class twoCons(QDialog):
    def __init__(self,parent=None):
        super(twoCons,self).__init__(parent)

        grid = QGridLayout()
        slide = QSlider(Qt.Horizontal)
        slide.setRange(0,100)

        grid.addWidget(slide,0,0)

        sb = QSpinBox()
        sb.setRange(0,100)
        grid.addWidget(sb,1,0)

        sb.valueChanged.connect(slide.setValue)
        slide.valueChanged.connect(sb.setValue)

        self.setLayout(grid)
        self.setWindowTitle('Bağlı Parçacıklar')

app = QApplication([])
window = twoCons()
window.show()
app.exec_()