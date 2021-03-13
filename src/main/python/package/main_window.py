"""
Main window of the application neuroPsyPatientManager
"""

from PySide2 import QtWidgets, QtCore, QtGui

from package.ui.main_window_elements.tasks_window import TasksWindow
from package.ui.main_window_elements.details_window import DetailsWindow

from package.api.models.patient import Patient


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
        self.modify_widgets()
        self.add_widgets_to_layouts()
        self.setup_connections()

    def create_widgets(self):
        """
        creates the widgets inside the current widget
        """
        test_patient = Patient(last_name="Houari", first_name="Idir", birth_date="1996-07-25",
                               description="J'ai fais une description",
                               tests={"Teach":    ("Payé", "2021-03-12"), "Wisc-V": ("Dr.Contardsqfqsfqfqo", "2021-02-17"),
                                      "Weiss":    ("Payé", "2021-03-12"), "NewTest": ("Dr.Contaqsfqsfqsfrdo", "2021-02-17"),
                                      "Teachbis": ("Payé", "2021-03-12"), "Wisc-Vbis": ("Dr.Contqsfqsfqfqardo", "2021-02-17"),
                                      "Weissbis": ("Payé", "2021-03-12"), "Wisc-IV": ("Dr.Contaqsfqfsqfrdo", "2021-02-17"),
                                      "Weisster": ("Payé", "2021-03-12"), "Wisc-IVbis": ("Dr.Contaqsfqfsqfrdo", "2021-02-17"),
                                      "Test": ("Payé", "2021-03-12"), "Wisc-VI": ("Dr.Contaqsfqfsqfrdo", "2021-02-17"),
                                      "Testencore": ("Payé", "2021-03-12"), "Wisc-XIV": ("Dr.Contaqsfqfsqfrdo", "2021-02-17")})

        test_patient.save_patient()

        self.center_widget = QtWidgets.QWidget()
        self.details_window = DetailsWindow(ctx=self.ctx, patient=test_patient)
        self.tasks_list = TasksWindow(patient=test_patient, ctx=self.ctx)
        self.lw_patients = QtWidgets.QListWidget()
        self.te_description = QtWidgets.QTextEdit(text=test_patient.description)

        self.bottom_layout_splitter = QtWidgets.QSplitter()

    def modify_widgets(self):
        """
            Modifying the created widgets
        """
        stylesheet = self.ctx.get_resource("styles/style.css")
        with open(stylesheet) as f:
            self.setStyleSheet(f.read())

    def create_layouts(self):
        """
            Creating the layouts
        """

        self.main_layout = QtWidgets.QVBoxLayout(self.center_widget)
        self.upper_layout = QtWidgets.QHBoxLayout()
        self.bottom_layout = QtWidgets.QHBoxLayout()

    def add_widgets_to_layouts(self):
        """
            Adding the created widgets to the layouts
        """
        self.setCentralWidget(self.center_widget)

        self.main_layout.addLayout(self.upper_layout, stretch=1)
        self.main_layout.addLayout(self.bottom_layout, stretch=2)

        self.upper_layout.addWidget(self.details_window)
        self.upper_layout.addWidget(self.tasks_list)

        self.bottom_layout.addWidget(self.bottom_layout_splitter)
        self.bottom_layout_splitter.addWidget(self.lw_patients)
        self.bottom_layout_splitter.addWidget(self.te_description)
        self.bottom_layout_splitter.setSizes([self.width() / 3, self.width() * (2/3)])

    def setup_connections(self):
        """
            Creating the connections
        """
        pass
