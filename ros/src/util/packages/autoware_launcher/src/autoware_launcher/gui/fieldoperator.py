from python_qt_binding import QtCore
from python_qt_binding import QtGui
from python_qt_binding import QtWidgets

from ..core import myutils
from ..core import AwLaunchClientIF

from .operations import AwSelectSensorSourceWidget
from .operations import AwSensorSourceWidget
from .operations import AwLoadMapProfileWidget
from .operations import AwLoadComputingProfileWidget
from .operations import AwLoadMapWidget
from .operations import AwComputingWidget
from .operations import AwOpenRvizWidget
from .operations import AwToggleLoggingWidget
from .operations import AwToggleGatewayWidget



class AwFieldOperatorPanel(QtWidgets.QWidget):

    def __init__(self, guimgr):
        super(AwFieldOperatorPanel, self).__init__()
        self.guimgr = guimgr
        self.frames = {"root/" + name: None for name in ["map", "vehicle", "sensing", "visualization"]}

        self.awlogo = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(myutils.package("resources/autoware_logo.png"))
        self.awlogo.setPixmap(pixmap)
        # self.awlogo.setAlignment(QtCore.Qt.AlignCenter)
        # self.awlogo.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)

        layout = QtWidgets.QGridLayout()

        self.select_sensor_source = AwSelectSensorSourceWidget(self.guimgr)
        self.sensor_source = AwSelectSensorSourceWidget(self.guimgr)
        self.load_map_profile = AwLoadMapProfileWidget(self.guimgr)
        self.load_computing_profile = AwLoadComputingProfileWidget(self.guimgr)
        self.load_map = AwLoadMapWidget(self.guimgr)
        self.computing = AwComputingWidget(self.guimgr)
        self.open_rviz = AwOpenRvizWidget(self.guimgr)
        self.logging = AwToggleLoggingWidget(self.guimgr)
        self.gateway = AwToggleGatewayWidget(self.guimgr)

        self.select_sensor_source.setStyleSheet("background-color:red;")
        self.sensor_source.setStyleSheet("background-color:red;")
        self.load_map_profile.setStyleSheet("background-color:red;")
        self.load_computing_profile.setStyleSheet("background-color:red;")
        self.load_map.setStyleSheet("background-color:red;")
        self.computing.setStyleSheet("background-color:red;")
        self.open_rviz.setStyleSheet("background-color:red;")
        self.logging.setStyleSheet("background-color:red;")
        self.gateway.setStyleSheet("background-color:red;")

        # layout.addWidget(self.awlogo,                  0, 0,  2,  4)
        layout.addWidget(self.select_sensor_source,    2, 0, 11,  4)
        layout.addWidget(self.load_map_profile,       13, 0,  1,  8)
        layout.addWidget(self.load_computing_profile, 14, 0,  1,  8)
        layout.addWidget(self.sensor_source,           0, 4, 13,  4)
        layout.addWidget(self.load_map,                0, 8,  3,  4)
        layout.addWidget(self.computing,               3, 8,  10,  4)
        layout.addWidget(self.open_rviz,               13, 8,  1, 4)
        layout.addWidget(self.logging,                 14, 8,  2, 2)
        layout.addWidget(self.gateway,                 14, 10,  2, 2)

        self.setLayout(layout)

    def profile_ui_cleared(self):
        pass
        # self.guimgr.panel_setup(self, self.awlogo)

    def node_ui_created(self, lnode):
        pass
        # if lnode.path() == "root": self.setup_widget(lnode)

    def node_ui_updated(self, lnode):
        pass
        # if lnode.path() == "root": self.setup_widget(lnode)

    def status_ui_updated(self, lpath, state):
        pass
        # frame = self.frames.get(lpath)
        # if frame:
        #     if state == 0x00: frame.term_completed()
        #     if state == 0x01: frame.exec_requested()
        #     if state == 0x02: frame.term_requested()

    # def setup_widget(self, node):
    #     layout = QtWidgets.QGridLayout()

    #     self.select_sensor_source = AwSelectSensorSourceWidget(self.guimgr)
    #     self.sensor_source = AwSelectSensorSourceWidget(self.guimgr)
    #     self.load_map_profile = AwLoadMapProfileWidget(self.guimgr)
    #     self.load_computing_profile = AwLoadComputingProfileWidget(self.guimgr)
    #     self.load_map = AwLoadMapWidget(self.guimgr)
    #     self.computing = AwComputingWidget(self.guimgr)
    #     self.open_rviz = AwOpenRvizWidget(self.guimgr)
    #     self.logging = AwToggleLoggingWidget(self.guimgr)
    #     self.gateway = AwToggleGatewayWidget(self.guimgr)

    #     # layout.addWidget(self.select_sensor_source,    0, 0, 13,  4)
    #     # layout.addWidget(self.load_map_profile,       13, 0,  1,  8)
    #     # layout.addWidget(self.load_computing_profile, 13, 0,  1,  8)
    #     # layout.addWidget(self.sensor_source,           0, 4, 13,  4)
    #     # layout.addWidget(self.load_map,                0, 8,  3,  4)
    #     # layout.addWidget(self.computing,               3, 8,  9,  4)
    #     # layout.addWidget(self.open_rviz,               13, 8,  1, 4)
    #     # layout.addWidget(self.logging,                 14, 8,  1, 4)
    #     # layout.addWidget(self.gateway,                 15, 8,  1, 4)

    #     self.guimgr.panel_add_widget(self, self.select_sensor_source)
    #     self.guimgr.panel_add_widget(self, self.load_map_profile)
    #     self.guimgr.panel_add_widget(self, self.load_computing_profile)
    #     self.guimgr.panel_add_widget(self, self.sensor_source)
    #     self.guimgr.panel_add_widget(self, self.load_map)
    #     self.guimgr.panel_add_widget(self, self.computing)
    #     self.guimgr.panel_add_widget(self, self.open_rviz)
    #     self.guimgr.panel_add_widget(self, self.logging)
    #     self.guimgr.panel_add_widget(self, self.gateway)

    #     print('set up layout')
    #     self.setLayout(layout)


class AwLaunchFrame(QtWidgets.QWidget):

    def __init__(self, guimgr, node, opts):
        super(AwLaunchFrame, self).__init__()
        self.node = node
        self.states = ["Launch", "Terminate"]

        guimgr.frame_setup(self)

        self.title.setText(node.name().capitalize())
        guimgr.frame_add_text_widget(self, node.get_config("exts.description", "No Description"))

        self.button = QtWidgets.QPushButton(self.states[0])
        self.button.clicked.connect(self.onclicked)
        guimgr.frame_add_button(self, self.button)

    def onclicked(self):
        state_text = self.button.text()
        if state_text == self.states[0]:
            self.node.launch(True)
            self.exec_requested()
        if state_text == self.states[1]:
            self.node.launch(False)
            self.term_requested()

    def exec_requested(self):
        self.button.setText(self.states[1])

    def term_requested(self):
        self.button.setEnabled(False)

    def term_completed(self):
        self.button.setText(self.states[0])
        self.button.setEnabled(True)

