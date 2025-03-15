from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import pyqtSignal
from .letter_layout import Keyboard_Layout

class BaseButtonGroup(QWidget):
    text_signal = pyqtSignal(str)
    def __init__(self, layout_data=None, grid_size=None):
        super().__init__()
        self.buttons = []
        self.layout_data = layout_data
        self.grid_size = grid_size
        if layout_data:
            self.init_ui()

    def on_button_clicked(self):
        button = self.sender()
        if button:
            self.text_signal.emit(button.text())

    def init_ui(self):
        if not self.layout_data or not self.grid_size:
            return
        positions = [(i,j) for i in range(self.grid_size[0]) for j in range(self.grid_size[1])]
        grid = QGridLayout()
        self.setLayout(grid)

        for position, name in zip(positions, self.layout_data):
            if name != '':
                button = QPushButton(name)
                button.clicked.connect(self.on_button_clicked)
                self.buttons.append(button)
                grid.addWidget(button, position[0], position[1])
            else:
                placeholder = QWidget()
                grid.addWidget(placeholder, position[0], position[1])

class HiraganaSeionGroup(BaseButtonGroup):
    def __init__(self):
        keyboard_layout = Keyboard_Layout()
        super().__init__(keyboard_layout.seion_hiragana, (11, 5))

class KatakanaSeionGroup(BaseButtonGroup):
    def __init__(self):
        keyboard_layout = Keyboard_Layout()
        super().__init__(keyboard_layout.seion_katakana, (11, 5))

class HiraganaDakuonGroup(BaseButtonGroup):
    def __init__(self):
        keyboard_layout = Keyboard_Layout()
        super().__init__(keyboard_layout.dakuon_hiragana, (4, 5))

class KatakanaDakuonGroup(BaseButtonGroup):
    def __init__(self):
        keyboard_layout = Keyboard_Layout()
        super().__init__(keyboard_layout.dakuon_katakana, (4, 5))

class HiraganaHandakuonGroup(BaseButtonGroup):
    def __init__(self):
        keyboard_layout = Keyboard_Layout()
        super().__init__(keyboard_layout.handakuon_hiragana, (1, 5))

class KatakanaHandakuonGroup(BaseButtonGroup):
    def __init__(self):
        keyboard_layout = Keyboard_Layout()
        super().__init__(keyboard_layout.handakuon_katakana, (1, 5))

class HiraganaSmallGroup(BaseButtonGroup):
    def __init__(self):
        keyboard_layout = Keyboard_Layout()
        super().__init__(keyboard_layout.small_hiragana, (3, 3))

class KatakanaSmallGroup(BaseButtonGroup):
    def __init__(self):
        keyboard_layout = Keyboard_Layout()
        super().__init__(keyboard_layout.small_katakana, (3, 3))

class SpecialCharacterGroup(BaseButtonGroup):
    def __init__(self):
        keyboard_layout = Keyboard_Layout()
        super().__init__(keyboard_layout.special, (1, 1))
