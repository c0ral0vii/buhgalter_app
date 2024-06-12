# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stop_order.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(490, 178)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        Form.setFont(font)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pause_comboBox = QComboBox(Form)
        self.pause_comboBox.addItem("")
        self.pause_comboBox.addItem("")
        self.pause_comboBox.addItem("")
        self.pause_comboBox.addItem("")
        self.pause_comboBox.setObjectName(u"pause_comboBox")
        self.pause_comboBox.setMinimumSize(QSize(6, 0))

        self.horizontalLayout.addWidget(self.pause_comboBox)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.plainTextEdit = QLineEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 1, 0, 1, 1)


        self.retranslateUi(Form)

        self.pause_comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0413\u043e\u0442\u043e\u0432\u043e", None))
        self.pause_comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u041f\u0430\u0443\u0437\u0430", None))
        self.pause_comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u0412\u044b\u043f\u043e\u043b\u043d\u044f\u0435\u0442\u0441\u044f", None))
        self.pause_comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u0412 \u0430\u0440\u0445\u0438\u0432\u0435", None))
        self.pause_comboBox.setItemText(3, QCoreApplication.translate("Form", u"\u0421\u0442\u043e\u043f", None))

        self.pause_comboBox.setPlaceholderText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441", None))
        self.plainTextEdit.setText("")
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"\u041a\u043e\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439", None))
    # retranslateUi

