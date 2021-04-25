from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QSlider, QVBoxLayout, QWidget
import sys

from onedim.onedim import OneDim
from components import StartButton, TextBox, ImageViewer, Loop, ResetButton

'''
Set up the main window and link all elements to events
'''
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

        self.rule_label = QLabel("Rule:")

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(10)
        self.slider.setMaximum(1000)
        self.slider.setValue(910)
        self.slider.setTickInterval(10)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.valueChanged.connect(self.slider_changed)

        self.slider_label = QLabel("Speed:")

        self.viewer = ImageViewer()
        self.viewer.set_model(self.board)

        self.loop.timeout.connect(self.viewer.update_view)

        setup_layout.addWidget(self.rule_label)
        setup_layout.addWidget(self.rule)
        setup_layout.addStretch()
        setup_layout.addWidget(self.slider_label)
        setup_layout.addWidget(self.slider)
        setup_layout.addStretch()
        setup_layout.addWidget(self.start)
        setup_layout.addWidget(self.reset)

       
        outer_layout.addLayout(setup_layout)
        outer_layout.addWidget(self.viewer)
        self.viewer.update_view()
        self.setLayout(outer_layout)

    def start_stop_clicked(self):
        self.loop.start_stop()

    def reset_clicked(self):
        if self.loop.is_going():
            self.loop.start_stop()
            self.start.pressed()

        self.board.reset()
        self.viewer.update_view()

    def slider_changed(self, value):
        self.loop.currentTimer = 1010 - value

'''
Callable for main to instatiate game and launch window
'''
def window():
    app = QApplication(sys.argv)
    board = OneDim()
    timer = Loop()
    timer.timeout.connect(board.next_gen)
    win = MainWindow(board, timer)
    
    win.show()
    sys.exit(app.exec_())