from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox, QMainWindow, \
    QWidgetAction, QTableWidget, QTableWidgetItem, QDialog, QVBoxLayout
import sqlite3
import sys

from PyQt6.QtGui import QAction


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student management system")

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")


        add_student_action = QAction("Add student", self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        search = QAction("search", self)
        search.triggered.connect(self.search_text)
        edit_menu_item.addAction(search)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = connection.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()

    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search_text(self):
        search_dialog = InsertSearch()
        search_dialog.exec()

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add student name
        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

         # Add combo box
        self.course_name = QComboBox()
        courses = ["Biology", "Math", "Astronomy", "Phisics"]
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)


        # Add mobile
        self.mobile = QLineEdit()
        self.mobile.setPlaceholderText("Mobile")
        layout.addWidget(self.mobile)


        # Add a submit button

        button = QPushButton("Register")
        button.clicked.connect(self.add_student)
        layout.addWidget(button)



        self.setLayout(layout)

class InsertSearch(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout()

        # Add student name
        self.search = QLineEdit()
        self.search.setPlaceholderText("Search")
        layout.addWidget(self.search)



        # Add a submit button

        button = QPushButton("Search")
        button.clicked.connect(self.search_student)
        layout.addWidget(button)
        self.setLayout(layout)

    def search_student(self):
        name = self.search.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
        rows = list(result)
        print(rows)
        items = mainwindow.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            mainwindow.table.item(item.row(), 1).setSelected(True)

        cursor.close()
        connection.close()


    def add_student(self):
        name=self.student_name.text()
        course=self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile.text()
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, mobile))
        connection.commit()
        cursor.close()
        connection.close()
        mainwindow.load_data()

app = QApplication(sys.argv)
mainwindow = MainWindow()
mainwindow.show()
mainwindow.load_data()
sys.exit(app.exec())