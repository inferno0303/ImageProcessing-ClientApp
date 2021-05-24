from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon

# 主布局
from main_windows import ui_main_window

# 子窗口实例
from sub_windows import sub_window_1
from sub_windows import sub_window_2
from sub_windows import sub_window_3
from sub_windows import sub_window_4
from sub_windows import sub_window_5
from sub_windows import sub_window_6
from sub_windows import sub_window_7
from sub_windows import sub_window_8
from sub_windows import sub_window_10


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__(parent=None)
        # 布局初始化
        self.ui = ui_main_window.Ui_Form()
        self.ui.setupUi(Form=self)
        # 子窗口实例化命名空间
        self.sub_window_1_ = None  # 色彩空间转换
        self.sub_window_2_ = None  # 图像缩放剪裁
        self.sub_window_3_ = None  # 图像加噪平滑
        self.sub_window_4_ = None  # 图像锐化
        self.sub_window_5_ = None  # 直方图变换
        self.sub_window_6_ = None  # DCT图像压缩
        self.sub_window_7_ = None  # Canny边缘检测
        self.sub_window_8_ = None  # 人脸检测实例
        self.sub_window_10_ = None  # 关于页面
        # 多线程
        pass
        # 信号与槽定义
        self.signal_and_slot()
        # 图标
        self.setWindowIcon(QIcon('./static/icon.ico'))

    def signal_and_slot(self):
        self.ui.pushButton_1.clicked.connect(self.pushButton_1)
        self.ui.pushButton_2.clicked.connect(self.pushButton_2)
        self.ui.pushButton_3.clicked.connect(self.pushButton_3)
        self.ui.pushButton_4.clicked.connect(self.pushButton_4)
        self.ui.pushButton_5.clicked.connect(self.pushButton_5)
        self.ui.pushButton_6.clicked.connect(self.pushButton_6)
        self.ui.pushButton_7.clicked.connect(self.pushButton_7)
        self.ui.pushButton_8.clicked.connect(self.pushButton_8)
        self.ui.pushButton_10.clicked.connect(self.pushButton_10)

    def pushButton_1(self):
        self.sub_window_1_ = sub_window_1.SubWindow()
        self.sub_window_1_.show()

    def pushButton_2(self):
        self.sub_window_2_ = sub_window_2.SubWindow()
        self.sub_window_2_.show()

    def pushButton_3(self):
        self.sub_window_3_ = sub_window_3.SubWindow()
        self.sub_window_3_.show()

    def pushButton_4(self):
        self.sub_window_4_ = sub_window_4.SubWindow()
        self.sub_window_4_.show()

    def pushButton_5(self):
        self.sub_window_5_ = sub_window_5.SubWindow()
        self.sub_window_5_.show()

    def pushButton_6(self):
        self.sub_window_6_ = sub_window_6.SubWindow()
        self.sub_window_6_.show()

    def pushButton_7(self):
        self.sub_window_7_ = sub_window_7.SubWindow()
        self.sub_window_7_.show()

    def pushButton_8(self):
        self.sub_window_8_ = sub_window_8.SubWindow()
        self.sub_window_8_.show()

    def pushButton_10(self):
        self.sub_window_10_ = sub_window_10.SubWindow()
        self.sub_window_10_.show()
