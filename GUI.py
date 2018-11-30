from Huffman import Huffman
from Form1 import Ui_Form

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import sys


class GUI(QWidget, Huffman, Ui_Form):
    # a figure instance to plot on

    # this is the Canvas Widget that displays the `figure`
    # it takes the `figure` instance as a parameter to __init__

    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)
        self.setupUi(self)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setParent(self.groupBox_4)
        self.canvas.setGeometry(QRect(20, 20, 600, 600))

        self.pb_encode.clicked.connect(self.encode_string)
        self.pb_decode.clicked.connect(self.decode_string)
        self.pb_reset.clicked.connect(self.clear_plot)

    def encode_string(self):
        self.tw_encode_table.clear()
        string = self.pte_encode.toPlainText()
        self.init_encode(string)
        # show graph
        self.plot()

        # show table
        for key in self.encode_table:
            value = self.encode_table[key]
            keyItem = QTableWidgetItem(key)
            valueItem = QTableWidgetItem(str(value))
            self.tw_encode_table.insertRow(0)
            self.tw_encode_table.setItem(0, 0, keyItem)
            self.tw_encode_table.setItem(0, 1, valueItem)

    def decode_string(self):
        string = self.pte_decode_input.toPlainText()
        ret_str = self.decode(string)
        self.pte_decode_output.setPlainText(ret_str)

    def plot(self):
        self.canvas.draw()

    def clear_plot(self):
        self.canvas.figure.clf()
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = GUI()
    main.show()

    # main.plot()

    sys.exit(app.exec_())
