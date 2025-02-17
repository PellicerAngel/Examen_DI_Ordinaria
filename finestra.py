# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Finestra formulari.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(283, 152)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.LiniaNom = QLineEdit(Dialog)
        self.LiniaNom.setObjectName(u"LiniaNom")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.LiniaNom)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.LiniaContrassenya = QLineEdit(Dialog)
        self.LiniaContrassenya.setObjectName(u"LiniaContrassenya")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.LiniaContrassenya)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.LiniaROl = QComboBox(Dialog)
        self.LiniaROl.addItem("")
        self.LiniaROl.addItem("")
        self.LiniaROl.addItem("")
        self.LiniaROl.setObjectName(u"LiniaROl")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.LiniaROl)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Cancelar = QPushButton(Dialog)
        self.Cancelar.setObjectName(u"Cancelar")

        self.horizontalLayout.addWidget(self.Cancelar)

        self.OK = QPushButton(Dialog)
        self.OK.setObjectName(u"OK")

        self.horizontalLayout.addWidget(self.OK)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nom", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Contrassenya", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Rol", None))
        self.LiniaROl.setItemText(0, QCoreApplication.translate("Dialog", u"Admin", None))
        self.LiniaROl.setItemText(1, QCoreApplication.translate("Dialog", u"Usuari", None))
        self.LiniaROl.setItemText(2, QCoreApplication.translate("Dialog", u"Convidat", None))

        self.Cancelar.setText(QCoreApplication.translate("Dialog", u"Cancelar", None))
        self.OK.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

