from PySide2.QtWidgets import QApplication, QWidget
import sys
import time
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle("WeatherMan")
        self.setGeometry(300,300, 500,500)
        self.setMinimumHeight(250)
        self.setMinimumWidth(250)
 
 
myApp = QApplication(sys.argv)# define argument value is that 4 or only 1
window = Window()
window.show()
 
myApp.exec_()
sys.exit(0)
