import sys
from PyQt5.QtWidgets import QApplication
from src import TypingUI

def main():
    app = QApplication(sys.argv)
    typingUI = TypingUI()
    typingUI.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()