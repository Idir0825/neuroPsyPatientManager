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
            patient = Patient(guid=guid,
                              last_name=last_name,
                              first_name=first_name,
                              birth_date=birth_date,
                              description=description,
                              notes=notes,
                              tasks=tasks,
                              tests=tests,
                              color_to_delete=color_to_delete,
                              creation_date=creation_date)
            patients_list.append(patient)
    return patients_list


class Patient:
    """ Creates an instance of a Patient """

    def __init__(self, guid="", last_name="", first_name="", birth_date="", description="", notes={},
                 tests={}, tasks={}, color_to_delete="red", creation_date=""):

        """
        Constructor for the class patient.

        :param guid: str unique universal identifier of the patient
        :param last_name: str name of the patient
        :param first_name: str first name of the patient
        :param birth_date: str birthdate of the patient
        :param description:
        :param notes: dict all the notes that the patient got for any test that he passed
        :param tests: dict each item of the dict is a tuple with (payedornot, date) or (whodidthetest, dateornot)
        :param tasks: dict tasks linked to the patient
        :param color_to_delete: str the color that will be delete when pressing the trash icon in the taskList
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
    def description(self):
        """
        private property containing the description of the patient
        :return: the value contained by the property description in the class Patient
        """
        return self._description

    @description.setter
    def description(self, des):
        """
        setter of the property description in the class Patient
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

        :return: The path to the patient's file
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
        logging.info("La tâche a été supprimé correctement")
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

            data = {"last_name":     self.last_name,
                    "first_name":    self.first_name,
                    "birth_date":    self.birth_date,
                    "description":   self.description,
                    "notes":         self.notes,
                    "tasks":         self.tasks,
                    "tests":         self.tests,
                    "color_to_delete": self.color_to_delete,
                    "creation_date": self.created_on
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
        Changes the status of a task and the color of the line it is written on in the list
        :param name: str the name of the task that is being worked on
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
            logging.error(f"La tâche {name} n'existe pas dans la liste de tâches du patient {self.last_name} {self.first_name}.")
            return False

        self.tasks[name] = color
        self.save_patient()
        return True, color


if __name__ == '__main__':
    idir = Patient(last_name="Houari", first_name="Idir", birth_date="1996-07-25",
                   description="Je suis un garçon de 24 ans qui travaille dans une école.")
    idir.save_patient()
    print(idir)
    print(idir.description)
