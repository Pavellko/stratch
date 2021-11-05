from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel)
 
app = QApplication([])
 
window = QWidget()
window.setWindowTitle('Memo Card')
 
btn = QPushButton('Ответить') 
lb = QLabel('В каком году была основана Москва?') 
 
layout = QVBoxLayout()


layout.addStretch(1)

layout.addWidget(lb) 
 

layout.addWidget(btn, stretch=2) 
# layout.addStretch(1)
  

layout.setSpacing(5) # пробелы между содержимым
 
window.setLayout(layout)
window.show()
app.exec()
