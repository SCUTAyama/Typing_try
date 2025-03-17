class UI_Constants:


    #设置主界面标题
    MAINWINDOW_TITLE = 'Typing'

    #设置主界面尺寸
    WINDOW_GEOMETRY = (1100,300,800,400)

    BASE_BUTTON_STYLE = """
            QPushButton {
                background-color: white;
                color: #333333;
                border: 1px solid #e0e0e0;
                padding: 8px;
                min-width: 40px;
                min-height: 30px;
                font-family: "MS Gothic";
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                border-color: #d0d0d0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
                border-color: #c0c0c0;
            }
        """

    SWITCH_BUTTON_STYLE = """
            QPushButton {
                background-color: white;
                color: #333333;
                border: 1px solid #e0e0e0;
                padding: 8px;
                min-width: 40px;
                min-height:20px;
                font-family: "MS Gothic";
                font-size: 18px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
                border-color: #d0d0d0;
            }
            QPushButton:pressed {
                background-color: #d0d0d0;
                border-color: #c0c0c0;
            }
        """

    UI_STYLE = """
            QMainWindow, QWidget {
                background-color: white;
            }
            QLineEdit {
                background-color: white;
                border: 1px solid #e0e0e0;
                padding: 5px;
            }

            QLineEdit {
                font-family: "MS Gothic";
                font-size: 18px;
            }
        """