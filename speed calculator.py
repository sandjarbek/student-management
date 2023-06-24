from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox

import sys


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        self.setWindowTitle("Speed calculator")

        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_line = QLineEdit()

        calculate_button = QPushButton("Calculate speed")
        calculate_button.clicked.connect(self.calculate_speed)

        self.measurement = QComboBox()
        self.measurement.addItem("KM")
        self.measurement.addItem("Miles")

        self.output_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line, 1, 1)
        grid.addWidget(calculate_button, 2, 0)
        grid.addWidget(self.output_label, 3, 0, 1, 2)
        grid.addWidget(self.measurement, 0, 2)

        self.setLayout(grid)

    def calculate_speed(self):
        # if self.measurement.addItem("KM"):
            speed = int(self.distance_line_edit.text()) / int(self.time_line.text())
            self.output_label.setText(f"Average speed is {speed}")
            print(speed)
        # else:
        #
        #     speed = int(self.distance_line_edit.text())*1,60934 / int(self.time_line.text())
        #     self.output_label.setText(f"Average speed is {speed}")

        # current_year = datetime.now().year
        # date_of_birth = self.date_birth_line.text()
        # year_of_birth = datetime.strptime(date_of_birth, "%d.%m.%Y").date().year
        # age=current_year - year_of_birth
        # self.output_label.setText(f"{self.name_line_edit.text()} is {age} year old")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
