import re
import subprocess

from PySide2.QtCore import QThreadPool
from PySide2.QtGui import QCloseEvent
from PySide2.QtWidgets import QWidget, QFileDialog, QTableWidgetItem, QAbstractItemView, QMessageBox

from app.lib.global_var import G
from app.lib.path_lib import get_py_version
from app.ui.ui_py_manage import Ui_Form
from app.ui.ui_interpretes import Ui_Interpreters
from app.ui.ui_new_env import Ui_NewEnv
from app.ui.ui_modify_env import Ui_Modify
from app.honey.worker import Worker


class PyManageWidget(QWidget, Ui_Form):
    def __init__(self, home):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.home = home
        self.thread_pool = QThreadPool()
        # btn
        self.py_setting_btn.clicked.connect(self.py_setting_slot)
        self.ok_btn.clicked.connect(self.ok_btn_slot)
        self.cancel_btn.clicked.connect(self.cancel_btn_slot)
        #
        self.py_box.currentTextChanged.connect(self.py_change_slot)
        #
        self.load_py()

    def load_py(self):
        for k, v in G.config.python_path.items():
            self.py_box.addItem(k)
            if G.config.choice_python:
                self.py_box.setCurrentText(k)
                self.path.setText(v)
        if G.config.choice_python:
            py_ = G.config.python_path[G.config.choice_python]
            self.load_pip(py_)

    def load_pip(self, py_):
        self.pip_list.clear()
        output = subprocess.check_output([py_, '-m', 'pip', 'freeze']).decode()
        for i in output.splitlines():
            self.pip_list.addItem(i)

    def py_setting_slot(self):
        self.interpreter = InterpreterWidget()
        self.interpreter.show()

    def ok_btn_slot(self):
        name = self.py_box.currentText()
        G.config.choice_python = name

    def cancel_btn_slot(self):
        pass

    def py_change_slot(self, name):
        path = G.config.python_path[name]
        self.path.setText(G.config.python_path[name])
        self.load_pip(path)


class InterpreterWidget(QWidget, Ui_Interpreters):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.py_table.horizontalHeader().setStretchLastSection(True)  # 最后一列自适应表格宽度
        self.py_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # btn
        self.add_btn.clicked.connect(self.add_btn_slot)
        self.del_btn.clicked.connect(self.del_btn_slot)
        self.change_btn.clicked.connect(self.change_btn_slot)
        #
        self.load_py()

    def load_py(self):
        self.py_table.setRowCount(0)
        for k, v in G.config.python_path.items():
            self.py_table.insertRow(0)
            self.py_table.setItem(0, 0, QTableWidgetItem(str(k)))
            self.py_table.setItem(0, 1, QTableWidgetItem(str(v)))

    def add_btn_slot(self):
        self.new_env = NewEnvWidget(self)
        self.new_env.show()

    def del_btn_slot(self):
        row = self.py_table.currentRow()
        name = self.py_table.item(row, 0).text()
        replay = QMessageBox.question(self, '提示', '确定删除吗？', QMessageBox.Yes | QMessageBox.Cancel, QMessageBox.Cancel)
        if replay == QMessageBox.Yes:
            G.config.python_path.pop(name, None)
            self.load_py()

    def change_btn_slot(self):
        row = self.py_table.currentRow()
        name = self.py_table.item(row, 0).text()
        path = self.py_table.item(row, 1).text()
        self.modify_env = ModifyEnvWidget(self, name, path)
        self.modify_env.show()


class NewEnvWidget(QWidget, Ui_NewEnv):
    def __init__(self, parent):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.parent = parent


class ModifyEnvWidget(QWidget, Ui_Modify):
    def __init__(self, parent, name, path):
        super(self.__class__, self).__init__()
        self.setupUi(self)
        self.patent = parent
        self.name.setText(name)
        self.path.setText(path)
        self.path_btn.clicked.connect(self.path_btn_slot)
        self.name.textChanged.connect(self.name_change_slot)

    def name_change_slot(self):
        name = self.name.text()
        if name in G.config.python_path:
            self.name.setStyleSheet("color:red")
            self.save_btn.setDisabled(True)
        else:
            self.name.setStyleSheet("color:green")
            self.save_btn.setEnabled(True)

    def path_btn_slot(self):
        pass
