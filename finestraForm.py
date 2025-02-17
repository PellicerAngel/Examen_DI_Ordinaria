from finestra import Ui_Dialog
import sys
from PySide6 import QtWidgets

class FinestraForm(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, name="", password="", role=""):
        super().__init__()
        self.setupUi(self)

        self.LiniaNom.setText(name)
        self.LiniaContrassenya.setText(password)
        self.LiniaROl.setEditText(role)


        self.OK.clicked.connect(self.accept)
        self.Cancelar.clicked.connect(self.close)

