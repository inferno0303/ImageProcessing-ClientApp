# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_sub_window_8.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(921, 726)
        self.label_title = QtWidgets.QLabel(Form)
        self.label_title.setGeometry(QtCore.QRect(20, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.pushButton_open_file = QtWidgets.QPushButton(Form)
        self.pushButton_open_file.setGeometry(QtCore.QRect(40, 90, 111, 28))
        self.pushButton_open_file.setCheckable(False)
        self.pushButton_open_file.setDefault(True)
        self.pushButton_open_file.setObjectName("pushButton_open_file")
        self.label_image_1 = QtWidgets.QLabel(Form)
        self.label_image_1.setGeometry(QtCore.QRect(210, 10, 700, 700))
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
        self.pushButton_video_captrue = QtWidgets.QPushButton(Form)
        self.pushButton_video_captrue.setGeometry(QtCore.QRect(40, 140, 111, 81))
        self.pushButton_video_captrue.setObjectName("pushButton_video_captrue")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 260, 151, 81))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 40, 72, 15))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "人脸检测"))
        self.label_title.setText(_translate("Form", "人脸检测"))
        self.pushButton_open_file.setText(_translate("Form", "打开图片"))
        self.label_image_1.setText(_translate("Form", "帧预览"))
        self.pushButton_video_captrue.setText(_translate("Form", "开始捕捉摄像头"))
        self.groupBox.setTitle(_translate("Form", "当前帧人脸数量："))
        self.label.setText(_translate("Form", "0"))

