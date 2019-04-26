from python_qt_binding import QtCore
from python_qt_binding import QtWidgets
from autoware_launcher.core import myutils


class AwOpenRvizWidget(QtWidgets.QWidget):

    def __init__(self, guimgr):
        super(AwOpenRvizWidget, self).__init__()

        self.button = QtWidgets.QPushButton('Open Rviz', self)
        self.button.clicked.connect(self.onclicked)

    def onclicked(self):
        print('open rviz')

