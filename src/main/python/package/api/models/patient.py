""" Model of the object patient for the app neuroPsychoPatientManager """

import os
from pathlib import Path
import json
import logging
from glob import glob
import datetime as dt
import uuid
from itertools import cycle, dropwhile

PATIENTS_PATH = os.path.join(Path.home(), ".patients")


def get_patients():
    """
        Returns a list of all the patients contained in the PATIENTS_PATH
    """
    if not os.path.exists(PATIENTS_PATH):
        logging.error(f"Aucun patient n'a été créé à l'heure actuelle, le chemin {PATIENTS_PATH} n'existe pas.")
        return False

    patients_list = []
    files = glob(os.path.join(PATIENTS_PATH, "*.json"))
    for file in files:
        with open(file, "r") as f:
            data = json.load(f)
            guid = os.path.splitext(os.path.basename(file))[0]
            last_name = data.get('last_name')
            first_name = data.get('first_name')
            birth_date = data.get('birth_date')
            description = data.get('description')
            notes = data.get('notes')
            tasks = data.get('tasks')
            tests = data.get('tests')
            color_to_delete = data.get('color_to_delete')
            creation_date = data.get('creation_date')
            temp_patient = Patient(guid=guid,
                                   last_name=last_name,
                                   first_name=first_name,
                                   birth_date=birth_date,
                                   description=description,
                                   tests=tests,
                                   notes=notes,
                                   tasks=tasks,
                                   color_to_delete=color_to_delete,
                                   creation_date=creation_date)
            patients_list.append(temp_patient)
    return patients_list


