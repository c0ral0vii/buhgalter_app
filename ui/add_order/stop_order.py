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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(490, 178)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        Form.setFont(font)
        Form.setStyleSheet(u"/* \u041e\u0431\u0449\u0438\u0435 \u0441\u0442\u0438\u043b\u0438 */\n"
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

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)


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
        self.label.setText(QCoreApplication.translate("Form", u"\u0418\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0435 \u0441\u0442\u0430\u0442\u0443\u0441\u0430", None))
    # retranslateUi

