import cv2
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# 子窗口布局
from sub_windows import ui_sub_window_5


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = ui_sub_window_5.Ui_Form()
        self.ui.setupUi(self)
        self.ui_init()
        self.cv_srcImage = None
        self.cv_equImage = None

    def ui_init(self):
        self.ui.pushButton_open_file.clicked.connect(self.open_file)
        self.ui.pushButton_brightness_change.clicked.connect(self.brightness_change)
        self.ui.pushButton_hist_equ.clicked.connect(self.hist_equ)
        pass

    def open_file(self):
        file_path, file_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '', '图像文件(*.jpg *.bmp *.png)')
        self.cv_srcImage = cv2.imread(file_path)
        print(self.cv_srcImage.shape)
        height, width = self.cv_srcImage.shape[0], self.cv_srcImage.shape[1]
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_1.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_1.height())
        self.ui.label_image_1.setPixmap(QPixmap.fromImage(ui_image))
        self._show_hist_image(flag=1)

    def brightness_change(self):
        def _brightness_change(image, p=0):
            copyImage = image.copy()
            copyImage = np.array(copyImage, dtype=np.uint16)
            copyImage = copyImage + p
            copyImage = np.clip(copyImage, 0, 255)
            copyImage = np.array(copyImage, dtype=np.uint8)
            return copyImage
        self.cv_equImage = _brightness_change(image=self.cv_srcImage, p=self.ui.spinBox_brightness_change.value())
        height, width = self.cv_equImage.shape[0], self.cv_equImage.shape[1]
        ui_image = QImage(cv2.cvtColor(self.cv_equImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_2.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_2.height())
        self.ui.label_image_2.setPixmap(QPixmap.fromImage(ui_image))
        self._show_hist_image(flag=2)

    def hist_equ(self):
        def _his_equ(image):
            copyImage = image.copy()
            if copyImage.ndim == 3:
                ycrcbImage = cv2.cvtColor(copyImage, cv2.COLOR_BGR2YCR_CB)
                channels = cv2.split(ycrcbImage)
                channels[0] = cv2.equalizeHist(src=channels[0])
                ycrcbImage = cv2.merge([channels[0], channels[1], channels[2]])
                copyImage = cv2.cvtColor(ycrcbImage, cv2.COLOR_YCR_CB2BGR)
                return copyImage
            elif copyImage.ndim == 2:
                copyImage = cv2.equalizeHist(src=copyImage)
                return copyImage
        self.cv_equImage = _his_equ(image=self.cv_srcImage)
        height, width = self.cv_equImage.shape[0], self.cv_equImage.shape[1]
        ui_image = QImage(cv2.cvtColor(self.cv_equImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_2.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_2.height())
        self.ui.label_image_2.setPixmap(QPixmap.fromImage(ui_image))
        self._show_hist_image(flag=2)

    def _show_hist_image(self, flag=1):
        if flag == 1:
            histImg = self._calc_gray_hist(image=self.cv_srcImage)
            width, height = histImg.shape[0], histImg.shape[1]
            ui_image = QImage(cv2.cvtColor(histImg, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
            self.ui.label_image_3.setPixmap(QPixmap.fromImage(ui_image))
        elif flag == 2:
            histImg = self._calc_gray_hist(image=self.cv_equImage)
            width, height = histImg.shape[0], histImg.shape[1]
            ui_image = QImage(cv2.cvtColor(histImg, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
            self.ui.label_image_4.setPixmap(QPixmap.fromImage(ui_image))

    def _calc_gray_hist(self, image):
        copyImage = image.copy()
        if copyImage.ndim == 3:
            copyImage = cv2.cvtColor(copyImage, cv2.COLOR_BGR2GRAY)
        histArray = cv2.calcHist([copyImage], [0], None, [256], [0, 255])  # 统计数组
        mnVal, maxVal, minLoc, macLoc = cv2.minMaxLoc(histArray)  # 找最大值
        histImg = np.zeros([256, 256, 3], np.uint8)
        hpt = int(0.9 * 256)  # 预留顶部空间
        for i in range(256):
            intensity = int(histArray[i] * hpt / maxVal)  # 柱状图高度
            cv2.line(histImg, (i, 256), (i, 256 - intensity), [255, 255, 255])  # 画线
        return histImg
