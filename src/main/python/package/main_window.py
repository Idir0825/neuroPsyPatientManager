"""
Main window of the application neuroPsyPatientManager
"""

from PySide2 import QtWidgets, QtCore, QtGui

from package.ui.main_window_elements.tasks_window import TasksWindow
from package.ui.main_window_elements.details_window import DetailsWindow
from package.ui.main_window_elements.patients_list_window import PatientsList


class MainWindow(QtWidgets.QMainWindow):
    """
    MainWindow of the app neuroPsyPatientManager
    """

    def __init__(self, ctx):
        """
        Constructor for the class MainWindow, this class is the mainwindow of the application neuroPsyPatientManager
        :param ctx: application context, the app itself
        """
        super().__init__()
        self.ctx = ctx
        self.setup_ui()

    def setup_ui(self):
        """
        Execution of the UI building functions
        """
        self.create_widgets()
        self.create_layouts()
        self.add_widgets_to_layouts()
        self.modify_widgets()
        self.setup_connections()

    def create_widgets(self):
        """
        creates the widgets inside the current widget
        """

        self.center_widget = QtWidgets.QWidget()
        self.patients_layout_container = QtWidgets.QWidget()

        self.details_window = DetailsWindow(ctx=self.ctx, main_window=self)
        self.tasks_list = TasksWindow(ctx=self.ctx, main_window=self)
        self.btn_add_patient = QtWidgets.QPushButton("Ajouter un patient")
        self.lw_patients = PatientsList(ctx=self.ctx, main_window=self)
        self.te_description = QtWidgets.QTextEdit()

        self.bottom_layout_splitter = QtWidgets.QSplitter()

    def modify_widgets(self):
        """
            Modifying the created widgets
        """
        # -- Setting stylesheets --
        stylesheet = self.ctx.get_resource("styles/style.css")
        with open(stylesheet) as f:
            self.setStyleSheet(f.read())

        self.patients_layout_container.setStyleSheet("border: 1px solid rgb(50, 50, 50); border-radius: 4px;")

        self.btn_add_patient.setStyleSheet("font-weight: bold;")

        # -- End Setting stylesheets --

        self.patients_layout.setContentsMargins(0, 0, 0, 0)
        self.patients_layout.setSpacing(0)

        self.bottom_layout_splitter.setCollapsible(0, False)  # Avoid items in the splitter from collapsing completely
        self.bottom_layout_splitter.setCollapsible(1, False)

    def create_layouts(self):
        """
            Creating the layouts
        """

        self.main_layout = QtWidgets.QVBoxLayout(self.center_widget)
        self.upper_layout = QtWidgets.QHBoxLayout()
        self.patients_layout = QtWidgets.QVBoxLayout(self.patients_layout_container)

    def add_widgets_to_layouts(self):
        """
            Adding the created widgets to the layouts
        """
        self.setCentralWidget(self.center_widget)

        self.main_layout.addLayout(self.upper_layout, stretch=1)
        self.main_layout.addWidget(self.bottom_layout_splitter, stretch=2)

        self.upper_layout.addWidget(self.details_window)
        self.upper_layout.addWidget(self.tasks_list)

        self.patients_layout.addWidget(self.btn_add_patient)
        self.patients_layout.addWidget(self.lw_patients)

        self.bottom_layout_splitter.addWidget(self.patients_layout_container)
        self.bottom_layout_splitter.addWidget(self.te_description)

    def setup_connections(self):
        """
            Creating the connections
        """
        pass
