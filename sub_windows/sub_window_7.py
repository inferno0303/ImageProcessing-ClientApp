import cv2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# 子窗口布局
from sub_windows import ui_sub_window_7


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = ui_sub_window_7.Ui_Form()
        self.ui.setupUi(self)
        self.cv_srcImage = None
        self.ui_init()

    def ui_init(self):
        self.ui.pushButton_open_file.clicked.connect(self.open_file)
        self.ui.pushButton_canny.clicked.connect(self.canny_process)

    def open_file(self):
        file_path, file_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '', '图像文件(*.jpg *.bmp *.png)')
        self.cv_srcImage = cv2.imread(file_path)
        height, width = self.cv_srcImage.shape[0], self.cv_srcImage.shape[1]
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_1.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_1.height())
        self.ui.label_image_1.setPixmap(QPixmap.fromImage(ui_image))

    def canny_process(self):
        if self.cv_srcImage is None:
            return
        low_th = int(self.ui.spinBox_low_th.value())
        high_th = int(self.ui.spinBox_high_th.value())
        edgeImg = cv2.Canny(self.cv_srcImage.copy(), low_th, high_th)
        height, width = edgeImg.shape[0], edgeImg.shape[1]
        ui_image = QImage(cv2.cvtColor(edgeImg, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_1.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_1.height())
        self.ui.label_image_2.setPixmap(QPixmap.fromImage(ui_image))
