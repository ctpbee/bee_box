import webbrowser

from PySide2.QtWidgets import QDialog

from app.ui.ui_py_notfound import Ui_Dialog


class NotFoundDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.commandLinkButton.clicked.connect(self.open_url)

    def open_url(self):
        url = "https://www.python.org/"
        try:
            webbrowser.get('chrome').open_new_tab(url)
        except Exception as e:
            webbrowser.open_new_tab(url)
