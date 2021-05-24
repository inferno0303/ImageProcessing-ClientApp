# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(733, 546)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 10, 291, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 130, 331, 261))
        self.groupBox.setObjectName("groupBox")
        self.pushButton_1 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_1.setGeometry(QtCore.QRect(40, 50, 111, 71))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 50, 111, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 140, 111, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 140, 111, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(380, 130, 331, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_8.setGeometry(QtCore.QRect(180, 140, 111, 71))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setGeometry(QtCore.QRect(180, 50, 111, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setGeometry(QtCore.QRect(50, 50, 111, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 140, 111, 71))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_10 = QtWidgets.QPushButton(Form)
        self.pushButton_10.setGeometry(QtCore.QRect(560, 430, 111, 71))
        self.pushButton_10.setObjectName("pushButton_10")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图像处理仿真系统"))
        self.label.setText(_translate("Form", "图像处理仿真系统"))
        self.groupBox.setTitle(_translate("Form", "图像变换"))
        self.pushButton_1.setText(_translate("Form", "色彩空间转换"))
        self.pushButton_2.setText(_translate("Form", "图像缩放剪裁"))
        self.pushButton_3.setText(_translate("Form", "图像加噪平滑"))
        self.pushButton_4.setText(_translate("Form", "图像锐化"))
        self.groupBox_2.setTitle(_translate("Form", "应用实例"))
        self.pushButton_8.setText(_translate("Form", "人脸检测"))
        self.pushButton_6.setText(_translate("Form", "图像压缩"))
        self.pushButton_5.setText(_translate("Form", "直方图变换"))
        self.pushButton_7.setText(_translate("Form", "边缘检测"))
        self.pushButton_10.setText(_translate("Form", "关于"))

