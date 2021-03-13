from PySide2 import QtWidgets, QtCore, QtGui
from glob import glob
import os

COLORS = {"red":    (255, 187, 187), "orange": (255, 218, 187), "green": (231, 255, 187), "blue": (187, 205, 255),
          "purple": (224, 202, 245)}


class TaskItem(QtWidgets.QListWidgetItem):
    """ Item inside of a QListWidget of the TasksWindow class. This class implements two methods that are used to change the status of a task"""
    def __init__(self, patient, name, color_name, list_widget):
        """
        Constructor for the class TaskItem
        :param patient: Patient the patient that the tasks are linked to
        :param name: str the name of the task represented by this item
        :param color_name: str the color with which the item is actually highlighted
        :param list_widget: QListWidget the list widget that will contain the TaskItem
        """
        super().__init__(name)

        self.patient = patient
        self.list_widget = list_widget
        self.name = name
        self.color_name = color_name
        self.setTextAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.setSizeHint(QtCore.QSize(0, 25))  # Permet de changer la taille de l'élément

        self.list_widget.addItem(self)
        self.set_background_color()

    def toggle_state(self):
        """
        Calls the function set_task_status of the patient to change the status of the task linked to this TaskItem
        :return:
        """
        _, self.color_name = self.patient.set_task_status(name=self.name)
        self.set_background_color()

    def set_background_color(self):
        """
        Changes the background color of the TaskItem in the list depending on the color that the task status has
        """
        color = COLORS.get(self.color_name)
        self.setBackgroundColor(QtGui.QColor(*color))
        color_str = ", ".join(map(str, color))  # On utilise str sur chaque élément du tuple color
        stylesheet = f""" QListView::item:selected {{background: rgb({color_str});
													 color: #000000;}}
					QListView{{color: #000000;
					font-weight: bold;}}
					"""
        # Les :: signifient qu'on veut affecter uniquement les items, et pas tout le liste view, le : signifie qu'on veut affecter un événement
        # On utilise le CSS pour pouvoir mettre une couleur de sélection qui soit la même que la couleur qui montre si l'item est fini ou non
        self.list_widget.setStyleSheet(stylesheet)


