#a temp ui for qt based implimentation with matplot lib to show graphs
import sys
import matplotlib
import json
matplotlib.use('Qt5Agg')

from PyQt5 import QtCore, QtWidgets

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

file = open("temp.txt","r")
data = file.readlines()
humx = []
humy = []
tempx = []
tempy = []
for i in range(len(data)):
	humy.append((json.loads(data[i])).get("hum"))
	tempy.append((json.loads(data[i])).get("temp"))

for i in range(1,3044):
	humx.append(i)
	tempx.append(i)

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object, 
        # which defines a single set of axes as self.axes.
        sc = MplCanvas(self, width=10, height=10, dpi=100)
        sc.axes.plot(humx , humy)
        sc.axes.plot(tempx , tempy)
        self.setCentralWidget(sc)

        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()
