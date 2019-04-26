from python_qt_binding import QtCore
from python_qt_binding import QtWidgets
from autoware_launcher.core import myutils


class AwSelectSensorSourceWidget(QtWidgets.QWidget):

    def __init__(self, guimgr):
        super(AwSelectSensorSourceWidget, self).__init__()
        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel('Select Sensor source')
        layout.addWidget(self.label)

        self.setLayout(layout)