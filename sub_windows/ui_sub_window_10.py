# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_sub_window_10.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(686, 524)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(210, 30, 271, 61))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(100, 110, 491, 261))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(490, 430, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "关于本软件"))
        self.label.setText(_translate("Form", "1561130423-阳旭 的毕业设计"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'黑体\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">本课题针对图像处理的难点，设计了一款界面友好的图像处理仿真系统，意在帮助初学者形象的理解图像处理所涉及的部分知识点。</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">该软件包含常见的图像处理实例，例如图像缩放、加噪、平滑锐化、直方图均衡、压缩编码，边缘检测、人脸检测等。这些模块涉及到较多图像处理知识，通过每个模块设计的实例，循序渐进的让初学者加深理解图像处理方法间的联系，激发初学者对图像处理的兴趣。</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'宋体\';\">本设计利用</span><span style=\" font-family:\'Times New Roman,serif\';\">PyCharm</span><span style=\" font-family:\'宋体\';\">和</span><span style=\" font-family:\'Times New Roman,serif\';\">QT Designer</span><span style=\" font-family:\'宋体\';\">开发平台，基于</span><span style=\" font-family:\'Times New Roman,serif\';\">Python</span><span style=\" font-family:\'宋体\';\">编程语言以及</span><span style=\" font-family:\'Times New Roman,serif\';\">OpenCV</span><span style=\" font-family:\'宋体\';\">计算机视觉库，利用</span><span style=\" font-family:\'Times New Roman,serif\';\">Qt5</span><span style=\" font-family:\'宋体\';\">作为</span><span style=\" font-family:\'Times New Roman,serif\';\">GUI</span><span style=\" font-family:\'宋体\';\">框架，构建了一个兼容</span><span style=\" font-family:\'Times New Roman,serif\';\">Windows-x86</span><span style=\" font-family:\'宋体\';\">平台的软件。</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "2019-06-03"))

