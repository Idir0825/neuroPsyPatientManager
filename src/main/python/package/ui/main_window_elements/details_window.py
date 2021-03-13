from PySide2 import QtWidgets, QtGui, QtCore


class DetailsWindow(QtWidgets.QMainWindow):
    """
        Window that will hold the details about the patient
    """

    def __init__(self, ctx, patient):
        """
        Constructor of the class DetailsWindow
        :param ctx: context of the application
        :param patient: Patient the patient that we need to show the infos of
        """
        super().__init__()
        self.ctx = ctx  # Cette variable correspond au "contexte" à l'application en elle même
        self.patient = patient
        self.setup_ui()
        self.populate_passed_tests()

    # -- START UI --
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
            Creating all the widgets used in the MainWindow
        """
        self.center_widget = QtWidgets.QWidget()
        self.lbl_last_name = QtWidgets.QLabel("Nom:")
        self.lbl_first_name = QtWidgets.QLabel("Prénom:")
        self.lbl_birthDate = QtWidgets.QLabel("Naissance:")

        self.last_name = QtWidgets.QLabel(text=self.patient.last_name)
        self.first_name = QtWidgets.QLabel(text=self.patient.first_name)
        self.birthDate = QtWidgets.QLabel(text=self.patient.birth_date)

        self.hline = QtWidgets.QFrame() # Creating the line between the patient infos and the tests he passed on the UI
        self.hline.setObjectName("line")
        self.hline.setGeometry(QtCore.QRect(320, 150, 118, 3))
        self.hline.setFrameShape(QtWidgets.QFrame().HLine)
        self.hline.setFrameShadow(QtWidgets.QFrame().Sunken)

        self.lbl_tests = QtWidgets.QLabel("Tests passés:")

        self.tests_passed_layout_container = QtWidgets.QWidget()
        self.scrollable_tests_area = QtWidgets.QScrollArea()

    def modify_widgets(self):
        """
            Modifying the created widgets
        """
        css_file = self.ctx.get_resource("styles/details_window_style.css")  # ça va bien dans 'resources/base/
        with open(css_file, "r") as f:
            self.setStyleSheet(f.read())

        lbl_stylesheet = "font-size: 20px;"
        for item in [self.lbl_last_name, self.lbl_first_name, self.lbl_birthDate, self.lbl_tests, self.last_name, self.first_name, self.birthDate]:
            item.setStyleSheet(lbl_stylesheet)

        self.scrollable_tests_area.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def create_layouts(self):
        """
            Creating the layouts
        """
        self.main_layout = QtWidgets.QVBoxLayout(self.center_widget)

        self.infos_layout = QtWidgets.QHBoxLayout()
        self.infos_left_layout = QtWidgets.QVBoxLayout()
        self.infos_right_layout = QtWidgets.QVBoxLayout()

        self.tests_layout = QtWidgets.QVBoxLayout()
        self.tests_passed_layout = QtWidgets.QGridLayout(self.tests_passed_layout_container)

    def add_widgets_to_layouts(self):
        """
            Adding the created widgets to the layouts
        """
        self.setCentralWidget(self.center_widget)

        self.main_layout.addLayout(self.infos_layout)
        self.main_layout.addWidget(self.hline)
        self.main_layout.addLayout(self.tests_layout)

        self.infos_layout.addLayout(self.infos_left_layout)
        self.infos_layout.addLayout(self.infos_right_layout)

        self.infos_left_layout.addWidget(self.lbl_last_name)
        self.infos_right_layout.addWidget(self.last_name)

        self.infos_left_layout.addWidget(self.lbl_first_name)
        self.infos_right_layout.addWidget(self.first_name)

        self.infos_left_layout.addWidget(self.lbl_birthDate)
        self.infos_right_layout.addWidget(self.birthDate)

        self.tests_layout.addWidget(self.lbl_tests)
        self.tests_layout.addWidget(self.scrollable_tests_area)

        self.scrollable_tests_area.setWidget(self.tests_passed_layout_container)

    def setup_connections(self):
        """
            Creating the connections
        """
        pass

    def populate_passed_tests(self):
        """
        Updates the content of the passed tests scrollable window
        """
        tests = self.patient.tests
        if tests:
            i = 0
            for test in self.patient.tests.items():
                name = QtWidgets.QLabel(test[0])  # Name of the test
                first_info = QtWidgets.QLabel(test[1][0])  # PassedOrNot or Name of the doctor the did it
                second_info = QtWidgets.QLabel(test[1][1])  # Date or NotDate

                self.tests_passed_layout.addWidget(name, i, 0)
                self.tests_passed_layout.addWidget(first_info, i, 1)
                self.tests_passed_layout.addWidget(second_info, i, 2)
                i += 1
                self.patient.save_patient()

    # -- END UI --
