# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'keystroke.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(625, 139)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 601, 121))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.keystrokesLabel = QLabel(self.formLayoutWidget)
        self.keystrokesLabel.setObjectName(u"keystrokesLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.keystrokesLabel)

        self.keystrokeinput = QLineEdit(self.formLayoutWidget)
        self.keystrokeinput.setObjectName(u"keystrokeinput")
        self.keystrokeinput.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.keystrokeinput)

        self.shortcutLabel = QLabel(self.formLayoutWidget)
        self.shortcutLabel.setObjectName(u"shortcutLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.shortcutLabel)

        self.shortcutinput = QLineEdit(self.formLayoutWidget)
        self.shortcutinput.setObjectName(u"shortcutinput")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.shortcutinput)

        self.runLabel = QLabel(self.formLayoutWidget)
        self.runLabel.setObjectName(u"runLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.runLabel)

        self.runinput = QLineEdit(self.formLayoutWidget)
        self.runinput.setObjectName(u"runinput")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.runinput)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.keystroke = QPushButton(self.formLayoutWidget)
        self.keystroke.setObjectName(u"keystroke")
        self.keystroke.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.keystroke)

        self.buttonBox = QDialogButtonBox(self.formLayoutWidget)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_2.addWidget(self.buttonBox)


        self.formLayout.setLayout(3, QFormLayout.ItemRole.FieldRole, self.horizontalLayout_2)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.keystrokesLabel.setText(QCoreApplication.translate("Dialog", u"Keystrokes", None))
        self.shortcutLabel.setText(QCoreApplication.translate("Dialog", u"Shortcut Name", None))
        self.runLabel.setText(QCoreApplication.translate("Dialog", u"Run Command", None))
        self.keystroke.setText(QCoreApplication.translate("Dialog", u"Keystroke...", None))
    # retranslateUi

