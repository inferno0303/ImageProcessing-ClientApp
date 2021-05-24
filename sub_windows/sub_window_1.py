import cv2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# 子窗口布局
from sub_windows import ui_sub_window_1


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = ui_sub_window_1.Ui_Form()
        self.ui.setupUi(self)
        self.ui_init()
        self.cv_srcImage = None
        self.q_image = None

    def ui_init(self):
        self.ui.pushButton_open_file.clicked.connect(self.open_file)
        self.ui.pushButton_gray_convert.clicked.connect(self.gray_convert)
        self.ui.pushButton_bin_convert.clicked.connect(self.bin_convert)
        self.ui.pushButton_reset.clicked.connect(self.reset)

    def open_file(self):
        file_path, file_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '', '图像文件(*.jpg *.bmp *.png)')
        self.cv_srcImage = cv2.imread(file_path)
        height, width, channels = self.cv_srcImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image.height())
        self._update_qimage_to_label(ui_image)
        self._show_image_information(1)
        self._set_pushbutton_enabled()

    def gray_convert(self):
        gray_image = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2GRAY)
        height, width = gray_image.shape
        ui_image = QImage(cv2.cvtColor(gray_image, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image.height())
        self._update_qimage_to_label(ui_image)
        self._show_image_information(2)

    def bin_convert(self):
        threshold_value = int(self.ui.spinBox_bin_threshold.value())
        gray_image = cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2GRAY)
        ret, bin_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
        height, width = bin_image.shape
        ui_image = QImage(cv2.cvtColor(bin_image, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image.height())
        self._update_qimage_to_label(ui_image)
        self._show_image_information(3)

    def reset(self):
        height, width, channels = self.cv_srcImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image.height())
        self._update_qimage_to_label(ui_image)
        self._show_image_information(1)

    def _update_qimage_to_label(self, qimage):
        self.ui.label_image.setPixmap(QPixmap.fromImage(qimage))

    def _show_image_information(self, current_image_type):
        if current_image_type == 1:
            self.ui.label_color_space_2.setText('彩色图')
        if current_image_type == 2:
            self.ui.label_color_space_2.setText('灰度图')
        if current_image_type == 3:
            self.ui.label_color_space_2.setText('二值图')

    def _set_pushbutton_enabled(self):
        self.ui.pushButton_gray_convert.setEnabled(True)
        self.ui.pushButton_bin_convert.setEnabled(True)
        self.ui.pushButton_reset.setEnabled(True)