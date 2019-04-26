from python_qt_binding import QtCore
from python_qt_binding import QtWidgets
from autoware_launcher.core import myutils


class AwLoadComputingProfileWidget(QtWidgets.QWidget):

    def __init__(self, guimgr):
        super(AwLoadComputingProfileWidget, self).__init__()
        layout = QtWidgets.QVBoxLayout()

        self.label = QtWidgets.QLabel('load Computing profile')
        layout.addWidget(self.label)

        self.setLayout(layout)