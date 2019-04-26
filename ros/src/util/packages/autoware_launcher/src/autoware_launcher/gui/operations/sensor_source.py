from python_qt_binding import QtCore
from python_qt_binding import QtWidgets
from autoware_launcher.core import myutils


class AwSensorSourceWidget(QtWidgets.QWidget):

    def __init__(self, guimgr):
        super(AwSensorSourceWidget, self).__init__()

        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel('Sensor source')
        layout.addWidget(self.label)

        self.setLayout(layout)