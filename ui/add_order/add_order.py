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
        AddForm.resize(1190, 710)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        AddForm.setFont(font)
        AddForm.setStyleSheet(u"/* \u041e\u0431\u0449\u0438\u0435 \u0441\u0442\u0438\u043b\u0438 */\n"
"QWidget {\n"
"    background-color: #2d2d2d;\n"
"    color: #cccccc;\n"
"    font-family: Arial, sans-serif;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"/* \u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043a\u0438 */\n"
"QLabel#headerLabel {\n"
"    font-size: 32px;\n"
"    font-weight: bold;\n"
"    color: #66ccff;\n"
"}\n"
"\n"
"/* \u041a\u043d\u043e\u043f\u043a\u0438 */\n"
"QPushButton {\n"
"    background-color: #4a4a4a;\n"
"    color: #cccccc;\n"
"    border: none;\n"
"    padding: 10px 20px;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #666666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #333333;\n"
"}\n"
"\n"
"/* \u041f\u043e\u043b\u044f \u0432\u0432\u043e\u0434\u0430 */\n"
"QLineEdit, QTextEdit, QSpinBox, QDoubleSpinBox, QDateEdit {\n"
"    background-color: #333333;\n"
"    border: 1px solid #55555"
                        "5;\n"
"    padding: 5px;\n"
"    border-radius: 3px;\n"
"    color: #cccccc;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLineEdit:focus, QTextEdit:focus, QSpinBox:focus, QDoubleSpinBox:focus, QDateEdit:focus {\n"
"    border-color: #66ccff;\n"
"    outline: none;\n"
"}\n"
"\n"
"/* \u0422\u0430\u0431\u043b\u0438\u0446\u044b */\n"
"QTableView {\n"
"    background-color: #333333;\n"
"    border: 1px solid #555555;\n"
"    gridline-color: #555555;\n"
"    color: #cccccc;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #66ccff;\n"
"    color: #2d2d2d;\n"
"}\n"
"\n"
"/* \u041c\u0435\u043d\u044e */\n"
"QMenuBar {\n"
"    background-color: #2d2d2d;\n"
"    color: #cccccc;\n"
"    border-bottom: 1px solid #555555;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
" "
                        "   background-color: #66ccff;\n"
"    color: #2d2d2d;\n"
"}\n"
"\n"
"QMenu {\n"
"    background-color: #333333;\n"
"    border: 1px solid #555555;\n"
"    color: #cccccc;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QMenu::item {\n"
"    padding: 5px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background-color: #66ccff;\n"
"    color: #2d2d2d\n"
"}")
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
        self.type_comboBox.addItem("")
        self.type_comboBox.addItem("")
        self.type_comboBox.setObjectName(u"type_comboBox")

        self.horizontalLayout.addWidget(self.type_comboBox)

        self.add_type_pushButton = QPushButton(AddForm)
        self.add_type_pushButton.setObjectName(u"add_type_pushButton")

        self.horizontalLayout.addWidget(self.add_type_pushButton)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 1)

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

        self.add_city_pushButton = QPushButton(AddForm)
        self.add_city_pushButton.setObjectName(u"add_city_pushButton")

        self.verticalLayout.addWidget(self.add_city_pushButton)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(AddForm)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.city = QComboBox(AddForm)
        self.city.setObjectName(u"city")

        self.horizontalLayout_5.addWidget(self.city)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.scrollArea = QScrollArea(AddForm)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1170, 325))
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
        self.label.setText(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label_2.setText(QCoreApplication.translate("AddForm", u"\u0422\u0438\u043f:", None))
        self.type_comboBox.setItemText(0, QCoreApplication.translate("AddForm", u"\u0413\u0440\u0430\u0444\u0438\u0442\u0438", None))
        self.type_comboBox.setItemText(1, QCoreApplication.translate("AddForm", u"\u0411\u043e\u043b\u044c\u0448\u043e\u0435 \u0433\u0440\u0430\u0444\u0438\u0442\u0438", None))
        self.type_comboBox.setItemText(2, QCoreApplication.translate("AddForm", u"\u0427\u0442\u043e \u0443\u0433\u043e\u0434\u043d\u043e", None))
        self.type_comboBox.setItemText(3, QCoreApplication.translate("AddForm", u"\u041d\u0430\u043a\u043b\u0435\u0439\u043a\u0438", None))

        self.type_comboBox.setCurrentText("")
        self.type_comboBox.setPlaceholderText(QCoreApplication.translate("AddForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0438\u043f", None))
        self.add_type_pushButton.setText(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0438\u043f", None))
        self.label_3.setText(QCoreApplication.translate("AddForm", u"\u0417\u0430\u043a\u0430\u0437\u0447\u0438\u043a:", None))
        self.order_lineEdit.setPlaceholderText(QCoreApplication.translate("AddForm", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0438\u043c\u044f \u0437\u0430\u043a\u0430\u0437\u0447\u0438\u043a\u0430", None))
        self.label_4.setText(QCoreApplication.translate("AddForm", u"\u0413\u043e\u0440\u043e\u0434:", None))
        self.city_lineEdit.setPlaceholderText(QCoreApplication.translate("AddForm", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u0433\u043e\u0440\u043e\u0434", None))
        self.add_city_pushButton.setText(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0433\u043e\u0440\u043e\u0434", None))
        self.label_5.setText(QCoreApplication.translate("AddForm", u"\u0413\u043e\u0440\u043e\u0434\u0430:", None))
        self.city.setPlaceholderText(QCoreApplication.translate("AddForm", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442 \u0433\u043e\u0440\u043e\u0434 \u0434\u043b\u044f \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u0440\u0430\u0439\u043e\u043d\u0430", None))
        self.add_area_pushButton.setText(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0440\u0430\u0439\u043e\u043d", None))
        self.add_order_pushbutton.setText(QCoreApplication.translate("AddForm", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.status.setText(QCoreApplication.translate("AddForm", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0438", None))
    # retranslateUi

