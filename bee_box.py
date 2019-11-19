import sys

from PySide2.QtWidgets import QApplication
from app.mainwindow import MainWindow
from app.initial import box_init
from app.py_notfound import NotFoundDialog

if __name__ == '__main__':
    try:
        import ctypes

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("bee_box")
    except Exception as e:
        print(e)
    try:
        box_init()
        app = QApplication(sys.argv)
        main = MainWindow()
        main.show()
        sys.exit(app.exec_())
    except Exception as e:
        NotFoundDialog.exec_()