class Patient:
    """ Creates an instance of a Patient """

    def __init__(self, guid="", last_name="", first_name="", birth_date="", description="", notes={},
                 tests={}, tasks={}, color_to_delete="red", creation_date=""):

        """
        Constructor for the class patient

        :param guid: str unique universal identifier of the patient
        :param last_name: str name of the patient
        :param first_name: str first name of the patient
        :param birth_date: str birthdate of the patient
        :param description: str description of the patient
        :param tests: dict each item of the dict is a tuple with (name of the test, date) or (name of the test, dateornot)
        :param notes: dict each item of the dict is a dict with the notes of the test, the keys are the subtests' names
        :param tasks: dict the keys are the names of the tasks linked to the patient, the values are the colors of those tasks in the list of tasks
        :param creation_date: str date when the patient was created on the disk
        """

        if not guid:
            self.id = str(uuid.uuid4())
        else:
            self.id = guid

        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.description = description
        self.notes = notes
        self.tests = tests
        self.tasks = tasks
        self.color_to_delete = color_to_delete

        if not creation_date:
            self.created_on = dt.datetime.today().strftime("%d-%m-%Y")
        elif type(creation_date) is not str:
            raise Exception(
                    f"Le type de creation_date doit être str pour le patient {self.last_name} {self.first_name}.")
        else:
            self.created_on = creation_date

    def __str__(self):
        return f"Le patient {self.last_name} " \
               f"{self.first_name} né le {self.birth_date}"

    def __repr__(self):
        return f"{self.last_name} {self.first_name} ({self.id})"

    def add_task(self, name):
        """
        Adds a task to the patient's taskList

        :param name: str the name of the task to add
        :return: True if added successfully, otherwise returns False
        """
        if not os.path.exists(self.path):
            logging.error("Impossible d'ajouter une tâche pour un patient qui n'existe pas.")
            return False

        if name in self.tasks.keys():  # Vérifie si le nom est déjà pris par une des tâches de la liste de tâches
            logging.error("Une tâche avec le même nom existe déjà.")
            return False

        self.tasks[name] = "red"
        self.save_patient()
        return True

    def add_test(self, name: str, date: str, test_uuid=""):
        """
        Adds a test to the patient's testList. Gives the test a unique universal identifier that will be the key to
        accessing it in the tests dictionary

        :param test_uuid: str the uuid of the test if it has already been defined
        :param name: str name of the test to add
        :param date: str date when the test was passed
        :return: True if added successfully, otherwise returns False
        """
        if not test_uuid:
            temp_test_uuid = str(uuid.uuid4())
        else:
            temp_test_uuid = test_uuid

        if not os.path.exists(self.path):
            logging.error("Impossible d'ajouter un test pour un patient qui n'existe pas.")
            return False

        self.tests[temp_test_uuid] = (name, date)
        self.save_patient()
        return True

    def add_notes(self, uuid_of_the_test: str, notes_to_add: dict):
        """
        Adds the notes of a test to the patient's notes dictionary
        Notes can only be added to a test that was already created in the dict 'tests'

        :param uuid_of_the_test: str the uuid of the test that the notes are linked to
        :param notes_to_add: dict the notes to add to the dictionary
        :return: True if the notes are added successfully, else, returns False
        """
        if not os.path.exists(self.path):
            logging.error("Impossible d'ajouter des notes pour un patient qui n'existe pas.")
            return False

        if uuid_of_the_test not in self.tests.keys():
            logging.error("Impossible d'ajouter des notes pour un test que le patient n'a pas passé.")
            return False

        self.notes[uuid_of_the_test] = notes_to_add
        self.save_patient()
        return True

    def delete_patient(self):
        """
        Deletes the patient from the Disc

        :return: False if the suppression was not completed, True if the suppression was a success
        """

        os.remove(self.path)
        if os.path.exists(self.path):
            logging.error(f"Le/la patient(e) {self.last_name} {self.first_name} n'a pas pu être supprimé(e).")
            return False

        logging.info(f"Le/la patient(e) {self.last_name} {self.first_name} a bien été supprimé(e).")
        return True

    @property
    def color_to_delete(self):
        """
        private property containing the color the has to be deleted in the patient's taskList

        :return: the value contained by the property 'color_to_delete' in the class 'Patient'
        """
        return self._color_to_delete

    @color_to_delete.setter
    def color_to_delete(self, col):
        """
        setter of the property 'color_to_delete' in the class 'Patient'

        :param col: a string with the name of the color that will be deleted
        """

        if isinstance(col, str):
            self._color_to_delete = col
        else:
            raise TypeError("Valeur invalide, besoin d'une chaîne de caractères.")

    @property
    def description(self):
        """
        private property containing the description of the patient

        :return: the value contained by the property 'description' in the class 'Patient'
        """
        return self._description

    @description.setter
    def description(self, des):
        """
        setter of the property 'description' in the class 'Patient'

        :param des: a string/text to describe the patient, his behavior, his results ..
        """
        if isinstance(des, str):
            self._description = des
        else:
            raise TypeError("Valeur invalide, besoin d'une chaîne de caractères.")

    @property
    def path(self):
        """"
        Property containing the path to the patient's file

        :return: A string containing the path to the patient's file
        """
        return os.path.join(PATIENTS_PATH, self.id + ".json")

    def remove_task(self, name):
        """
        Removes the task 'name' from the patient's taskList

        :param name: str the name of the task to remove
        :return: False if it failed, else returns True
        """
        if not os.path.exists(self.path):
            logging.error("Impossible d'enlever une tâche pour un patient qui n'existe pas.")
            return False

        if name not in self.tasks.keys():
            logging.error("Cette tâche n'existe pas.")
            return False

        del self.tasks[name]
        logging.info("La tâche a été supprimée correctement")
        self.save_patient()
        return True

    def remove_test(self, test_uuid):
        """ Removes the test with uuid=test_uuid from the patient's testList """

        if not os.path.exists(self.path):
            logging.error("Impossible d'enlever un test pour un patient qui n'existe pas.")
            return False

        if test_uuid not in self.tests.keys():
            logging.error("Ce test n'existe pas.")
            return False

        del self.tests[test_uuid]
        self.remove_notes(test_uuid=test_uuid)
        logging.info("Le test a été supprimé correctement")
        self.save_patient()
        return True

    def remove_notes(self, test_uuid):
        """ Removes the notes of the test with uuid=test_uuid from the patient's notesList """

        if not os.path.exists(self.path):
            logging.error("Impossible d'enlever des notes pour un patient qui n'existe pas.")
            return False

        if test_uuid not in self.notes.keys():
            logging.error("Les notes pour ce test n'existe pas.")
            return False

        del self.notes[test_uuid]
        logging.info("Les notes de ce test ont été supprimées correctement")
        self.save_patient()
        return True

    def save_patient(self):
        """
        Saves the patient in the path defined by the variable self.path

        :return: True if the patient was saved successfully, else returns False
        """
        try:
            if not os.path.exists(PATIENTS_PATH):
                os.makedirs(PATIENTS_PATH)

            data = {"last_name":       self.last_name,
                    "first_name":      self.first_name,
                    "birth_date":      self.birth_date,
                    "description":     self.description,
                    "tests":           self.tests,
                    "notes":           self.notes,
                    "tasks":           self.tasks,
                    "color_to_delete": self.color_to_delete,
                    "creation_date":   self.created_on
                    }

            with open(self.path, "w") as f:
                json.dump(data, f, indent=4)
                logging.info(f"Le/la patient(e) {self.last_name} {self.first_name} a bien été mis(e) à jour.")
            return True

        except Exception as e:
            logging.error(f"Le/la patient(e) n'a pas pu être enregistré(e)")
            print(e)
            return False

    def set_task_status(self, name):
        """
        Changes the status of a task and the color of the line it is written on in the listWidget
        :param name: str the name of the task
        :return: False if the change failed, else it returns True and the new color of the task status
        """
        colors = ["red", "orange", "green", "blue", "purple"]
        colors_cycler = cycle(colors)
        skipped = dropwhile(lambda x: x != self.tasks[name], colors_cycler)  # drop the values until x == self.color
        next(skipped)
        color = next(skipped)

        if not os.path.exists(self.path):
            logging.error(f"Impossible de modifier les tâches pour un patient qui n'existe pas.")
            return False

        if name not in self.tasks.keys():
            logging.error(
                f"La tâche {name} n'existe pas dans la liste de tâches du patient {self.last_name} {self.first_name}.")
            return False

        self.tasks[name] = color
        self.save_patient()
        return True, color


if __name__ == '__main__':
    idir = Patient(last_name="Houari", first_name="Idir", birth_date="25-07-1996",
                   description="Je suis un garçon de 24 ans qui travaille dans une école.")
    idir.save_patient()
    idir.add_test("Banane", "14-03-2021")
    for u in idir.tests.keys():
        idir.add_notes(uuid_of_the_test=u, notes_to_add={"A": 15, "B": 20})
    idir.color_to_delete = "purple"

    patients = get_patients()
    for patient in patients:
        print(patient)
        print(patient.tests)
        print(patient.notes)
        print(" ")

    """ 
    my_keys = []
    for u in idir.tests.keys():
        my_keys.append(u)

    for i in my_keys:
        idir.remove_test(test_uuid=i)

    patients = get_patients()
    for patient in patients:
        print(patient)
        print(patient.tests)
        print(patient.notes)
        print(" ")
    """
