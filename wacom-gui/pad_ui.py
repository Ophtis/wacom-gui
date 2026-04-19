# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pad_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QTabWidget,
    QWidget)

class Ui_PadWidget(object):
    def setupUi(self, PadWidget):
        if not PadWidget.objectName():
            PadWidget.setObjectName(u"PadWidget")
        PadWidget.resize(840, 520)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(PadWidget.sizePolicy().hasHeightForWidth())
        PadWidget.setSizePolicy(sizePolicy)
        PadWidget.setMinimumSize(QSize(840, 520))
        PadWidget.setMaximumSize(QSize(840, 520))
        PadWidget.setStyleSheet(u"QTabBar::tab:selected {\n"
"                                    border-bottom: 3px solid qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #6DD7E8);\n"
"                                }\n"
"                                QTabBar::tab {\n"
"                                    padding: 5px 15px 3px 15px;\n"
"                                    margin-top: 10px;\n"
"                                    color: #080808;\n"
"                                    border-top-left-radius: 4px;\n"
"                                    border-top-right-radius: 4px;\n"
"                                }\n"
"border-style: none;\n"
"border-width: 0px;")
        self.keys = QWidget()
        self.keys.setObjectName(u"keys")
        self.gridLayoutWidget = QWidget(self.keys)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 831, 481))
        self.keysLayout = QGridLayout(self.gridLayoutWidget)
        self.keysLayout.setObjectName(u"keysLayout")
        self.keysLayout.setContentsMargins(0, 0, 0, 0)
        PadWidget.addTab(self.keys, "")

        self.retranslateUi(PadWidget)

        PadWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PadWidget)
    # setupUi

    def retranslateUi(self, PadWidget):
        PadWidget.setWindowTitle(QCoreApplication.translate("PadWidget", u"TabWidget", None))
        PadWidget.setTabText(PadWidget.indexOf(self.keys), QCoreApplication.translate("PadWidget", u"Express Keys", None))
    # retranslateUi

