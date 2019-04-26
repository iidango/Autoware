from python_qt_binding import QtCore
from python_qt_binding import QtWidgets
from autoware_launcher.core import myutils


class AwLoadMapProfileWidget(QtWidgets.QWidget):

    def __init__(self, guimgr):
        super(AwLoadMapProfileWidget, self).__init__()
        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel('load map profile')
        layout.addWidget(self.label)

        self.setLayout(layout)