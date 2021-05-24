import cv2
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# 子窗口布局
from sub_windows import ui_sub_window_3


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = ui_sub_window_3.Ui_Form()
        self.ui.setupUi(self)
        self.ui_init()
        self.cv_srcImage = None
        self.cv_noiseImage = None
        self.cv_blurImage = None

    def ui_init(self):
        self._group_enable_ctrl()
        # 下拉选择
        noise_type_list = ['椒盐噪声', '高斯噪声', '乘积性噪声']
        self.ui.comboBox_noise_type.addItems(noise_type_list)
        self.ui.comboBox_noise_type.activated.connect(self.comboBox_noise_type_selected)
        filter_type_list = ['均值滤波', '高斯滤波', '中值滤波', '双边滤波']
        self.ui.comboBox_filter_type.addItems(filter_type_list)
        self.ui.comboBox_filter_type.activated.connect(self.comboBox_filter_type_selected)
        # 按钮
        self.ui.pushButton_open_file.clicked.connect(self.open_file)
        self.ui.pushButton_salt_pepper_noise.clicked.connect(self.salt_pepper_noise)
        self.ui.pushButton_gasuss_noise.clicked.connect(self.gasuss_noise)
        self.ui.pushButton_speckle_noise.clicked.connect(self.speckle_noise)
        self.ui.pushButton_mean_blur_filter.clicked.connect(self.mean_blur_filter)
        self.ui.pushButton_gauss_blur_filter.clicked.connect(self.gauss_blur_filter)
        self.ui.pushButton_median_blur_filter.clicked.connect(self.median_blur_filter)
        self.ui.pushButton_double_blur_filter.clicked.connect(self.double_blur_filter)

    def _group_enable_ctrl(self, flag=None):
        if flag is None:
            self.ui.groupBox_salt_noise.setEnabled(False)
            self.ui.groupBox_gauss_noise.setEnabled(False)
            self.ui.groupBox_speckle_noise.setEnabled(False)
            self.ui.groupBox_mean_blur_filter.setEnabled(False)
            self.ui.groupBox_gauss_blur_filter.setEnabled(False)
            self.ui.groupBox_median_blur_filter.setEnabled(False)
            self.ui.groupBox_double_blur_filter.setEnabled(False)
        elif flag == '椒盐噪声' and self.cv_srcImage is not None:
            self.ui.groupBox_salt_noise.setEnabled(True)
            self.ui.groupBox_gauss_noise.setEnabled(False)
            self.ui.groupBox_speckle_noise.setEnabled(False)
        elif flag == '高斯噪声' and self.cv_srcImage is not None:
            self.ui.groupBox_salt_noise.setEnabled(False)
            self.ui.groupBox_gauss_noise.setEnabled(True)
            self.ui.groupBox_speckle_noise.setEnabled(False)
        elif flag == '乘积性噪声' and self.cv_srcImage is not None:
            self.ui.groupBox_salt_noise.setEnabled(False)
            self.ui.groupBox_gauss_noise.setEnabled(False)
            self.ui.groupBox_speckle_noise.setEnabled(True)
        elif flag == '均值滤波' and self.cv_srcImage is not None:
            self.ui.groupBox_mean_blur_filter.setEnabled(True)
            self.ui.groupBox_gauss_blur_filter.setEnabled(False)
            self.ui.groupBox_median_blur_filter.setEnabled(False)
            self.ui.groupBox_double_blur_filter.setEnabled(False)
        elif flag == '高斯滤波' and self.cv_srcImage is not None:
            self.ui.groupBox_mean_blur_filter.setEnabled(False)
            self.ui.groupBox_gauss_blur_filter.setEnabled(True)
            self.ui.groupBox_median_blur_filter.setEnabled(False)
            self.ui.groupBox_double_blur_filter.setEnabled(False)
        elif flag == '中值滤波' and self.cv_srcImage is not None:
            self.ui.groupBox_mean_blur_filter.setEnabled(False)
            self.ui.groupBox_gauss_blur_filter.setEnabled(False)
            self.ui.groupBox_median_blur_filter.setEnabled(True)
            self.ui.groupBox_double_blur_filter.setEnabled(False)
        elif flag == '双边滤波' and self.cv_srcImage is not None:
            self.ui.groupBox_mean_blur_filter.setEnabled(False)
            self.ui.groupBox_gauss_blur_filter.setEnabled(False)
            self.ui.groupBox_median_blur_filter.setEnabled(False)
            self.ui.groupBox_double_blur_filter.setEnabled(True)

    def open_file(self):
        file_path, file_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '', '*.jpg *.bmp *.png *tif')
        self.cv_srcImage = cv2.imread(file_path)
        height, width, channels = self.cv_srcImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_1.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_1.height())
        self.ui.label_image_1.setPixmap(QPixmap.fromImage(ui_image))

    def comboBox_noise_type_selected(self):
        selected = self.ui.comboBox_noise_type.currentText()
        self._group_enable_ctrl(flag=selected)

    def comboBox_filter_type_selected(self):
        selected = self.ui.comboBox_filter_type.currentText()
        self._group_enable_ctrl(flag=selected)

    def salt_pepper_noise(self):
        def _salt_pepper_noise(image, proportion, mode=1):
            copyImage = image.copy()
            height, width, channels = copyImage.shape
            noise_pixel_num = int(height * width * proportion)
            if mode == 1 and channels == 3:
                for k in range(noise_pixel_num):
                    x_axis = int(np.random.random() * width)
                    y_axis = int(np.random.random() * height)
                    salt_pepper_flag = np.random.choice((True, False))
                    copyImage[y_axis, x_axis, 0] = 255 if salt_pepper_flag else 0
                    copyImage[y_axis, x_axis, 1] = 255 if salt_pepper_flag else 0
                    copyImage[y_axis, x_axis, 2] = 255 if salt_pepper_flag else 0
                return copyImage
            elif mode == 1 and channels == 2:
                for k in range(noise_pixel_num):
                    x_axis = int(np.random.random() * width)
                    y_axis = int(np.random.random() * height)
                    salt_pepper_flag = np.random.choice((True, False))
                    copyImage[y_axis, x_axis] = 255 if salt_pepper_flag else 0
                return copyImage
            elif mode == 2 and channels == 3:
                for k in range(noise_pixel_num):
                    x_axis = int(np.random.random() * width)
                    y_axis = int(np.random.random() * height)
                    copyImage[y_axis, x_axis, 0] = 255
                    copyImage[y_axis, x_axis, 1] = 255
                    copyImage[y_axis, x_axis, 2] = 255
                return copyImage
            elif mode == 2 and channels == 2:
                for k in range(noise_pixel_num):
                    x_axis = int(np.random.random() * width)
                    y_axis = int(np.random.random() * height)
                    copyImage[y_axis, x_axis] = 255
                return copyImage
            elif mode == 3 and channels == 3:
                for k in range(noise_pixel_num):
                    x_axis = int(np.random.random() * width)
                    y_axis = int(np.random.random() * height)
                    copyImage[y_axis, x_axis, 0] = 0
                    copyImage[y_axis, x_axis, 1] = 0
                    copyImage[y_axis, x_axis, 2] = 0
                return copyImage
            elif mode == 3 and channels == 3:
                for k in range(noise_pixel_num):
                    x_axis = int(np.random.random() * width)
                    y_axis = int(np.random.random() * height)
                    copyImage[y_axis, x_axis] = 0
                return copyImage
        proportion = self.ui.doubleSpinBox_salt_proportion.value()
        mode = 1
        if self.ui.radioButton_1.isChecked():
            mode = 1
        elif self.ui.radioButton_2.isChecked():
            mode = 2
        elif self.ui.radioButton_3.isChecked():
            mode = 3
        self.cv_noiseImage = _salt_pepper_noise(image=self.cv_srcImage, proportion=proportion, mode=mode)
        height, width, channels = self.cv_noiseImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_noiseImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_2.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_2.height())
        self.ui.label_image_2.setPixmap(QPixmap.fromImage(ui_image))

    def gasuss_noise(self):
        def _gasuss_noise(image, mean=0.0, var=0.1):
            copyImage = image.copy()
            noise = np.random.normal(loc=mean, scale=var, size=copyImage.shape)
            copyImage = np.array(copyImage / 255, dtype=float)
            out = copyImage + noise
            out = np.clip(out, 0.0, 1.0)
            out = np.uint8(out * 255)
            return out
        mean = self.ui.doubleSpinBox_gauss_mean.value()
        var = self.ui.doubleSpinBox_gauss_var.value()
        self.cv_noiseImage = _gasuss_noise(image=self.cv_srcImage, mean=mean, var=var)
        height, width, channels = self.cv_noiseImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_noiseImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_2.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_2.height())
        self.ui.label_image_2.setPixmap(QPixmap.fromImage(ui_image))

    def speckle_noise(self):
        def _speckle_noise(image, mean=0.0, var=0.2):
            copyImage = image.copy()
            noise = np.random.normal(loc=mean, scale=var, size=copyImage.shape)
            copyImage = np.array(copyImage / 255, dtype=float)
            out = (1 + noise) * copyImage
            out = np.clip(out, 0.0, 1.0)
            out = np.uint8(out * 255)
            return out

        mean = self.ui.doubleSpinBox_speckle_mean.value()
        var = self.ui.doubleSpinBox_speckle_var.value()
        self.cv_noiseImage = _speckle_noise(image=self.cv_srcImage, mean=mean, var=var)
        height, width, channels = self.cv_noiseImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_noiseImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_2.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_2.height())
        self.ui.label_image_2.setPixmap(QPixmap.fromImage(ui_image))

    def mean_blur_filter(self):
        def _mean_blur_filter(image, size=5):
            copyImage = image.copy()
            if int(size) % 2 == 0:
                return None
            copyImage = cv2.blur(copyImage, ksize=(int(size), int(size)))
            return copyImage
        size = self.ui.spinBox_mean_ksize.value()
        self.cv_blurImage = _mean_blur_filter(image=self.cv_noiseImage, size=size)
        height, width, channels = self.cv_blurImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_blurImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_3.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_3.height())
        self.ui.label_image_3.setPixmap(QPixmap.fromImage(ui_image))

    def gauss_blur_filter(self):
        def _gauss_blur_filter(image, size=5):
            copyImage = image.copy()
            if int(size) % 2 == 0:
                return None
            copyImage = cv2.GaussianBlur(copyImage, ksize=(int(size), int(size)), sigmaX=0, sigmaY=0)
            return copyImage
        size = self.ui.spinBox_gauss_blur_ksize.value()
        self.cv_blurImage = _gauss_blur_filter(image=self.cv_noiseImage, size=size)
        height, width, channels = self.cv_blurImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_blurImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_3.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_3.height())
        self.ui.label_image_3.setPixmap(QPixmap.fromImage(ui_image))

    def median_blur_filter(self):
        def _median_blur_filter(image, size=5):
            copyImage = image.copy()
            if int(size) % 2 == 0:
                return None
            copyImage = cv2.medianBlur(copyImage, ksize=int(size))
            return copyImage
        size = self.ui.spinBox_median_ksize.value()
        self.cv_blurImage = _median_blur_filter(image=self.cv_noiseImage, size=size)
        height, width, channels = self.cv_blurImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_blurImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_3.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_3.height())
        self.ui.label_image_3.setPixmap(QPixmap.fromImage(ui_image))

    def double_blur_filter(self):
        def _double_blur_filter(image):
            copyImage = image.copy()
            copyImage = cv2.bilateralFilter(copyImage, d=25, sigmaColor=25 * 2, sigmaSpace=25 / 2)
            return copyImage
        self.cv_blurImage = _double_blur_filter(image=self.cv_srcImage)
        height, width, channels = self.cv_blurImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_blurImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_3.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_3.height())
        self.ui.label_image_3.setPixmap(QPixmap.fromImage(ui_image))
        cv2.namedWindow('haha', cv2.WINDOW_NORMAL)
        cv2.imshow('haha', self.cv_blurImage)
        cv2.waitKey(0)
