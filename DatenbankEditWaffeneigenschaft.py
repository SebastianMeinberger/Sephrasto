# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatenbankEditWaffeneigenschaft.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_waffeneigenschaftDialog(object):
    def setupUi(self, waffeneigenschaftDialog):
        waffeneigenschaftDialog.setObjectName("waffeneigenschaftDialog")
        waffeneigenschaftDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        waffeneigenschaftDialog.resize(440, 200)
        self.gridLayout_2 = QtWidgets.QGridLayout(waffeneigenschaftDialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_5 = QtWidgets.QLabel(waffeneigenschaftDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.textEdit = QtWidgets.QPlainTextEdit(waffeneigenschaftDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(waffeneigenschaftDialog)
        self.label_4.setMinimumSize(QtCore.QSize(110, 0))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.scriptPrioEdit = QtWidgets.QSpinBox(waffeneigenschaftDialog)
        self.scriptPrioEdit.setMinimum(-10)
        self.scriptPrioEdit.setMaximum(10)
        self.scriptPrioEdit.setSingleStep(1)
        self.scriptPrioEdit.setProperty("value", 0)
        self.scriptPrioEdit.setObjectName("scriptPrioEdit")
        self.horizontalLayout.addWidget(self.scriptPrioEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(waffeneigenschaftDialog)
        self.label_3.setMinimumSize(QtCore.QSize(110, 0))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.scriptEdit = QtWidgets.QLineEdit(waffeneigenschaftDialog)
        self.scriptEdit.setObjectName("scriptEdit")
        self.gridLayout.addWidget(self.scriptEdit, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(waffeneigenschaftDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(waffeneigenschaftDialog)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 1, 1, 1, 1)
        self.warning = QtWidgets.QLabel(waffeneigenschaftDialog)
        self.warning.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.warning.setWordWrap(True)
        self.warning.setVisible(False)
        self.warning.setObjectName("warning")
        self.gridLayout.addWidget(self.warning, 0, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(waffeneigenschaftDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_2.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(waffeneigenschaftDialog)
        self.buttonBox.accepted.connect(waffeneigenschaftDialog.accept)
        self.buttonBox.rejected.connect(waffeneigenschaftDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(waffeneigenschaftDialog)
        waffeneigenschaftDialog.setTabOrder(self.nameEdit, self.textEdit)
        waffeneigenschaftDialog.setTabOrder(self.textEdit, self.scriptPrioEdit)
        waffeneigenschaftDialog.setTabOrder(self.scriptPrioEdit, self.scriptEdit)

    def retranslateUi(self, waffeneigenschaftDialog):
        _translate = QtCore.QCoreApplication.translate
        waffeneigenschaftDialog.setWindowTitle(_translate("waffeneigenschaftDialog", "Sephrasto - Waffeneigenschaft bearbeiten..."))
        self.label_5.setText(_translate("waffeneigenschaftDialog", "Beschreibung"))
        self.label_4.setText(_translate("waffeneigenschaftDialog", "Script Priorität"))
        self.label_3.setText(_translate("waffeneigenschaftDialog", "Script"))
        self.label.setText(_translate("waffeneigenschaftDialog", "Name"))
        self.warning.setText(_translate("waffeneigenschaftDialog", "Dies ist eine Ilaris-Standardwaffeneigenschaft. Sobald du hier etwas veränderst, bekommst du eine persönliche Kopie und das Original wird in der aktuellen User-Regelbasis gelöscht. Damit erhältst du für diese Waffeneigenschaft keine automatischen Updates mehr mit neuen Sephrasto-Versionen."))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    waffeneigenschaftDialog = QtWidgets.QDialog()
    ui = Ui_waffeneigenschaftDialog()
    ui.setupUi(waffeneigenschaftDialog)
    waffeneigenschaftDialog.show()
    sys.exit(app.exec_())
