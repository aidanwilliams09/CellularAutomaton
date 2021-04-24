from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage, QIntValidator, QPixmap, qRgb
from PyQt5.QtWidgets import QLabel, QPushButton, QLineEdit, QSizePolicy
import numpy as np
import qimage2ndarray

class StartButton(QPushButton):
    
    def __init__(self):
        super(StartButton, self).__init__()
        self.text = ['Start', 'Stop']
        self.make_button()

    def make_button(self):
        self.setFixedWidth(100)
        self.setText(self.text[0])
        self.stop = False
        self.setStyleSheet('background-color:orange; border: 2px solid black')
        self.clicked.connect(self.pressed)
        
    def pressed(self):
        if self.stop:
            self.setText(self.text[0])
        else:
            self.setText(self.text[1])

        self.stop = not self.stop

class ResetButton(QPushButton):

    def __init__(self):
        super().__init__()
        self.make_button()

    def make_button(self):
        self.setFixedWidth(100)
        self.setText('Reset')
        self.setStyleSheet('background-color:orange; border: 2px solid black')
        
class TextBox(QLineEdit):
    
    def __init__(self):
        super(TextBox, self).__init__()
        self.make_textbox()

    def make_textbox(self):
        self.setFixedWidth(100)
        self.setAlignment(Qt.AlignCenter)
        self.setValidator(QIntValidator())
        self.setMaxLength(3)


class ImageViewer(QLabel):

    def __init__(self):
        super().__init__()

        self.setAlignment(Qt.AlignCenter)
        self.setScaledContents(True)
        self.V_margin = 0
        self.H_margin = 0
        self.h = 0
        self.w = 0

    def set_model(self, od):
        self.od = od
        self.update_view()

    def update_view(self):

        grid = self.od.get_map()
        self.h = grid.shape[0]
        self.w = grid.shape[1]

        qim = self.createQImage(grid)
        qpix = QPixmap.fromImage(qim)
        self.setPixmap(qpix.scaled(self.size(), Qt.KeepAspectRatio, Qt.FastTransformation))

        self.V_margin = (self.size().height() - self.pixmap().size().height()) / 2
        self.H_margin = (self.size().width() - self.pixmap().size().width()) / 2

    def createQImage(self, im):
        if im is None:
            return QImage()

        qim = qimage2ndarray.array2qimage(im)
        return qim


class Loop(QTimer):

    def __init__(self):
        super().__init__()

        self.going = False

        self.currentTimer = 50
        self.timeout.connect(self.loop)
        self.setSingleShot(True)

    def loop(self):
        if self.going and self.isSingleShot() and self.currentTimer > 0:
            self.start(self.currentTimer)

    def start_stop(self):
        self.stop()
        self.going = not self.going
        if self.going:
            self.start(self.currentTimer)

    def is_going(self):
        return self.going

