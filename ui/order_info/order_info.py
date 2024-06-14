# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_info.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QScrollArea, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_CustomerWidget(object):
    def setupUi(self, CustomerWidget):
        if not CustomerWidget.objectName():
            CustomerWidget.setObjectName(u"CustomerWidget")
        CustomerWidget.resize(675, 471)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        CustomerWidget.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(CustomerWidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(CustomerWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.date_time_label = QLabel(CustomerWidget)
        self.date_time_label.setObjectName(u"date_time_label")

        self.horizontalLayout_5.addWidget(self.date_time_label)

        self.date_layer = QLabel(CustomerWidget)
        self.date_layer.setObjectName(u"date_layer")

        self.horizontalLayout_5.addWidget(self.date_layer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(CustomerWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.customer_lineEdit = QLineEdit(CustomerWidget)
        self.customer_lineEdit.setObjectName(u"customer_lineEdit")

        self.horizontalLayout.addWidget(self.customer_lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(CustomerWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.status_label = QLabel(CustomerWidget)
        self.status_label.setObjectName(u"status_label")

        self.horizontalLayout_2.addWidget(self.status_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(CustomerWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.type_label = QLabel(CustomerWidget)
        self.type_label.setObjectName(u"type_label")

        self.horizontalLayout_3.addWidget(self.type_label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(CustomerWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.city_lineEdit = QLineEdit(CustomerWidget)
        self.city_lineEdit.setObjectName(u"city_lineEdit")

        self.horizontalLayout_4.addWidget(self.city_lineEdit)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.scrollArea = QScrollArea(CustomerWidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 655, 214))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.verticalLayout_4.addLayout(self.verticalLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_3.addWidget(self.scrollArea)

        self.save_pushButton = QPushButton(CustomerWidget)
        self.save_pushButton.setObjectName(u"save_pushButton")

        self.verticalLayout_3.addWidget(self.save_pushButton)


        self.retranslateUi(CustomerWidget)

        QMetaObject.connectSlotsByName(CustomerWidget)
    # setupUi

    def retranslateUi(self, CustomerWidget):
        CustomerWidget.setWindowTitle(QCoreApplication.translate("CustomerWidget", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0437\u0430\u043a\u0430\u0437\u0435", None))
        self.label_5.setText(QCoreApplication.translate("CustomerWidget", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0437\u0430\u043a\u0430\u0437\u0435:", None))
        self.date_time_label.setText(QCoreApplication.translate("CustomerWidget", u"\u0414\u0430\u0442\u0430 -", None))
        self.date_layer.setText(QCoreApplication.translate("CustomerWidget", u"\u0434\u0430\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("CustomerWidget", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a:", None))
        self.customer_lineEdit.setText("")
        self.label_2.setText(QCoreApplication.translate("CustomerWidget", u"\u0421\u0442\u0430\u0442\u0443\u0441:", None))
        self.status_label.setText(QCoreApplication.translate("CustomerWidget", u"\u0421\u0442\u0430\u0443\u0442\u0441", None))
        self.label_3.setText(QCoreApplication.translate("CustomerWidget", u"\u0422\u0438\u043f", None))
        self.type_label.setText(QCoreApplication.translate("CustomerWidget", u"\u0422\u0438\u043f", None))
        self.label_4.setText(QCoreApplication.translate("CustomerWidget", u"\u0413\u043e\u0440\u043e\u0434:", None))
        self.save_pushButton.setText(QCoreApplication.translate("CustomerWidget", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

