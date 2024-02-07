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
        self.filtered_user_data = []
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
        self.setFixedSize(QSize(550, 300))
        self.search_user()
        
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
        hbox = QHBoxLayout()
        hbox.addWidget(QLabel("Name:"))
        hbox.addWidget(name)
        hbox.addWidget(QLabel("Email:"))
        hbox.addWidget(email)
        hbox.addWidget(QLabel("Phone:"))
        hbox.addWidget(phone)
        hbox.addWidget(button)
        
        
        search = QLineEdit()
        search.setMaxLength(30)
        search.setPlaceholderText("Search...")
        search.setFixedSize(QSize(100,20))
        self.search_input = search
        
        searchBtn = QPushButton()
        searchBtn.setText("Search")
        searchBtn.setFixedSize(QSize(100,40))
        searchBtn.clicked.connect(self.search_user)
        searchBox = QHBoxLayout()
        searchBox.setSpacing(10)
        # searchBox.setContentsMargins(0, -1, 330, -1)
        searchBox.addWidget(search)
        searchBox.addWidget(searchBtn)
        searchBox.addStretch()

        layout.addLayout(hbox)
        layout.addLayout(searchBox)
        
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
        self.search_user()
        
    def search_user(self):
        search_text = self.search_input.text()
        self.filtered_user_data.clear()  # Clear the list before starting a new search
        for user_details in self.user_data.values():
            if user_details["name"].find(search_text) != -1:
                self.filtered_user_data.append(user_details)  # Save the filtered user details
                print(user_details)
        
        # After filtering, display the filtered data in the table
        self.display_data()
        
    def display_data(self):
        # Clear the table widget
        self.table_widget.clear()
        self.table_widget.setRowCount(len(self.filtered_user_data))  # Use filtered data for row count
        self.table_widget.setColumnCount(3)
        self.table_widget.setHorizontalHeaderLabels(["Name", "Email", "Phone"])
        self.table_widget.setColumnWidth(1, 200)
        # Populate the table widget with filtered data
        for row, user_details in enumerate(self.filtered_user_data):
            name = user_details.get("name", "")
            email = user_details.get("email", "")
            phone = user_details.get("phone", "")
            
            self.table_widget.setItem(row, 0, QTableWidgetItem(name))
            self.table_widget.setItem(row, 1, QTableWidgetItem(email))
            self.table_widget.setItem(row, 2, QTableWidgetItem(phone))
         
app =  QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()