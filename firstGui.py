from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import json
class MainWindow(QMainWindow):
    
    def __init__(self,*arg , **kwargs ):
        super(MainWindow,self).__init__(*arg,**kwargs)
        self.setWindowTitle("PyQt5")
        with open("userData.json", "r") as f:
         self.user_data = json.load(f)
        layout = QVBoxLayout()
        label = QLabel("Form")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.inputs(layout)
        
         # Add a table widget to display the data
        self.table_widget = QTableWidget()
        layout.addWidget(self.table_widget)
        
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.setFixedSize(QSize(500, 300))
        self.display_data()
        
    def inputs(self,layout):
        name = QLineEdit()
        name.setMaxLength(20)
        name.setPlaceholderText("Name")
        name.setFixedSize(QSize(100,20))
        self.name_input = name
        email = QLineEdit()
        email.setMaxLength(30)
        email.setPlaceholderText("Email")
        email.setFixedSize(QSize(100,20))
        self.email_input = email
        
        phone = QLineEdit()
        phone.setMaxLength(10)
        phone.setPlaceholderText("Phone")
        phone.setFixedSize(QSize(100,20))
        self.phone_input = phone
        
        button = QPushButton()
        button.setText("Save")
        button.setFixedSize(QSize(100,40))
        button.clicked.connect(self.submit_form)
        layout.addWidget(name)
        layout.addWidget(email)
        layout.addWidget(phone)
        layout.addWidget(button)
        
    def submit_form(self):
        name = self.name_input.text()
        email = self.email_input.text() 
        phone = self.phone_input.text()
        self.user_data[len(self.user_data)] = {"name": name, "email": email, "phone": phone}
        with open("userData.json", "w") as f:
           json.dump(self.user_data, f)
        print(self.user_data)
        self.name_input.setText("")
        self.email_input.setText("")
        self.phone_input.setText("")
        self.display_data()
        
    def display_data(self):
        # Clear the table widget
        self.table_widget.clear()
        self.table_widget.setRowCount(len(self.user_data))
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Email", "Phone"])
        
        # Populate the table widget with data
        for row, key in enumerate(self.user_data):
            item_data = self.user_data[key]
            name = item_data.get("name", "")
            email = item_data.get("email", "")
            phone = item_data.get("phone", "")
            
            self.table_widget.setItem(row, 0, QTableWidgetItem(name))
            self.table_widget.setItem(row, 1, QTableWidgetItem(email))
            self.table_widget.setItem(row, 2, QTableWidgetItem(phone))
app =  QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()