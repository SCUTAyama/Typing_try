from typing import Text
from PyQt5.QtWidgets import QMainWindow,QWidget,QGridLayout,QLineEdit,QPushButton
from PyQt5.QtCore import Qt
from .ui_constants import *
from .button_group_container import *

class TypingUI(QMainWindow):
    def __init__(self):
        super(__class__, self).__init__()
        self.displaying_text = ''
        self.initUI()

    def initUI(self):

        #b = ButtonGroup_hina_sei()

        ui_constants = UI_Constants()
        self.setWindowTitle(ui_constants.MAINWINDOW_TITLE)
        self.setGeometry(*ui_constants.WINDOW_GEOMETRY)

        #Centrol Widget and Grid
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        grid = QGridLayout()
        central_widget.setLayout(grid)

        #Displace Area
        self.display_unit = QLineEdit()
        self.display_unit.setAlignment(Qt.AlignCenter)
        grid.addWidget(self.display_unit,0,0,1,4)

        #Group of hinagana_seion
        hana_sei = ButtonGroup_hina_sei()
        hana_sei.text_signal.connect(self.text_display)
        grid.addWidget(hana_sei,1,0,3,4)


    def text_display(self,text):
        self.displaying_text += text
        self.display_unit.setText(self.displaying_text)