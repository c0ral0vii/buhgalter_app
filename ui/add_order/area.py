# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'area.ui'
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_area_form(object):
    def setupUi(self, area_form):
        if not area_form.objectName():
            area_form.setObjectName(u"area_form")
        area_form.resize(617, 161)
        font = QFont()
        font.setPointSize(16)
        area_form.setFont(font)
        self.verticalLayout = QVBoxLayout(area_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(area_form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(100, 100))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.groupBox.setFont(font1)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.area_lineEdit = QLineEdit(self.groupBox)
        self.area_lineEdit.setObjectName(u"area_lineEdit")

        self.horizontalLayout.addWidget(self.area_lineEdit)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.count_lineEdit = QLineEdit(self.groupBox)
        self.count_lineEdit.setObjectName(u"count_lineEdit")

        self.horizontalLayout.addWidget(self.count_lineEdit)

        self.delete_area_pushButton = QPushButton(self.groupBox)
        self.delete_area_pushButton.setObjectName(u"delete_area_pushButton")

        self.horizontalLayout.addWidget(self.delete_area_pushButton)


        self.verticalLayout.addWidget(self.groupBox)


        self.retranslateUi(area_form)

        QMetaObject.connectSlotsByName(area_form)
    # setupUi

    def retranslateUi(self, area_form):
        area_form.setWindowTitle(QCoreApplication.translate("area_form", u"Form", None))
        self.label_5.setText(QCoreApplication.translate("area_form", u"\u0420\u0430\u0439\u043e\u043d:", None))
        self.area_lineEdit.setPlaceholderText(QCoreApplication.translate("area_form", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0440\u0430\u0439\u043e\u043d(\u0435\u0441\u043b\u0438 \u0435\u0441\u0442\u044c)", None))
        self.label_6.setText(QCoreApplication.translate("area_form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.count_lineEdit.setText("")
        self.count_lineEdit.setPlaceholderText(QCoreApplication.translate("area_form", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.delete_area_pushButton.setText(QCoreApplication.translate("area_form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

