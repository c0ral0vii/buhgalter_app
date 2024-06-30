# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pageui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1373, 733)
        MainWindow.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"/* \u041e\u0431\u0449\u0438\u0435 \u0441\u0442\u0438\u043b\u0438 */\n"
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.all_orders_pushButton = QPushButton(self.centralwidget)
        self.all_orders_pushButton.setObjectName(u"all_orders_pushButton")

        self.horizontalLayout_3.addWidget(self.all_orders_pushButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.archive_button = QPushButton(self.centralwidget)
        self.archive_button.setObjectName(u"archive_button")

        self.horizontalLayout_2.addWidget(self.archive_button)

        self.order_limit_pushButton = QPushButton(self.centralwidget)
        self.order_limit_pushButton.setObjectName(u"order_limit_pushButton")

        self.horizontalLayout_2.addWidget(self.order_limit_pushButton)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setAutoFillBackground(False)
        self.tableView.setFrameShape(QFrame.Panel)
        self.tableView.setAutoScrollMargin(10)
        self.tableView.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed|QAbstractItemView.SelectedClicked)
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.tableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_order_button = QPushButton(self.centralwidget)
        self.add_order_button.setObjectName(u"add_order_button")

        self.horizontalLayout.addWidget(self.add_order_button)

        self.stop_pushButton = QPushButton(self.centralwidget)
        self.stop_pushButton.setObjectName(u"stop_pushButton")

        self.horizontalLayout.addWidget(self.stop_pushButton)

        self.delete_order_button = QPushButton(self.centralwidget)
        self.delete_order_button.setObjectName(u"delete_order_button")

        self.horizontalLayout.addWidget(self.delete_order_button)

        self.add_types_pushButton = QPushButton(self.centralwidget)
        self.add_types_pushButton.setObjectName(u"add_types_pushButton")

        self.horizontalLayout.addWidget(self.add_types_pushButton)

        self.reload_button = QPushButton(self.centralwidget)
        self.reload_button.setObjectName(u"reload_button")

        self.horizontalLayout.addWidget(self.reload_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.status = QLabel(self.centralwidget)
        self.status.setObjectName(u"status")
        self.status.setFont(font)
        self.status.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.status)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0445\u0433\u0430\u043b\u0442\u0435\u0440\u0438\u044f", None))
        self.all_orders_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0435 \u0437\u0430\u043a\u0430\u0437\u044b", None))
        self.archive_button.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u0432", None))
        self.order_limit_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u0442\u043a\u0438", None))
        self.add_order_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        self.stop_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.delete_order_button.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437", None))
        self.add_types_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u0438\u043f\u044b", None))
        self.reload_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0442 \u0431\u0443\u0434\u0443\u0442 \u043e\u0442\u043e\u0431\u0440\u043e\u0436\u0430\u0442\u044c\u0441\u044f \u0432\u0430\u0448\u0438 \u0443\u0441\u043f\u0435\u0448\u043d\u044b\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f(\u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435, \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0438 \u0442.\u0434.)", None))
    # retranslateUi

