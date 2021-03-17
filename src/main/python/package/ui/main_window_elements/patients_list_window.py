from PySide2 import QtWidgets, QtCore, QtGui

from package.api.models.patient import get_patients


class PatientsList(QtWidgets.QListWidget):
    """ The list that will contain all the patients in the mainWindow of the application """

    def __init__(self, ctx, main_window):
        """
        Constructor of the class 'PatientList'

        :param ctx: context of the application, the app itself
        :param main_window: QMainWindow the main window of the application used to make a link with the other windows
        """
        super().__init__()
        self.ctx = ctx
        self.main_window = main_window
        self.setup_ui()

    def setup_ui(self):
        """
        Execution of the UI building functions
        """
        self.populate_list()
        self.modify_widgets()

    def modify_widgets(self):
        """ Modifies the created widgets """
        stylesheet = self.ctx.get_resource("styles/patients_list_window.css")
        with open(stylesheet, 'r') as f:
            self.setStyleSheet(f.read())

        self.setAlternatingRowColors(True)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setItemAlignment(QtCore.Qt.AlignCenter)

    def get_selected_item(self):
        """
            Returns the item that was selected else, returns None
        :return:
        """
        selected_items = self.lw_notes.selectedItems()
        if selected_items:
            return selected_items[0]
        return None

    def populate_list(self):
        """ Populates the list with all the patients """

        patients = get_patients()
        for patient in patients:
            item = QtWidgets.QListWidgetItem(patient.last_name + " " + patient.first_name)
            self.addItem(item)
            item.patient = patient
