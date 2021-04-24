from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QFormLayout, QGraphicsView, QHBoxLayout, QLabel, QMainWindow, QVBoxLayout, QPushButton, QWidget, QGridLayout
import sys

from onedim.onedim import OneDim
from components import StartButton, TextBox, ImageViewer, Loop, ResetButton

class MainWindow(QWidget):
    def __init__(self, board, loop):
        super().__init__()

        self.board = board
        self.loop = loop
        self.initUI()

    def initUI(self):
        
        self.setGeometry(200, 200, 1000, 600)
        self.setWindowTitle("Blocks")

        outer_layout = QVBoxLayout()
        setup_layout = QHBoxLayout()

        self.start = StartButton()
        self.start.clicked.connect(self.start_stop_clicked)

        self.reset = ResetButton()
        self.reset.clicked.connect(self.reset_clicked)

        self.rule = TextBox()
        self.rule.textChanged.connect(self.board.set_ruleset)

        self.rule_label = QLabel("Rule")

        self.viewer = ImageViewer()
        self.viewer.resize(800, 600)
        self.viewer.set_model(self.board)

        self.loop.timeout.connect(self.viewer.update_view)

        setup_layout.addWidget(self.rule_label)
        setup_layout.addWidget(self.rule)
        setup_layout.addWidget(self.start)
        setup_layout.addWidget(self.reset)
       
        outer_layout.addLayout(setup_layout)
        outer_layout.addWidget(self.viewer)

        self.setLayout(outer_layout)

    def start_stop_clicked(self):
        self.loop.start_stop()

    def reset_clicked(self):
        if self.loop.is_going():
            self.loop.start_stop()
            self.start.pressed()

        self.board.reset()
        self.viewer.update_view()


def window():
    app = QApplication(sys.argv)
    board = OneDim()
    timer = Loop()
    timer.timeout.connect(board.next_gen)
    win = MainWindow(board, timer)
    
    win.show()
    sys.exit(app.exec_())