class TasksWindow(QtWidgets.QMainWindow):
    """
    Window that will show up all the tasks that need to be done
    """
    def __init__(self, patient, ctx):
        """
        Constructor of the class TasksWindow, this will generate the window with all the tasks
        :param patient: Patient the patient to which the tasks are linked
        :param ctx: application context, the app itself
        """
        super().__init__()
        self.setMinimumSize(250, 250)
        self.patient = patient
        self.ctx = ctx
        self.setup_ui()
        self.get_tasks()
        self.make_change_color_to_delete(self.patient.color_to_delete)
        self.resize(QtCore.QSize(256, 350))

    def setup_ui(self):
        """
        sets up the ui of the current widget
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
        self.center_widget = QtWidgets.QWidget()

        self.lw_tasks = QtWidgets.QListWidget()
        self.btn_add = QtWidgets.QPushButton()
        self.btn_clean = QtWidgets.QPushButton()
        self.icon_color_to_delete = QtWidgets.QPushButton()

        self.rc_delete_menu = QtWidgets.QMenu()
        self.rc_delete_menu_choose_color_to_delete_menu = QtWidgets.QMenu("Couleur des tâches terminées")
        self.colors = glob(os.path.join(self.ctx.get_resource(), "colors/*.svg"))
        self.rc_delete_menu_choose_color_to_delete_menu_choices = {}
        for color_path in self.colors:
            color = os.path.basename(os.path.splitext(color_path)[0])
            self.rc_delete_menu_choose_color_to_delete_menu_choices[
                QtWidgets.QAction(icon=QtGui.QIcon(color_path))] = color

        self.delete_tasks_confirmation_box = QtWidgets.QMessageBox()
        self.delete_tasks_confirmation_box.setWindowTitle("Suppression")
        self.delete_tasks_confirmation_box.setText(f"Suppression d'une ou plusieurs tâche(s), continuer ?")
        self.delete_tasks_confirmation_box.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.btn_yes_task = self.delete_tasks_confirmation_box.addButton("Oui", QtWidgets.QMessageBox.ActionRole)
        self.btn_no_task = self.delete_tasks_confirmation_box.addButton("Non", QtWidgets.QMessageBox.ActionRole)

    def modify_widgets(self):
        """
        modifies the widgets inside the current widget
        """
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        stylesheet = self.ctx.get_resource("styles/task_window_style.css")
        with open(stylesheet, "r") as f:
            self.setStyleSheet(f.read())

        # FramelessWindowHint Permet d'enlever la barre de tâche, | signifie qu'on veut les deux flags
        self.setWindowFlags(
                QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)  # Les flags sont des attributs

        self.btn_add.setIcon(QtGui.QIcon(self.ctx.get_resource("images/add.svg")))
        self.btn_clean.setIcon(QtGui.QIcon(self.ctx.get_resource("images/clean.svg")))
        self.icon_color_to_delete.setIcon(QtGui.QIcon(self.ctx.get_resource(f"colors/{self.patient.color_to_delete}.svg")))

        self.btn_add.setFixedSize(36, 36)
        self.btn_clean.setFixedSize(36, 36)

        self.lw_tasks.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lw_tasks.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    def create_layouts(self):
        """
        creates the layouts inside the current widget
        """
        self.main_layout = QtWidgets.QVBoxLayout(self.center_widget)
        self.layout_buttons = QtWidgets.QHBoxLayout()

    def add_widgets_to_layouts(self):
        """
        populates the layouts of the current widget
        """
        self.setCentralWidget(self.center_widget)

        self.main_layout.addWidget(self.lw_tasks)
        self.main_layout.addLayout(self.layout_buttons)
        self.layout_buttons.addWidget(self.btn_add)
        self.layout_buttons.addWidget(self.btn_clean)

        self.layout_buttons.addStretch()

        self.layout_buttons.addWidget(self.icon_color_to_delete)

        self.rc_delete_menu.addMenu(self.rc_delete_menu_choose_color_to_delete_menu)
        for action in self.rc_delete_menu_choose_color_to_delete_menu_choices.keys():
            self.rc_delete_menu_choose_color_to_delete_menu.addAction(action)

    def setup_connections(self):
        """
        Sets up the connections between the widgets and their functions
        """
        self.btn_add.clicked.connect(self.add_task)
        self.lw_tasks.itemClicked.connect(lambda lw_item: lw_item.toggle_state())
        self.btn_clean.clicked.connect(self.clean_task)
        self.icon_color_to_delete.clicked.connect(self.open_color_to_delete_menu)

        for action, color in self.rc_delete_menu_choose_color_to_delete_menu_choices.items():
            action.triggered.connect(self.make_change_color_to_delete(color))

    def add_task(self):
        """
        Adds a task to the taskList
        """
        task_name, ok = QtWidgets.QInputDialog.getText(self,
                                                       "Ajouter une tâche",
                                                       "Nom de la tâche :",
                                                       echo=QtWidgets.QLineEdit.Normal)
        if ok and task_name:
            self.patient.add_task(name=task_name)
            self.get_tasks()

    def make_change_color_to_delete(self, color):
        """
        Makes the function change_color_to_delete for each button of the context menu
        :param color: str the color of the button clicked in the context menu
        :return: func the function that was created
        """
        def change_color_to_delete():
            """
            sets the color that has to be deleted by the trash icon to be the one contained in the variable 'color'
            """
            self.patient.color_to_delete = color
            self.patient.save_patient()
            self.icon_color_to_delete.setIcon(QtGui.QIcon(self.ctx.get_resource(f"colors/{color}.svg")))

        return change_color_to_delete

    def clean_task(self):
        """ Method to suppress all the tasks that are marked as done """

        deletable_tasks = []

        for i in range(self.lw_tasks.count()):
            lw_item = self.lw_tasks.item(i)
            if lw_item.color_name == self.patient.color_to_delete:
                deletable_tasks.append(lw_item)

        if deletable_tasks:
            self.delete_tasks_confirmation_box.exec_()
            if self.delete_tasks_confirmation_box.clickedButton() == self.btn_yes_task:
                for task in deletable_tasks:
                    self.patient.remove_task(name=task.name)

        self.get_tasks()
        self.lw_tasks.repaint()  # Rafraichissement pour éviter les pbs d'affichage

    def get_tasks(self):
        """
        Gets a dict of all the tasks linked to the patient
        """
        self.lw_tasks.clear()
        tasks = self.patient.tasks
        for name, color in tasks.items():
            TaskItem(patient=self.patient, name=name, color_name=color, list_widget=self.lw_tasks)
            self.patient.save_patient()

    def open_color_to_delete_menu(self):
        """
        triggers the opening of the color_to_delete_menu, that allows the user to chose which color to delete when pressing the trash icon
        """
        pos = self.cursor().pos()
        self.rc_delete_menu.exec_(pos)
