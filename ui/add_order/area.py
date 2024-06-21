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
        area_form.resize(767, 161)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        area_form.setFont(font)
        area_form.setStyleSheet(u"/* \u041e\u0431\u0449\u0438\u0435 \u0441\u0442\u0438\u043b\u0438 */\n"
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
        self.verticalLayout = QVBoxLayout(area_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(area_form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(100, 100))
        self.groupBox.setFont(font)
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

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.limit_lineEdit = QLineEdit(self.groupBox)
        self.limit_lineEdit.setObjectName(u"limit_lineEdit")
        self.limit_lineEdit.setMinimumSize(QSize(0, 1))

        self.horizontalLayout.addWidget(self.limit_lineEdit)

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
        self.label_6.setText(QCoreApplication.translate("area_form", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e", None))
        self.count_lineEdit.setText("")
        self.count_lineEdit.setPlaceholderText(QCoreApplication.translate("area_form", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_7.setText(QCoreApplication.translate("area_form", u"\u041b\u0438\u043c\u0438\u0442", None))
        self.limit_lineEdit.setText("")
        self.limit_lineEdit.setPlaceholderText(QCoreApplication.translate("area_form", u"\u0423\u043a\u0430\u0436\u0438\u0442\u0435 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.delete_area_pushButton.setText(QCoreApplication.translate("area_form", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

