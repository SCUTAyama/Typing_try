from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from .ui_constants import UI_Constants
from .button_group_container import *

class TypingUI(QMainWindow):
    def __init__(self):
        super(__class__, self).__init__()
        self.displaying_text = ''
        self.input_modes = ['Hiragana','Katakana']
        self.input_mode = self.input_modes[0]
        self.initUI()

    def initUI(self):
        #Window Settings
        ui_constants = UI_Constants()
        self.setWindowTitle(ui_constants.MAINWINDOW_TITLE)
        self.setGeometry(*ui_constants.WINDOW_GEOMETRY)

        self.setStyleSheet(ui_constants.UI_STYLE)

        #Centrol Widget and Grid
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.grid = QGridLayout()
        central_widget.setLayout(self.grid)

        #Displace Area
        self.display_unit = QLineEdit()
        self.display_unit.setAlignment(Qt.AlignCenter)
        self.grid.addWidget(self.display_unit,0,0,1,9)

        #Initialize the layout 
        self.current_group = DisplayGroupContainer()
        self.current_group.text_signal.connect(self.text_display)
        self.grid.addWidget(self.current_group,1,0,12,10)


        #Mode Switch
        self.mode_switch = QPushButton("Hira")
        self.mode_switch.setStyleSheet(ui_constants.SWITCH_BUTTON_STYLE)
        self.mode_switch.clicked.connect(self.switch_mode)
        self.grid.addWidget(self.mode_switch,0,9,1,1)


    def text_display(self,text):
        self.displaying_text += text
        self.display_unit.setText(self.displaying_text)

    def switch_mode(self):
        self.current_group.setParent(None)
        if self.input_mode == 'Hiragana':
            self.input_mode = 'Katakana'
            self.current_group = DisplayGroupContainer(group_switch_mode="Katakana")
            self.mode_switch.setText("Kata")
        else :
            self.input_mode = 'Hiragana'
            self.current_group = DisplayGroupContainer(group_switch_mode="Hiragana")       
            self.mode_switch.setText("Hira")
        self.current_group.text_signal.connect(self.text_display)
        self.grid.addWidget(self.current_group,1,0,12,10)