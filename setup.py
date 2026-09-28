from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import json
import ctypes


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 218)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 170, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.webhook_url_line = QtWidgets.QLineEdit(Dialog)
        self.webhook_url_line.setGeometry(QtCore.QRect(30, 40, 341, 20))
        self.webhook_url_line.setObjectName("webhook_url_line")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 81, 16))
        self.label_2.setObjectName("label_2")
        self.message_id_line = QtWidgets.QLineEdit(Dialog)
        self.message_id_line.setGeometry(QtCore.QRect(30, 120, 341, 20))
        self.message_id_line.setObjectName("message_id_line")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Webhook URL"))
        self.label_2.setText(_translate("Dialog", "Message ID"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    result = Dialog.exec_()

    if result == QtWidgets.QDialog.Accepted:
        config = {
            "webhook_url": ui.webhook_url_line.text(),
            "message_id": ui.message_id_line.text()
        }

        if config["webhook_url"].startswith("https://discord.com/api/webhooks/") and config["message_id"].isdigit():
            with open("config.json", "w") as file:
                json.dump(config, file, indent=4)
        else:
            ctypes.windll.user32.MessageBoxW(
            0,
            "Invalid input",
            "Setup error",
            0x30
        )

    app.quit()
    sys.exit(0)
