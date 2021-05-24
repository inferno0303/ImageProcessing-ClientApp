import cv2
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# 子窗口布局
from sub_windows import ui_sub_window_4


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = ui_sub_window_4.Ui_Form()
        self.ui.setupUi(self)
        self.ui_init()

    def ui_init(self):
        sharpen_type_list = ['Sobel算子', 'Laplace算子', '自定义卷积核']
        self.ui.comboBox_selector.addItems(sharpen_type_list)
        self.ui.comboBox_selector.activated.connect(self.comboBox_selected)
        self.ui.pushButton_open_file.clicked.connect(self.open_file)
        self.ui.pushButton_sobel_filter.clicked.connect(self.sobel_sharpen_filter)
        self.ui.pushButton_laplace_filter.clicked.connect(self.laplacian_sharpen_filter)
        self.ui.pushButton_custom_filter.clicked.connect(self.custom_filter)
        self.cv_srcImage = None
        self.cv_sharpenImage = None
        self._group_enable_ctrl()
        pass

    def comboBox_selected(self):
        selected = self.ui.comboBox_selector.currentText()
        self._group_enable_ctrl(selected=selected)

    def _group_enable_ctrl(self, selected=None):
        if selected is None:
            self.ui.groupBox_sobel_filter.setEnabled(False)
            self.ui.groupBox_laplace_filter.setEnabled(False)
            self.ui.groupBox_custom_filter.setEnabled(False)
        elif selected == 'Sobel算子':
            self.ui.groupBox_sobel_filter.setEnabled(True)
            self.ui.groupBox_laplace_filter.setEnabled(False)
            self.ui.groupBox_custom_filter.setEnabled(False)
        elif selected == 'Laplace算子':
            self.ui.groupBox_sobel_filter.setEnabled(False)
            self.ui.groupBox_laplace_filter.setEnabled(True)
            self.ui.groupBox_custom_filter.setEnabled(False)
        elif selected == '自定义卷积核':
            self.ui.groupBox_sobel_filter.setEnabled(False)
            self.ui.groupBox_laplace_filter.setEnabled(False)
            self.ui.groupBox_custom_filter.setEnabled(True)

    def open_file(self):
        file_path, file_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '', '图像文件(*.jpg *.bmp *.png)')
        self.cv_srcImage = cv2.imread(file_path)
        height, width, channels = self.cv_srcImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_1.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_1.height())
        self.ui.label_image_1.setPixmap(QPixmap.fromImage(ui_image))

    def sobel_sharpen_filter(self):
        def _sobel_sharpen_filter(image, mode=0):
            copyImage = image.copy()
            if copyImage.ndim == 3:
                copyImage = cv2.cvtColor(copyImage, cv2.COLOR_BGR2GRAY)
            if mode == 1:
                x = cv2.Sobel(copyImage, ddepth=cv2.CV_16S, dx=1, dy=0)
                x = cv2.convertScaleAbs(x)
                return x
            elif mode == 2:
                y = cv2.Sobel(copyImage, ddepth=cv2.CV_16S, dx=0, dy=1)
                y = cv2.convertScaleAbs(y)
                return y
            elif mode == 0:
                x = cv2.Sobel(copyImage, ddepth=cv2.CV_16S, dx=1, dy=0)
                x = cv2.convertScaleAbs(x)
                y = cv2.Sobel(copyImage, ddepth=cv2.CV_16S, dx=0, dy=1)
                y = cv2.convertScaleAbs(y)
                x_y = cv2.addWeighted(x, 0.5, y, 0.5, 0)
                return x_y
        mode = 0
        if self.ui.radioButton_sobel_dx.isChecked():
            mode = 1
        elif self.ui.radioButton_sobel_dy.isChecked():
            mode = 2
        elif self.ui.radioButton_sobel_dx_dy.isChecked():
            mode = 0
        self.cv_sharpenImage = _sobel_sharpen_filter(image=self.cv_srcImage, mode=mode)
        height, width = self.cv_sharpenImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_sharpenImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_2.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_2.height())
        self.ui.label_image_2.setPixmap(QPixmap.fromImage(ui_image))

    def laplacian_sharpen_filter(self):
        def _laplacian_sharpen_filter(image, size=1):
            copyImage = image.copy()
            if copyImage.ndim == 3:
                copyImage = cv2.cvtColor(copyImage, cv2.COLOR_BGR2GRAY)
            copyImage = cv2.Laplacian(copyImage, ddepth=cv2.CV_16S, ksize=int(size))
            copyImage = cv2.convertScaleAbs(copyImage)
            return copyImage
        size = self.ui.spinBox_laplace_ksize.value()
        self.cv_sharpenImage = _laplacian_sharpen_filter(image=self.cv_srcImage, size=size)
        height, width = self.cv_sharpenImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_sharpenImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_2.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_2.height())
        self.ui.label_image_2.setPixmap(QPixmap.fromImage(ui_image))

    def custom_filter(self):
        def _custom_filter(image, custom_kernel=None):
            if custom_kernel is None:
                kernel = np.array([[0, -1.5, 0], [-1.5, 7, -1.5], [0, -1.5, 0]], np.float)
            else:
                kernel = np.array([[custom_kernel[0], custom_kernel[1], custom_kernel[2]],
                                   [custom_kernel[3], custom_kernel[4], custom_kernel[5]],
                                   [custom_kernel[6], custom_kernel[7], custom_kernel[8]]],
                                  np.float)
            dst = cv2.filter2D(src=image, ddepth=cv2.CV_16S, kernel=kernel)
            dst = cv2.convertScaleAbs(dst)
            return dst
        custom_kernel = [self.ui.doubleSpinBox_custom_filter_1.value(), self.ui.doubleSpinBox_custom_filter_2.value(), self.ui.doubleSpinBox_custom_filter_3.value(),
                         self.ui.doubleSpinBox_custom_filter_4.value(), self.ui.doubleSpinBox_custom_filter_5.value(), self.ui.doubleSpinBox_custom_filter_6.value(),
                         self.ui.doubleSpinBox_custom_filter_7.value(), self.ui.doubleSpinBox_custom_filter_8.value(), self.ui.doubleSpinBox_custom_filter_9.value()]
        self.cv_sharpenImage = _custom_filter(image=self.cv_srcImage, custom_kernel=custom_kernel)
        height, width = self.cv_sharpenImage.shape[0], self.cv_sharpenImage.shape[1]
        ui_image = QImage(cv2.cvtColor(self.cv_sharpenImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_2.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_2.height())
        self.ui.label_image_2.setPixmap(QPixmap.fromImage(ui_image))
