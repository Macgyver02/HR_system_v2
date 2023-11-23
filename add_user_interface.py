# add_user_interface.py
from PyQt5 import QtCore, QtGui, QtWidgets
import database
import hashlib

class Ui_AddUserWindow(object):
    def setupUi(self, AddUserWindow):
        AddUserWindow.setObjectName("AddUserWindow")
        AddUserWindow.resize(400, 300)
        AddUserWindow.setMinimumSize(QtCore.QSize(400, 300))
        AddUserWindow.setMaximumSize(QtCore.QSize(400, 300))
        self.centralwidget = QtWidgets.QWidget(AddUserWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.label.setText("Add User")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.label)

        self.staffNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.staffNumberLabel.setObjectName("staffNumberLabel")
        self.staffNumberLabel.setText("Staff Number:")
        self.verticalLayout.addWidget(self.staffNumberLabel)

        self.staffNumberField = QtWidgets.QLineEdit(self.centralwidget)
        self.staffNumberField.setObjectName("staffNumberField")
        self.verticalLayout.addWidget(self.staffNumberField)

        self.firstNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.firstNameLabel.setObjectName("firstNameLabel")
        self.firstNameLabel.setText("First Name:")
        self.verticalLayout.addWidget(self.firstNameLabel)

        self.firstNameField = QtWidgets.QLineEdit(self.centralwidget)
        self.firstNameField.setObjectName("firstNameField")
        self.verticalLayout.addWidget(self.firstNameField)

        self.secondNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.secondNameLabel.setObjectName("secondNameLabel")
        self.secondNameLabel.setText("Second Name:")
        self.verticalLayout.addWidget(self.secondNameLabel)

        self.secondNameField = QtWidgets.QLineEdit(self.centralwidget)
        self.secondNameField.setObjectName("secondNameField")
        self.verticalLayout.addWidget(self.secondNameField)

        self.lastNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.lastNameLabel.setObjectName("lastNameLabel")
        self.lastNameLabel.setText("Last Name:")
        self.verticalLayout.addWidget(self.lastNameLabel)

        self.lastNameField = QtWidgets.QLineEdit(self.centralwidget)
        self.lastNameField.setObjectName("lastNameField")
        self.verticalLayout.addWidget(self.lastNameField)

        self.passwordLabel = QtWidgets.QLabel(self.centralwidget)
        self.passwordLabel.setObjectName("passwordLabel")
        self.passwordLabel.setText("Password:")
        self.verticalLayout.addWidget(self.passwordLabel)

        self.passwordField = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordField.setObjectName("passwordField")
        self.verticalLayout.addWidget(self.passwordField)

        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.addButton.setText("Add User")
        self.addButton.clicked.connect(self.add_user)
        self.verticalLayout.addWidget(self.addButton, alignment=QtCore.Qt.AlignHCenter)

        AddUserWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddUserWindow)
        QtCore.QMetaObject.connectSlotsByName(AddUserWindow)

    def retranslateUi(self, AddUserWindow):
        _translate = QtCore.QCoreApplication.translate
        AddUserWindow.setWindowTitle(_translate("AddUserWindow", "Add User"))

    def add_user(self):
        staff_number = self.staffNumberField.text()
        first_name = self.firstNameField.text()
        second_name = self.secondNameField.text()
        last_name = self.lastNameField.text()
        password = self.passwordField.text()
        password = hashlib.sha256(password.encode()).hexdigest()

        database.add_admin(staff_number, first_name, second_name, last_name, password)
        QtWidgets.QMessageBox.information(self.centralwidget, "Success", "User added successfully!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddUserWindow = QtWidgets.QMainWindow()
    ui = Ui_AddUserWindow()
    ui.setupUi(AddUserWindow)
    AddUserWindow.show()
    sys.exit(app.exec_())
