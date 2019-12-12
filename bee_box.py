import sys

from PySide2.QtGui import QFont
from PySide2.QtWidgets import QApplication
from app.mainwindow import MainWindow

if __name__ == '__main__':
    try:
        import ctypes

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("bee_box")
    except Exception as e:
        print(e)

    app = QApplication(sys.argv)
    font = QFont()
    font.setFamily("微软雅黑")
    app.setFont(font)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
