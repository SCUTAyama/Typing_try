from PyQt5.QtWidgets import QWidget,QGridLayout,QPushButton
from PyQt5.QtCore import pyqtSignal
from .letter_layout import *

class ButtonGroup_base(QWidget):
    text_signal = pyqtSignal(str)
    def on_button_clicked(self):
        button = self.sender()
        if button:
            self.text_signal.emit(button.text())


class ButtonGroup_hina_sei(ButtonGroup_base):
    def __init__(self):
        super().__init__()
        self.buttons = []
        self.init_ui()

    def init_ui(self):
        keyboard_layout = Keyboard_Layout()
        positions = [(i,j) for i in range(11) for j in range(5)]
        grid = QGridLayout()
        self.setLayout(grid)

        for position, name in zip(positions,keyboard_layout.seion_hinagana):
            placeholder = QWidget()
            button = QPushButton(name)
            button.clicked.connect(self.on_button_clicked)
            if name != '':
                self.buttons.append(button)
                grid.addWidget(button, position[0], position[1])
            else:
                grid.addWidget(placeholder, position[0], position[1])

