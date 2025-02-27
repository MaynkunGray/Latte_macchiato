import sys
import sqlite3

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.QtCore import Qt
from PyQt6 import QtCore, QtGui, QtWidgets


class MainWindowDesign(object):
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


class AddEditDesign(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 623)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sort_name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.sort_name.setGeometry(QtCore.QRect(240, 110, 461, 31))
        self.sort_name.setObjectName("sort_name")
        self.main_header = QtWidgets.QLabel(parent=self.centralwidget)
        self.main_header.setGeometry(QtCore.QRect(210, 20, 451, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.main_header.setFont(font)
        self.main_header.setText("")
        self.main_header.setObjectName("main_header")
        self.roasting = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.roasting.setGeometry(QtCore.QRect(240, 180, 461, 31))
        self.roasting.setObjectName("roasting")
        self.molot_or_zer = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.molot_or_zer.setGeometry(QtCore.QRect(240, 260, 461, 31))
        self.molot_or_zer.setObjectName("molot_or_zer")
        self.taste = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.taste.setGeometry(QtCore.QRect(240, 340, 461, 31))
        self.taste.setObjectName("taste")
        self.price = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.price.setGeometry(QtCore.QRect(240, 420, 461, 31))
        self.price.setObjectName("price")
        self.volume = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.volume.setGeometry(QtCore.QRect(240, 510, 461, 31))
        self.volume.setObjectName("volume")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 260, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 340, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 430, 60, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 520, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.save_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.save_button.setGeometry(QtCore.QRect(580, 570, 121, 41))
        self.save_button.setObjectName("save_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Добавление / изменение записей"))
        self.label_2.setText(_translate("MainWindow", "Название сорта"))
        self.label_3.setText(_translate("MainWindow", "Степень обжарки"))
        self.label_4.setText(_translate("MainWindow", "Молотый/в зернах"))
        self.label_5.setText(_translate("MainWindow", "Описание вкуса"))
        self.label_6.setText(_translate("MainWindow", "Цена"))
        self.label_7.setText(_translate("MainWindow", "Объем упаковки"))
        self.save_button.setText(_translate("MainWindow", "Сохранить"))


class LatteMakiato(QMainWindow, MainWindowDesign):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.titles = None

        cur.execute("SELECT * FROM Info").fetchall()
        titles = [description[0] for description in cur.description]
        self.tableWidget.setColumnCount(len(titles))
        self.tableWidget.setHorizontalHeaderLabels(titles)

        self.update_result()
        self.create_new_data.clicked.connect(self.create_new)
        self.change_data.clicked.connect(self.change_curr_data)

    def update_result(self):
        result = cur.execute("SELECT * FROM Info").fetchall()
        self.tableWidget.setRowCount(len(result))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                item = QTableWidgetItem(str(val))
                self.tableWidget.setItem(i, j, item)
                if j == 0:
                    item.setFlags(Qt.ItemFlag.ItemIsEnabled)

    def create_new(self):
        form = AddEditForm([])
        form.show()
        add_forms.append(form)

    def change_curr_data(self):
        choosed_row = -1
        if self.tableWidget.selectedItems():
            for i in self.tableWidget.selectedItems():
                if choosed_row == -1:
                    choosed_row = i.row()
                elif choosed_row != i.row():
                    return
            result = cur.execute(f"""SELECT * FROM Info
                                  WHERE id = {self.tableWidget.item(choosed_row, 0).text()}""").fetchone()
            form = AddEditForm([i for i in result])
            form.show()
            edit_forms.append(form)

    def closeEvent(self, f):
        app.closeAllWindows()


class AddEditForm(QMainWindow, AddEditDesign):
    def __init__(self, listik):
        super().__init__()

        self.setupUi(self)

        self.forms = [self.sort_name, self.roasting, self.molot_or_zer, self.taste, self.price, self.volume]
        self.hl = listik
        if self.hl:
            self.main_header.setText('Редактирование записи в базе данных')
            for i in range(len(self.forms)):
                self.forms[i].setText(str(self.hl[i + 1]))
        else:
            self.main_header.setText('Добавление записи в базу данных')

        self.save_button.clicked.connect(self.save_data)

    def save_data(self):
        for i in self.forms:
            if not i.text():
                return
        if self.hl:
            cur.execute(f"""UPDATE Info
                                    SET 'Название сорта' = '{self.forms[0].text()}',
                                        'Степень обжарки' = '{self.forms[1].text()}',
                                        'Молотый/в зернах' = '{self.forms[2].text()}',
                                        'Описание вкуса' = '{self.forms[3].text()}',
                                        'Цена' = '{self.forms[4].text()}',
                                        'Объем упаковки' = '{self.forms[5].text()}'
                                    WHERE id = {self.hl[0]}""").fetchall()
            con.commit()
            ex.update_result()
        else:
            str_ask = """INSERT INTO Info('Название сорта', 'Степень обжарки', 'Молотый/в зернах',
             'Описание вкуса', 'Цена', 'Объем упаковки') VALUES(?, ?, ?, ?, ?, ?)"""
            data_tuple = (self.forms[0].text(), self.forms[1].text(), self.forms[2].text(),
                          self.forms[3].text(), self.forms[4].text(), self.forms[5].text())
            cur.execute(str_ask, data_tuple)
            con.commit()
            ex.update_result()
        self.destroy()


if __name__ == '__main__':
    add_forms = []
    edit_forms = []
    con = sqlite3.connect("data/coffee.sqlite")
    cur = con.cursor()
    app = QApplication(sys.argv)
    ex = LatteMakiato()
    ex.show()
    sys.exit(app.exec())
