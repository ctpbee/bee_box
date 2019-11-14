import sys

from PySide2.QtWidgets import QApplication
from app.mainwindow import MainWindow
from app.initial import box_init

if __name__ == '__main__':
    box_init()
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("bee_box")
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())
