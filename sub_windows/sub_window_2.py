import cv2
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# 子窗口布局
from sub_windows import ui_sub_window_2


class SubWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.ui = ui_sub_window_2.Ui_Form()
        self.ui.setupUi(self)
        self.ui_init()
        self.zoom_factor = 1.0
        self.cv_srcImage = None
        self.q_image = None

    def ui_init(self):
        self.ui.pushButton_open_file.clicked.connect(self.open_file)
        self.ui.pushButton_zoom_in.clicked.connect(self.zoom_in)
        self.ui.pushButton_zoom_out.clicked.connect(self.zoom_out)
        self.ui.pushButton_zoom_reset.clicked.connect(self.zoom_reset)
        self.ui.pushButton_screenshot.clicked.connect(self.clip_image)

    def open_file(self):
        file_path, file_type = QFileDialog.getOpenFileName(QFileDialog(), '选择图片', '', '图像文件(*.jpg *.bmp *.png)')
        self.cv_srcImage = cv2.imread(file_path)
        height, width, channels = self.cv_srcImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image.height())
        self.zoom_factor = 1.0
        self._show_qimage_to_label(ui_image)

    def zoom_in(self):
        if 10 > self.zoom_factor > 0.1:
            self.zoom_factor += 0.1
            print(self.zoom_factor)
            height, width, channels = self.cv_srcImage.shape
            ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
            if width > height:
                ui_image = ui_image.scaledToWidth(self.ui.label_image.width() * self.zoom_factor)
            else:
                ui_image = ui_image.scaledToHeight(self.ui.label_image.height() * self.zoom_factor)
            self._show_qimage_to_label(ui_image)

    def zoom_out(self):
        if 10 > self.zoom_factor > 0.2:
            self.zoom_factor -= 0.1
            print(self.zoom_factor)
            height, width, channels = self.cv_srcImage.shape
            ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
            if width > height:
                ui_image = ui_image.scaledToWidth(self.ui.label_image.width() * self.zoom_factor)
            else:
                ui_image = ui_image.scaledToHeight(self.ui.label_image.height() * self.zoom_factor)
            self._show_qimage_to_label(ui_image)

    def zoom_reset(self):
        self.zoom_factor = 1.0
        height, width, channels = self.cv_srcImage.shape
        ui_image = QImage(cv2.cvtColor(self.cv_srcImage, cv2.COLOR_BGR2RGB), width, height, QImage.Format_RGB888)
        if width > height:
            ui_image = ui_image.scaledToWidth(self.ui.label_image.width())
        else:
            ui_image = ui_image.scaledToHeight(self.ui.label_image.height())
        self._show_qimage_to_label(ui_image)

    def clip_image(self):
        anchor_x = int(self.ui.spinBox_anchor_x.value())
        anchor_y = int(self.ui.spinBox_anchor_y.value())
        offset_x = int(self.ui.spinBox_X_offset.value())
        offset_y = int(self.ui.spinBox_Y_offset.value())
        clip_image = self.cv_srcImage.copy()[anchor_y: offset_y - 1, anchor_x: offset_x - 1]
        cv2.imshow('clip_image', clip_image)
        cv2.waitKey(0)

    def _show_zoom_factor(self):
        self.ui.label_zoom_factor_2.setText(str(self.zoom_factor)[:3] + 'x')

    def _update_srcImage_size(self):
        height, width, channels = self.cv_srcImage.shape
        self.ui.label_srcImage_size.setText('原图X轴*Y轴：' + str(width) + ' x ' + str(height))
        self.ui.spinBox_anchor_x.setMaximum(width)
        self.ui.spinBox_anchor_y.setMaximum(height)
        self.ui.spinBox_X_offset.setMaximum(width)
        self.ui.spinBox_Y_offset.setMaximum(height)
        self.ui.spinBox_anchor_x.setValue(0)
        self.ui.spinBox_anchor_y.setValue(0)
        self.ui.spinBox_X_offset.setValue(width)
        self.ui.spinBox_Y_offset.setValue(height)

    def _show_qimage_to_label(self, qimage):
        self.ui.label_image.setPixmap(QPixmap.fromImage(qimage))
        self._show_zoom_factor()
        self._update_srcImage_size()