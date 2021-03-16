from PySide2 import QtWidgets, QtGui, QtCore


class TestItem(QtWidgets.QHBoxLayout):
    def __init__(self, name, first_info, second_info):
        """
        Constructor of the class TestItem, which is a QHBoxLayout made to show the infos of the test
        :param name: str name of the test
        :param first_info: str payedOrNot or Dr that did the test
        :param second_info: str dateOrNot
        """
        super().__init__()
        self.name = name
        self.first_info = first_info
        self.second_info = second_info
        self.make_layout()

    def make_layout(self):
        """
        Making the layout of the three infos concerning the test
        """
        name = QtWidgets.QLabel(self.name)  # Name of the test
        first_info = QtWidgets.QLabel(self.first_info)  # PassedOrNot or Name of the doctor the did it
        second_info = QtWidgets.QLabel(self.second_info)  # Date or NotDate

        self.addWidget(name)
        self.addWidget(first_info)
        self.addWidget(second_info)

        lbl_stylesheet = "font-size: 12px;"
        for item in [name, first_info, second_info]:
            item.setStyleSheet(lbl_stylesheet)


class DetailsWindow(QtWidgets.QMainWindow):
    """
        Window that will hold the details about the patient
    """

    def __init__(self, ctx, main_window):
        """
        Constructor of the class DetailsWindow
        :param ctx: context of the application
        :param main_window: QMainWindow the main window of the application used to make a link with the other windows
        """
        super().__init__()
        self.ctx = ctx  # Cette variable correspond au "contexte" à l'application en elle même
        self.main_window = main_window
        self.setup_ui()

    # -- START UI --
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
            Creating all the widgets used in the MainWindow
        """
        self.center_widget = QtWidgets.QWidget()
        self.lbl_last_name = QtWidgets.QLabel("Nom:")
        self.lbl_first_name = QtWidgets.QLabel("Prénom:")
        self.lbl_birthDate = QtWidgets.QLabel("Naissance:")

        self.last_name = QtWidgets.QLabel()
        self.first_name = QtWidgets.QLabel()
        self.birthDate = QtWidgets.QLabel()

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
        self.scrollable_tests_area.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def create_layouts(self):
        """
            Creating the layouts
        """
        self.main_layout = QtWidgets.QVBoxLayout(self.center_widget)

        self.infos_layout = QtWidgets.QHBoxLayout()
        self.infos_left_layout = QtWidgets.QVBoxLayout()
        self.infos_right_layout = QtWidgets.QVBoxLayout()

        self.tests_layout = QtWidgets.QVBoxLayout()
        self.tests_passed_layout = QtWidgets.QVBoxLayout(self.tests_passed_layout_container)

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

    def setup_connections(self):
        """
            Creating the connections
        """
        pass

    def define_patient(self, patient):
        """
        Defines the patient which the infos will be shown
        """
        self.patient = patient
        self.populate_patient_infos()
        self.populate_passed_tests()

    def populate_patient_infos(self):
        """
        Updates the content of the patients infos
        """

        self.last_name.setText(self.patient.last_name)
        self.first_name.setText(self.patient.first_name)
        self.birthDate.setText(self.patient.birth_date)

    def populate_passed_tests(self):
        """
        Updates the content of the passed tests scrollable window
        """
        tests = self.patient.tests
        if tests:
            for test in self.patient.tests.items():
                self.tests_passed_layout.addLayout(TestItem(test[0], test[1][0], test[1][1]))
        self.scrollable_tests_area.setWidget(self.tests_passed_layout_container)

    # -- END UI --
