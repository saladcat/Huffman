# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1069, 719)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 30, 311, 181))
        self.groupBox.setObjectName("groupBox")
        self.pb_encode = QtWidgets.QPushButton(self.groupBox)
        self.pb_encode.setGeometry(QtCore.QRect(180, 50, 113, 32))
        self.pb_encode.setObjectName("pb_encode")
        self.pte_encode = QtWidgets.QPlainTextEdit(self.groupBox)
        self.pte_encode.setGeometry(QtCore.QRect(10, 30, 171, 141))
        self.pte_encode.setObjectName("pte_encode")
        self.pb_reset = QtWidgets.QPushButton(self.groupBox)
        self.pb_reset.setGeometry(QtCore.QRect(180, 120, 113, 32))
        self.pb_reset.setObjectName("pb_reset")
        self.groupBox_4 = QtWidgets.QGroupBox(Form)
        self.groupBox_4.setGeometry(QtCore.QRect(340, 40, 681, 641))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 220, 311, 471))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pte_decode_input = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pte_decode_input.setGeometry(QtCore.QRect(10, 40, 281, 41))
        self.pte_decode_input.setObjectName("pte_decode_input")
        self.pb_decode = QtWidgets.QPushButton(self.groupBox_3)
        self.pb_decode.setGeometry(QtCore.QRect(90, 100, 113, 32))
        self.pb_decode.setObjectName("pb_decode")
        self.pte_decode_output = QtWidgets.QPlainTextEdit(self.groupBox_3)
        self.pte_decode_output.setGeometry(QtCore.QRect(10, 140, 281, 51))
        self.pte_decode_output.setObjectName("pte_decode_output")
        self.tw_encode_table = QtWidgets.QTableWidget(self.groupBox_3)
        self.tw_encode_table.setGeometry(QtCore.QRect(40, 210, 211, 241))
        self.tw_encode_table.setObjectName("tw_encode_table")
        self.tw_encode_table.setColumnCount(2)
        self.tw_encode_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tw_encode_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tw_encode_table.setHorizontalHeaderItem(1, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "init encode string"))
        self.pb_encode.setText(_translate("Form", "encode"))
        self.pb_reset.setText(_translate("Form", "reset"))
        self.groupBox_4.setTitle(_translate("Form", "encode table"))
        self.groupBox_3.setTitle(_translate("Form", "decode string"))
        self.pb_decode.setText(_translate("Form", "PushButton"))
        item = self.tw_encode_table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "key"))
        item = self.tw_encode_table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "code"))

