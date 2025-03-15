from PyQt5.QtWidgets import QWidget,QGridLayout,QPushButton
from .letter_layout import *

class ButtonGroup_base(QWidget):
    def on_button_clicked(self):
        #to do
        raise NotImplementedError

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
            if name != '':
                self.buttons.append(button)
                grid.addWidget(button, position[0], position[1])
            else:
                grid.addWidget(placeholder, position[0], position[1])

