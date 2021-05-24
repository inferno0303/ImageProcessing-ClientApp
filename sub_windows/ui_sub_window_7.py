# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_sub_window_7.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1269, 613)
        self.label_image_2 = QtWidgets.QLabel(Form)
        self.label_image_2.setGeometry(QtCore.QRect(720, 10, 450, 450))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_image_2.setFont(font)
        self.label_image_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_image_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_image_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image_2.setObjectName("label_image_2")
        self.pushButton_open_file = QtWidgets.QPushButton(Form)
        self.pushButton_open_file.setGeometry(QtCore.QRect(80, 80, 111, 28))
        self.pushButton_open_file.setCheckable(False)
        self.pushButton_open_file.setDefault(True)
        self.pushButton_open_file.setObjectName("pushButton_open_file")
        self.label_image_1 = QtWidgets.QLabel(Form)
        self.label_image_1.setGeometry(QtCore.QRect(250, 10, 450, 450))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_image_1.setFont(font)
        self.label_image_1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_image_1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_image_1.setScaledContents(False)
        self.label_image_1.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image_1.setObjectName("label_image_1")
        self.groupBox_1 = QtWidgets.QGroupBox(Form)
        self.groupBox_1.setGeometry(QtCore.QRect(30, 190, 191, 251))
        self.groupBox_1.setObjectName("groupBox_1")
        self.pushButton_canny = QtWidgets.QPushButton(self.groupBox_1)
        self.pushButton_canny.setGeometry(QtCore.QRect(50, 190, 93, 28))
        self.pushButton_canny.setObjectName("pushButton_canny")
        self.spinBox_low_th = QtWidgets.QSpinBox(self.groupBox_1)
        self.spinBox_low_th.setGeometry(QtCore.QRect(120, 50, 61, 41))
        self.spinBox_low_th.setMaximum(255)
        self.spinBox_low_th.setProperty("value", 150)
        self.spinBox_low_th.setObjectName("spinBox_low_th")
        self.label = QtWidgets.QLabel(self.groupBox_1)
        self.label.setGeometry(QtCore.QRect(10, 50, 81, 41))
        self.label.setObjectName("label")
        self.spinBox_high_th = QtWidgets.QSpinBox(self.groupBox_1)
        self.spinBox_high_th.setGeometry(QtCore.QRect(120, 110, 61, 41))
        self.spinBox_high_th.setMaximum(255)
        self.spinBox_high_th.setProperty("value", 200)
        self.spinBox_high_th.setObjectName("spinBox_high_th")
        self.label_2 = QtWidgets.QLabel(self.groupBox_1)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 81, 41))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "边缘检测"))
        self.label_image_2.setText(_translate("Form", "处理后的图像"))
        self.pushButton_open_file.setText(_translate("Form", "打开图片"))
        self.label_image_1.setText(_translate("Form", "原图"))
        self.groupBox_1.setTitle(_translate("Form", "Canny边缘检测"))
        self.pushButton_canny.setText(_translate("Form", "确定"))
        self.label.setText(_translate("Form", "低阈值抑制"))
        self.label_2.setText(_translate("Form", "高阈值抑制"))

