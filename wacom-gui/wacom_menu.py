# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wacom_menu.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(900, 900)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 900))
        MainWindow.setMaximumSize(QSize(900, 900))
        MainWindow.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 0, 881, 301))
        self.controlLayout = QFormLayout(self.formLayoutWidget)
        self.controlLayout.setContentsMargins(4, 4, 4, 4)
        self.controlLayout.setObjectName(u"controlLayout")
        self.controlLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.controlLayout.setLabelAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.controlLayout.setHorizontalSpacing(4)
        self.controlLayout.setVerticalSpacing(4)
        self.controlLayout.setContentsMargins(0, 0, 0, 0)
        self.tabletLbl = QLabel(self.formLayoutWidget)
        self.tabletLbl.setObjectName(u"tabletLbl")
        self.tabletLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.controlLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.tabletLbl)

        self.toolLbl = QLabel(self.formLayoutWidget)
        self.toolLbl.setObjectName(u"toolLbl")
        self.toolLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.controlLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.toolLbl)

        self.toolScroll = QScrollArea(self.formLayoutWidget)
        self.toolScroll.setObjectName(u"toolScroll")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toolScroll.sizePolicy().hasHeightForWidth())
        self.toolScroll.setSizePolicy(sizePolicy1)
        self.toolScroll.setMinimumSize(QSize(0, 90))
        self.toolScroll.setStyleSheet(u"QScrollBar:horizontal {\n"
"            border: none;\n"
"            background: none;\n"
"            height: 6px;\n"
"            margin: 0px 26px 0 26px;\n"
"        }\n"
"\n"
"        QScrollBar::handle:horizontal {\n"
"            background: rgb(90,90,90,90);\n"
"			border-width: 2px;\n"
"			border-radius: 2px;\n"
"			border-color: rgb(0,0,0,100);\n"
"            min-width: 6px;\n"
"			\n"
"        }\n"
"\n"
"        QScrollBar::add-line:horizontal {\n"
"            background: none;\n"
"            width: 6px;\n"
"            subcontrol-position: right;\n"
"            subcontrol-origin: margin;\n"
"            \n"
"        }\n"
"\n"
"        QScrollBar::sub-line:horizontal {\n"
"            background: none;\n"
"            width: 6px;\n"
"            subcontrol-position: top left;\n"
"            subcontrol-origin: margin;\n"
"            position: absolute;\n"
"        }")
        self.toolScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.toolScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 821, 86))
        self.toolScroll.setWidget(self.scrollAreaWidgetContents_2)

        self.controlLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.toolScroll)

        self.configLbl = QLabel(self.formLayoutWidget)
        self.configLbl.setObjectName(u"configLbl")
        self.configLbl.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.controlLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.configLbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tabletScroll = QScrollArea(self.formLayoutWidget)
        self.tabletScroll.setObjectName(u"tabletScroll")
        sizePolicy1.setHeightForWidth(self.tabletScroll.sizePolicy().hasHeightForWidth())
        self.tabletScroll.setSizePolicy(sizePolicy1)
        self.tabletScroll.setMinimumSize(QSize(0, 100))
        self.tabletScroll.setMaximumSize(QSize(780, 16777215))
        self.tabletScroll.setAutoFillBackground(False)
        self.tabletScroll.setStyleSheet(u"QScrollBar:horizontal {\n"
"            border: none;\n"
"            background: none;\n"
"            height: 6px;\n"
"            margin: 0px 26px 0 26px;\n"
"        }\n"
"\n"
"        QScrollBar::handle:horizontal {\n"
"            background: rgb(90,90,90,90);\n"
"			border-width: 2px;\n"
"			border-radius: 2px;\n"
"			border-color: rgb(0,0,0,100);\n"
"            min-width: 6px;\n"
"			\n"
"        }\n"
"\n"
"        QScrollBar::add-line:horizontal {\n"
"            background: none;\n"
"            width: 6px;\n"
"            subcontrol-position: right;\n"
"            subcontrol-origin: margin;\n"
"            \n"
"        }\n"
"\n"
"        QScrollBar::sub-line:horizontal {\n"
"            background: none;\n"
"            width: 6px;\n"
"            subcontrol-position: top left;\n"
"            subcontrol-origin: margin;\n"
"            position: absolute;\n"
"        }")
        self.tabletScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tabletScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tabletScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 776, 96))
        self.tabletScroll.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout.addWidget(self.tabletScroll)

        self.tabletRefresh = QPushButton(self.formLayoutWidget)
        self.tabletRefresh.setObjectName(u"tabletRefresh")
        self.tabletRefresh.setMaximumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.tabletRefresh)


        self.controlLayout.setLayout(0, QFormLayout.ItemRole.FieldRole, self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.configScroll = QScrollArea(self.formLayoutWidget)
        self.configScroll.setObjectName(u"configScroll")
        sizePolicy1.setHeightForWidth(self.configScroll.sizePolicy().hasHeightForWidth())
        self.configScroll.setSizePolicy(sizePolicy1)
        self.configScroll.setMinimumSize(QSize(0, 90))
        self.configScroll.setMaximumSize(QSize(740, 80))
        self.configScroll.setStyleSheet(u"QScrollBar:horizontal {\n"
"            border: none;\n"
"            background: none;\n"
"            height: 6px;\n"
"            margin: 0px 26px 0 26px;\n"
"        }\n"
"\n"
"        QScrollBar::handle:horizontal {\n"
"            background: rgb(90,90,90,90);\n"
"			border-width: 2px;\n"
"			border-radius: 2px;\n"
"			border-color: rgb(0,0,0,100);\n"
"            min-width: 6px;\n"
"			\n"
"        }\n"
"\n"
"        QScrollBar::add-line:horizontal {\n"
"            background: none;\n"
"            width: 6px;\n"
"            subcontrol-position: right;\n"
"            subcontrol-origin: margin;\n"
"            \n"
"        }\n"
"\n"
"        QScrollBar::sub-line:horizontal {\n"
"            background: none;\n"
"            width: 6px;\n"
"            subcontrol-position: top left;\n"
"            subcontrol-origin: margin;\n"
"            position: absolute;\n"
"        }")
        self.configScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.configScroll.setWidgetResizable(True)
        self.configScroll.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 725, 86))
        self.configScroll.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_2.addWidget(self.configScroll)

        self.configControls = QVBoxLayout()
        self.configControls.setSpacing(0)
        self.configControls.setObjectName(u"configControls")
        self.addConfig = QPushButton(self.formLayoutWidget)
        self.addConfig.setObjectName(u"addConfig")
        self.addConfig.setEnabled(False)
        self.addConfig.setMaximumSize(QSize(30, 30))

        self.configControls.addWidget(self.addConfig)

        self.removeConfig = QPushButton(self.formLayoutWidget)
        self.removeConfig.setObjectName(u"removeConfig")
        self.removeConfig.setEnabled(False)
        self.removeConfig.setMaximumSize(QSize(30, 30))

        self.configControls.addWidget(self.removeConfig)

        self.saveConfig = QPushButton(self.formLayoutWidget)
        self.saveConfig.setObjectName(u"saveConfig")

        self.configControls.addWidget(self.saveConfig)


        self.horizontalLayout_2.addLayout(self.configControls)


        self.controlLayout.setLayout(2, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)

        self.controlBox = QGroupBox(self.centralwidget)
        self.controlBox.setObjectName(u"controlBox")
        self.controlBox.setGeometry(QRect(10, 310, 880, 540))
        self.controlBox.setMinimumSize(QSize(880, 540))
        self.controlBox.setMaximumSize(QSize(880, 540))
        self.controlBox.setStyleSheet(u"")
        self.aboutButton = QPushButton(self.centralwidget)
        self.aboutButton.setObjectName(u"aboutButton")
        self.aboutButton.setGeometry(QRect(770, 860, 90, 20))
        sizePolicy.setHeightForWidth(self.aboutButton.sizePolicy().hasHeightForWidth())
        self.aboutButton.setSizePolicy(sizePolicy)
        self.helpButton = QPushButton(self.centralwidget)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setGeometry(QRect(870, 860, 20, 20))
        sizePolicy.setHeightForWidth(self.helpButton.sizePolicy().hasHeightForWidth())
        self.helpButton.setSizePolicy(sizePolicy)
        self.helpButton.setStyleSheet(u"border-radius: 10px;\n"
"border-style: inset;\n"
"border-width: 1px;\n"
"")
        self.deviceDefaults = QPushButton(self.centralwidget)
        self.deviceDefaults.setObjectName(u"deviceDefaults")
        self.deviceDefaults.setGeometry(QRect(650, 860, 111, 20))
        sizePolicy.setHeightForWidth(self.deviceDefaults.sizePolicy().hasHeightForWidth())
        self.deviceDefaults.setSizePolicy(sizePolicy)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 900, 20))
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Wacom GUI", None))
        self.tabletLbl.setText(QCoreApplication.translate("MainWindow", u"Tablet:", None))
        self.toolLbl.setText(QCoreApplication.translate("MainWindow", u"Tool:", None))
        self.configLbl.setText(QCoreApplication.translate("MainWindow", u"Config:", None))
        self.tabletRefresh.setText("")
        self.addConfig.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.removeConfig.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.saveConfig.setText(QCoreApplication.translate("MainWindow", u"Save Config", None))
        self.controlBox.setTitle("")
        self.aboutButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.helpButton.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.deviceDefaults.setText(QCoreApplication.translate("MainWindow", u"Restore Defaults", None))
    # retranslateUi

