import cv2
import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# 子窗口布局
from sub_windows import ui_sub_window_6


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = ui_sub_window_6.Ui_Form()
        self.ui.setupUi(self)
        self.cv_srcImage = None
        self.saveImage = None
        self.ui_init()

    def ui_init(self):
        self.ui.pushButton_open_file.clicked.connect(self.open_file)
        self.ui.pushButton_dct_process.clicked.connect(self.dct_process)
        self.ui.pushButton_save.clicked.connect(self.save)

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

    def dct_process(self):
        if self.cv_srcImage is None:
            return
        # 判断radio
        mask_flag = 6
        if self.ui.radioButton_s1.isChecked():
            print('s1')
            mask_flag = 1
        elif self.ui.radioButton_s3.isChecked():
            print('s3')
            mask_flag = 3
        elif self.ui.radioButton_s6.isChecked():
            print('s6')
            mask_flag = 6
        elif self.ui.radioButton_s10.isChecked():
            print('s10')
            mask_flag = 10
        elif self.ui.radioButton_s15.isChecked():
            print('s15')
            mask_flag = 15
        elif self.ui.radioButton_s21.isChecked():
            print('s21')
            mask_flag = 21
        # DCT处理
        compressImage = self._dct_test(image=self.cv_srcImage, block=8, mask_flag=mask_flag)
        self.saveImage = compressImage.copy()
        height, width = compressImage.shape[0], compressImage.shape[1]
        ui_image = QImage(cv2.cvtColor(compressImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image_1.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image_1.height())
        self.ui.label_image_2.setPixmap(QPixmap.fromImage(ui_image))

    def _dct_test(self, image, block=8, mask_flag=10):
        mask_21 = np.uint8([[1, 1, 1, 1, 1, 1, 0, 0],
                            [1, 1, 1, 1, 1, 0, 0, 0],
                            [1, 1, 1, 1, 0, 0, 0, 0],
                            [1, 1, 1, 0, 0, 0, 0, 0],
                            [1, 1, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]])
        mask_15 = np.uint8([[1, 1, 1, 1, 1, 0, 0, 0],
                            [1, 1, 1, 1, 0, 0, 0, 0],
                            [1, 1, 1, 0, 0, 0, 0, 0],
                            [1, 1, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]])
        mask_10 = np.uint8([[1, 1, 1, 1, 0, 0, 0, 0],
                            [1, 1, 1, 0, 0, 0, 0, 0],
                            [1, 1, 0, 0, 0, 0, 0, 0],
                            [1, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0]])
        mask_6 = np.uint8([[1, 1, 1, 0, 0, 0, 0, 0],
                           [1, 1, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]])
        mask_3 = np.uint8([[1, 1, 0, 0, 0, 0, 0, 0],
                           [1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]])
        mask_1 = np.uint8([[1, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]])
        mask = mask_10
        if mask_flag == 1:
            mask = mask_1
        elif mask_flag == 3:
            mask = mask_3
        elif mask_flag == 6:
            mask = mask_6
        elif mask_flag == 10:
            mask = mask_10
        elif mask_flag == 15:
            mask = mask_15
        elif mask_flag == 21:
            mask = mask_21

        srcImage = cv2.cvtColor(image.copy(), cv2.COLOR_BGR2YUV)
        retImage = np.zeros(
            ((srcImage.shape[0] // block + 1) * block, (srcImage.shape[1] // block + 1) * block, srcImage.ndim),
            np.float32)
        channels = cv2.split(srcImage)
        Y_channel_float = np.array(channels[0], dtype=np.float32)
        U_channel_float = np.array(channels[1], dtype=np.float32)
        V_channel_float = np.array(channels[2], dtype=np.float32)
        retImage[0: Y_channel_float.shape[0], 0: Y_channel_float.shape[1], 0] = Y_channel_float
        retImage[0: U_channel_float.shape[0], 0: U_channel_float.shape[1], 1] = U_channel_float
        retImage[0: V_channel_float.shape[0], 0: V_channel_float.shape[1], 2] = V_channel_float

        T = np.zeros((block, block), np.float64)
        T[0, :] = 1 * np.sqrt(1 / block)
        for i in range(1, block):
            for j in range(0, block):
                T[i, j] = np.cos(np.pi * i * (2 * j + 1) / (2 * block)) * np.sqrt(2 / block)

        for y_offset in range(int(retImage.shape[0] / block)):
            for x_offset in range(int(retImage.shape[1] / block)):
                for c in range(int(retImage.ndim)):
                    # opencv的方法
                    # subImg = retImage[y_offset * block: y_offset * block + block, x_offset * block: x_offset * block + block, c]
                    # subImg = cv2.dct(subImg) * mask
                    # subImg = cv2.idct(subImg)
                    # retImage[y_offset * block: y_offset * block + block, x_offset * block: x_offset * block + block, c] = subImg
                    # 自建的方法
                    subImg = retImage[y_offset * block: y_offset * block + block,
                             x_offset * block: x_offset * block + block, c]
                    dctImg = np.dot(np.dot(T, subImg), np.transpose(T)) * mask
                    subImg = np.dot(np.dot(np.transpose(T), dctImg), T)
                    retImage[y_offset * block: y_offset * block + block, x_offset * block: x_offset * block + block,
                    c] = subImg
        retImage = cv2.cvtColor(np.uint8(retImage), cv2.COLOR_YUV2BGR)
        retImage = retImage[0: srcImage.shape[0], 0: srcImage.shape[1]]
        return retImage

    def save(self):
        if self.saveImage is None:
            return
        jpg_image = cv2.imencode('.jpg', self.saveImage)[1]
        fp = open('.././dctCompressImage.jpg', 'wb')
        fp.write(jpg_image)
        fp.close()
        print('ok')



