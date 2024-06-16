# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_order.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddForm(object):
    def setupUi(self, AddForm):
        if not AddForm.objectName():
            AddForm.setObjectName(u"AddForm")
        AddForm.resize(627, 421)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        AddForm.setFont(font)
        self.verticalLayout = QVBoxLayout(AddForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(AddForm)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(AddForm)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.type_comboBox = QComboBox(AddForm)
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.type_comboBox.setObjectName(u"type_comboBox")

        self.horizontalLayout.addWidget(self.type_comboBox)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(AddForm)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.order_lineEdit = QLineEdit(AddForm)
        self.order_lineEdit.setObjectName(u"order_lineEdit")

        self.horizontalLayout_2.addWidget(self.order_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(AddForm)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.city_lineEdit = QLineEdit(AddForm)
        self.city_lineEdit.setObjectName(u"city_lineEdit")

        self.horizontalLayout_3.addWidget(self.city_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.scrollArea = QScrollArea(AddForm)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 607, 98))
        self.horizontalLayout_4 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetFixedSize)

        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.scrollArea)

        self.add_area_pushButton = QPushButton(AddForm)
        self.add_area_pushButton.setObjectName(u"add_area_pushButton")

        self.verticalLayout.addWidget(self.add_area_pushButton)

        self.add_order_pushbutton = QPushButton(AddForm)
        self.add_order_pushbutton.setObjectName(u"add_order_pushbutton")

        self.verticalLayout.addWidget(self.add_order_pushbutton)

        self.status = QLabel(AddForm)
        self.status.setObjectName(u"status")
        self.status.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.status)


        self.retranslateUi(AddForm)

        self.type_comboBox.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(AddForm)
    # setupUi

    def retranslateUi(self, AddForm):
        AddForm.setWindowTitle(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label.setText(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430", None))
        self.label_2.setText(QCoreApplication.translate("AddForm", u"\u0422\u0438\u043f:", None))
        self.type_comboBox.setItemText(0, QCoreApplication.translate("AddForm", u"\u0413\u0440\u0430\u0444\u0438\u0442\u0438", None))
        self.type_comboBox.setItemText(1, QCoreApplication.translate("AddForm", u"\u041d\u0430\u043a\u043b\u0435\u0439\u043a\u0438", None))

        self.type_comboBox.setCurrentText("")
        self.type_comboBox.setPlaceholderText(QCoreApplication.translate("AddForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f", None))
        self.label_3.setText(QCoreApplication.translate("AddForm", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a:", None))
        self.order_lineEdit.setPlaceholderText(QCoreApplication.translate("AddForm", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0438\u043c\u044f \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("AddForm", u"\u0413\u043e\u0440\u043e\u0434:", None))
        self.city_lineEdit.setPlaceholderText(QCoreApplication.translate("AddForm", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0433\u043e\u0440\u043e\u0434", None))
        self.add_area_pushButton.setText(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0439\u043e\u043d", None))
        self.add_order_pushbutton.setText(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.status.setText(QCoreApplication.translate("AddForm", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0438", None))
    # retranslateUi

