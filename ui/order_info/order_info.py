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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTreeView, QVBoxLayout, QWidget)

class Ui_CustomerWidget(object):
    def setupUi(self, CustomerWidget):
        if not CustomerWidget.objectName():
            CustomerWidget.setObjectName(u"CustomerWidget")
        CustomerWidget.resize(1102, 678)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        CustomerWidget.setFont(font)
        CustomerWidget.setStyleSheet(u"/* \u041e\u0431\u0449\u0438\u0435 \u0441\u0442\u0438\u043b\u0438 */\n"
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
        self.verticalLayout = QVBoxLayout(CustomerWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(CustomerWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.date_time_label = QLabel(CustomerWidget)
        self.date_time_label.setObjectName(u"date_time_label")

        self.horizontalLayout_5.addWidget(self.date_time_label)

        self.date_layer = QLabel(CustomerWidget)
        self.date_layer.setObjectName(u"date_layer")

        self.horizontalLayout_5.addWidget(self.date_layer)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(CustomerWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.customer_lineEdit = QLineEdit(CustomerWidget)
        self.customer_lineEdit.setObjectName(u"customer_lineEdit")

        self.horizontalLayout.addWidget(self.customer_lineEdit)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(CustomerWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.status_label = QLabel(CustomerWidget)
        self.status_label.setObjectName(u"status_label")

        self.horizontalLayout_2.addWidget(self.status_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(CustomerWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.type_label = QLabel(CustomerWidget)
        self.type_label.setObjectName(u"type_label")

        self.horizontalLayout_3.addWidget(self.type_label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.cities_treeView = QTreeView(CustomerWidget)
        self.cities_treeView.setObjectName(u"cities_treeView")
        self.cities_treeView.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.cities_treeView.header().setMinimumSectionSize(300)

        self.verticalLayout.addWidget(self.cities_treeView)

        self.save_pushButton = QPushButton(CustomerWidget)
        self.save_pushButton.setObjectName(u"save_pushButton")

        self.verticalLayout.addWidget(self.save_pushButton)

        self.status = QLabel(CustomerWidget)
        self.status.setObjectName(u"status")
        self.status.setFont(font)
        self.status.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.status)


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
        self.save_pushButton.setText(QCoreApplication.translate("CustomerWidget", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.status.setText(QCoreApplication.translate("CustomerWidget", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e\u0431 \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u0438 \u0437\u0430\u043a\u0430\u0437\u0430", None))
    # retranslateUi

