import sys

from PySide2.QtWidgets import QApplication
from app.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())
