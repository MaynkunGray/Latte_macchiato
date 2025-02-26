import sys
import sqlite3

from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6.QtCore import Qt
from UI import design_main, design_add_edit


class LatteMakiato(QMainWindow, design_main.Ui_MainWindow):
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


class AddEditForm(QMainWindow, design_add_edit.Ui_MainWindow):
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
