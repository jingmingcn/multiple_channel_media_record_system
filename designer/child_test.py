# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'child_test.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 310)
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 381, 261))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 371, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.tab1_combobox = QtWidgets.QComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_combobox.sizePolicy().hasHeightForWidth())
        self.tab1_combobox.setSizePolicy(sizePolicy)
        self.tab1_combobox.setObjectName("tab1_combobox")
        self.horizontalLayout.addWidget(self.tab1_combobox)
        spacerItem2 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tab1_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_label.sizePolicy().hasHeightForWidth())
        self.tab1_label.setSizePolicy(sizePolicy)
        self.tab1_label.setMinimumSize(QtCore.QSize(256, 144))
        self.tab1_label.setMaximumSize(QtCore.QSize(256, 144))
        self.tab1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tab1_label.setObjectName("tab1_label")
        self.verticalLayout_2.addWidget(self.tab1_label)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.layoutWidget_2.setGeometry(QtCore.QRect(0, 10, 371, 211))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem6 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.tab1_combobox_3 = QtWidgets.QComboBox(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_combobox_3.sizePolicy().hasHeightForWidth())
        self.tab1_combobox_3.setSizePolicy(sizePolicy)
        self.tab1_combobox_3.setObjectName("tab1_combobox_3")
        self.horizontalLayout_8.addWidget(self.tab1_combobox_3)
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_8)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem8)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.tab1_label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_label_3.sizePolicy().hasHeightForWidth())
        self.tab1_label_3.setSizePolicy(sizePolicy)
        self.tab1_label_3.setMinimumSize(QtCore.QSize(256, 144))
        self.tab1_label_3.setMaximumSize(QtCore.QSize(256, 144))
        self.tab1_label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.tab1_label_3.setObjectName("tab1_label_3")
        self.verticalLayout_5.addWidget(self.tab1_label_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget_3.setGeometry(QtCore.QRect(0, 10, 371, 211))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem11 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem11)
        self.tab1_combobox_4 = QtWidgets.QComboBox(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_combobox_4.sizePolicy().hasHeightForWidth())
        self.tab1_combobox_4.setSizePolicy(sizePolicy)
        self.tab1_combobox_4.setObjectName("tab1_combobox_4")
        self.horizontalLayout_9.addWidget(self.tab1_combobox_4)
        spacerItem12 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem12)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_8.addItem(spacerItem13)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.tab1_label_4 = QtWidgets.QLabel(self.layoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_label_4.sizePolicy().hasHeightForWidth())
        self.tab1_label_4.setSizePolicy(sizePolicy)
        self.tab1_label_4.setMinimumSize(QtCore.QSize(256, 144))
        self.tab1_label_4.setMaximumSize(QtCore.QSize(256, 144))
        self.tab1_label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.tab1_label_4.setObjectName("tab1_label_4")
        self.verticalLayout_7.addWidget(self.tab1_label_4)
        self.horizontalLayout_4.addLayout(self.verticalLayout_7)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(0, 10, 371, 211))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem15 = QtWidgets.QSpacerItem(40, 40, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem15)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem16 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem16)
        self.tab1_combobox_7 = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab1_combobox_7.sizePolicy().hasHeightForWidth())
        self.tab1_combobox_7.setSizePolicy(sizePolicy)
        self.tab1_combobox_7.setMinimumSize(QtCore.QSize(160, 0))
        self.tab1_combobox_7.setObjectName("tab1_combobox_7")
        self.horizontalLayout_14.addWidget(self.tab1_combobox_7)
        spacerItem17 = QtWidgets.QSpacerItem(31, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem17)
        self.verticalLayout_14.addLayout(self.horizontalLayout_14)
        spacerItem18 = QtWidgets.QSpacerItem(256, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_14.addItem(spacerItem18)
        self.verticalLayout_13.addLayout(self.verticalLayout_14)
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget1)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_13.addWidget(self.progressBar)
        spacerItem19 = QtWidgets.QSpacerItem(40, 60, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_13.addItem(spacerItem19)
        self.horizontalLayout_13.addLayout(self.verticalLayout_13)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem20)
        self.tabWidget.addTab(self.tab_4, "")
        self.OK = QtWidgets.QPushButton(Form)
        self.OK.setGeometry(QtCore.QRect(260, 280, 111, 23))
        self.OK.setObjectName("OK")

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.tab1_label.setText(_translate("Form", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "行为"))
        self.tab1_label_3.setText(_translate("Form", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "面部"))
        self.tab1_label_4.setText(_translate("Form", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "眼睛"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "麦克风"))
        self.OK.setText(_translate("Form", "确认"))

