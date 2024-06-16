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
        MainWindow.resize(954, 683)
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
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

        self.reload_button = QPushButton(self.centralwidget)
        self.reload_button.setObjectName(u"reload_button")

        self.horizontalLayout.addWidget(self.reload_button)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.status = QLabel(self.centralwidget)
        self.status.setObjectName(u"status")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.status.setFont(font1)
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
        self.reload_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0437\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0442 \u0431\u0443\u0434\u0443\u0442 \u043e\u0442\u043e\u0431\u0440\u043e\u0436\u0430\u0442\u044c\u0441\u044f \u0432\u0430\u0448\u0438 \u0443\u0441\u043f\u0435\u0448\u043d\u044b\u0435 \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u044f(\u0443\u0434\u0430\u043b\u0435\u043d\u0438\u0435, \u043e\u0431\u043d\u043e\u0432\u043b\u0435\u043d\u0438\u0435 \u0438 \u0442.\u0434.)", None))
    # retranslateUi

