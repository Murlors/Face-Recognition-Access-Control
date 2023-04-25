# This Python file uses the following encoding: utf-8
import sys
from threading import Thread

from PySide6.QtCore import QTimer, QDateTime
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QApplication

from Gate import *
from QueryRecord import *
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from ui_record import Ui_record


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.record_dialog = Ui_record()
        self.record_dialog.setupUi(self)
        self.time_active()
        self.ui.recordbutton.clicked.connect(self.record_dialog_show)
        self.record_dialog.backbutton.clicked.connect(self.record_dialog_hide)
        self.record_dialog_hide()

        self.record_dialog.Submitbutton.clicked.connect(self.query_record_by_id)

    def record_dialog_show(self):
        self.record_dialog.mainbgftame.show()
        self.record_dialog.backbutton.show()
        self.record_dialog.retranslateUi(self)

    def record_dialog_hide(self):
        self.record_dialog.mainbgftame.hide()
        self.record_dialog.backbutton.hide()

    def time_active(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showtime)
        self.timer.start(1000)

    def showtime(self):
        time = QDateTime.currentDateTime()
        timedisplay = time.toString("hh:mm:ss")
        datedisplay = time.toString("yyyy-MM-dd")
        self.ui.timelabel_2.setText(timedisplay)
        self.ui.datelabel_2.setText(datedisplay)
        self.record_dialog.timelabel.setText(timedisplay)
        self.record_dialog.datelabel.setText(datedisplay)

    def query_record_by_id(self):
        id = self.record_dialog.idEdit.text()
        begin_time = self.record_dialog.dateEdit_begin.text()
        end_time = self.record_dialog.dateEdit_end.text()
        print(id, begin_time, end_time)
        if id == "":
            result = gate.door_record(gate.door_id, gate.direction, begin_time, end_time)
        else:
            result = id_record(id, begin_time, end_time)
        result = json.loads(result)
        self.record_dialog.tableWidget.setRowCount(len(result))
        for i in range(len(result)):
            self.record_dialog.tableWidget.setItem(i, 0, QTableWidgetItem(result[i]['id']))
            self.record_dialog.tableWidget.setItem(i, 1, QTableWidgetItem(result[i]['name']))
            self.record_dialog.tableWidget.setItem(i, 2, QTableWidgetItem(result[i]['time']))
            self.record_dialog.tableWidget.setItem(i, 3, QTableWidgetItem(result[i]['direction']))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    gate = Gate(widget, 1, 'in', url='http://localhost:5555')
    Thread(target=gate.run).start()
    sys.exit(app.exec())
