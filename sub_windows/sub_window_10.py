from PyQt5.QtWidgets import *

# 子窗口布局
from sub_windows import ui_sub_window_10


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = ui_sub_window_10.Ui_Form()
        self.ui.setupUi(self)
        self.cv_srcImage = None
        self.saveImage = None
        self.ui_init()

    def ui_init(self):
        pass

