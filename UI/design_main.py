# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(803, 664)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 20, 761, 561))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.create_new_data = QtWidgets.QPushButton(parent=self.centralwidget)
        self.create_new_data.setGeometry(QtCore.QRect(60, 610, 281, 31))
        self.create_new_data.setObjectName("create_new_data")
        self.change_data = QtWidgets.QPushButton(parent=self.centralwidget)
        self.change_data.setGeometry(QtCore.QRect(470, 610, 281, 31))
        self.change_data.setObjectName("change_data")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Латте макиато"))
        self.create_new_data.setText(_translate("MainWindow", "Добавить запись"))
        self.change_data.setText(_translate("MainWindow", "Изменить выбранную в таблице запись"))
