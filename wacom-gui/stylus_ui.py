# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stylus_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_StylusWidget(object):
    def setupUi(self, StylusWidget):
        if not StylusWidget.objectName():
            StylusWidget.setObjectName(u"StylusWidget")
        StylusWidget.resize(840, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(StylusWidget.sizePolicy().hasHeightForWidth())
        StylusWidget.setSizePolicy(sizePolicy)
        StylusWidget.setMinimumSize(QSize(840, 520))
        StylusWidget.setMaximumSize(QSize(840, 520))
        StylusWidget.setStyleSheet(u"QTabBar::tab:selected {\n"
"                                    border-bottom: 3px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6DD7E8);\n"
"                                }\n"
"                                QTabBar::tab {\n"
"                                    padding: 5px 15px 3px 15px;\n"
"                                    margin-top: 10px;\n"
"                                    color: #080808;\n"
"                                    border-radius: 4px;\n"
"                                }\n"
"QProgressBar {\n"
"border: 1px solid black;\n"
"text-align: top;\n"
"padding: 1px;\n"
"border-radius: 2px;\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #fff,\n"
"stop: 0.4999 #eee,\n"
"stop: 0.5 #ddd,\n"
"stop: 1 #eee );\n"
"width: 15px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"stop: 0 #a2e7f2,\n"
"stop: 0.4999 #6DD7E8,\n"
"stop: 0.5 #58aebc,\n"
"stop: 1 #213f44 );\n"
"border-radius: 1px;\n"
"border: 1px solid bla"
                        "ck;\n"
"}\n"
"border-style: none;\n"
"border-width: 0px;")
        self.keys = QWidget()
        self.keys.setObjectName(u"keys")
        self.penImage = QLabel(self.keys)
        self.penImage.setObjectName(u"penImage")
        self.penImage.setGeometry(QRect(390, 20, 106, 440))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.penImage.sizePolicy().hasHeightForWidth())
        self.penImage.setSizePolicy(sizePolicy1)
        self.penImage.setMinimumSize(QSize(106, 440))
        self.penImage.setMaximumSize(QSize(106, 440))
        self.verticalLayoutWidget_4 = QWidget(self.keys)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 20, 321, 451))
        self.penToolLeft = QVBoxLayout(self.verticalLayoutWidget_4)
        self.penToolLeft.setSpacing(0)
        self.penToolLeft.setObjectName(u"penToolLeft")
        self.penToolLeft.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_5 = QWidget(self.keys)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(520, 20, 311, 421))
        self.penToolRight = QVBoxLayout(self.verticalLayoutWidget_5)
        self.penToolRight.setSpacing(0)
        self.penToolRight.setObjectName(u"penToolRight")
        self.penToolRight.setContentsMargins(0, 0, 0, 0)
        self.penDefault = QPushButton(self.keys)
        self.penDefault.setObjectName(u"penDefault")
        self.penDefault.setGeometry(QRect(740, 450, 84, 25))
        StylusWidget.addTab(self.keys, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.eraserImage = QLabel(self.tab)
        self.eraserImage.setObjectName(u"eraserImage")
        self.eraserImage.setGeometry(QRect(390, 20, 106, 440))
        sizePolicy1.setHeightForWidth(self.eraserImage.sizePolicy().hasHeightForWidth())
        self.eraserImage.setSizePolicy(sizePolicy1)
        self.eraserImage.setMinimumSize(QSize(106, 440))
        self.eraserImage.setMaximumSize(QSize(106, 440))
        self.verticalLayoutWidget_6 = QWidget(self.tab)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(0, 20, 311, 451))
        self.eraserToolLeft = QVBoxLayout(self.verticalLayoutWidget_6)
        self.eraserToolLeft.setSpacing(0)
        self.eraserToolLeft.setObjectName(u"eraserToolLeft")
        self.eraserToolLeft.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutWidget_7 = QWidget(self.tab)
        self.verticalLayoutWidget_7.setObjectName(u"verticalLayoutWidget_7")
        self.verticalLayoutWidget_7.setGeometry(QRect(520, 20, 311, 421))
        self.eraserToolRight = QVBoxLayout(self.verticalLayoutWidget_7)
        self.eraserToolRight.setSpacing(0)
        self.eraserToolRight.setObjectName(u"eraserToolRight")
        self.eraserToolRight.setContentsMargins(0, 0, 0, 0)
        self.eraserDefault = QPushButton(self.tab)
        self.eraserDefault.setObjectName(u"eraserDefault")
        self.eraserDefault.setGeometry(QRect(740, 450, 84, 25))
        StylusWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayoutWidget_8 = QWidget(self.tab_2)
        self.verticalLayoutWidget_8.setObjectName(u"verticalLayoutWidget_8")
        self.verticalLayoutWidget_8.setGeometry(QRect(520, 20, 311, 421))
        self.mappingToolRight = QVBoxLayout(self.verticalLayoutWidget_8)
        self.mappingToolRight.setSpacing(0)
        self.mappingToolRight.setObjectName(u"mappingToolRight")
        self.mappingToolRight.setContentsMargins(0, 0, 0, 0)
        self.mappingImage = QLabel(self.tab_2)
        self.mappingImage.setObjectName(u"mappingImage")
        self.mappingImage.setGeometry(QRect(40, 20, 340, 440))
        sizePolicy1.setHeightForWidth(self.mappingImage.sizePolicy().hasHeightForWidth())
        self.mappingImage.setSizePolicy(sizePolicy1)
        self.mappingImage.setMinimumSize(QSize(340, 440))
        self.mappingImage.setMaximumSize(QSize(340, 440))
        self.mappingDefault = QPushButton(self.tab_2)
        self.mappingDefault.setObjectName(u"mappingDefault")
        self.mappingDefault.setGeometry(QRect(740, 450, 84, 25))
        StylusWidget.addTab(self.tab_2, "")

        self.retranslateUi(StylusWidget)

        StylusWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(StylusWidget)
    # setupUi

    def retranslateUi(self, StylusWidget):
        StylusWidget.setWindowTitle(QCoreApplication.translate("StylusWidget", u"TabWidget", None))
        self.penImage.setText(QCoreApplication.translate("StylusWidget", u"TextLabel", None))
        self.penDefault.setText(QCoreApplication.translate("StylusWidget", u"Default", None))
        StylusWidget.setTabText(StylusWidget.indexOf(self.keys), QCoreApplication.translate("StylusWidget", u"Pen", None))
        self.eraserImage.setText(QCoreApplication.translate("StylusWidget", u"TextLabel", None))
        self.eraserDefault.setText(QCoreApplication.translate("StylusWidget", u"Default", None))
        StylusWidget.setTabText(StylusWidget.indexOf(self.tab), QCoreApplication.translate("StylusWidget", u"Eraser", None))
        self.mappingImage.setText(QCoreApplication.translate("StylusWidget", u"TextLabel", None))
        self.mappingDefault.setText(QCoreApplication.translate("StylusWidget", u"Default", None))
        StylusWidget.setTabText(StylusWidget.indexOf(self.tab_2), QCoreApplication.translate("StylusWidget", u"Mapping", None))
    # retranslateUi

