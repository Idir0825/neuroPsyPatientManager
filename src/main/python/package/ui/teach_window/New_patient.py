import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import messagebox

from datetime import date, datetime
import numpy as np

from Frames.New_patient_form import New_patient_form
from Frames.Gradient_Frames import GradientFrameUpToBottom

from TeachBusiness.TablesManager import pourcentage_voulu
from TeachDal.TestDal import TestDal
from TeachModels.Patient import Patient
from TeachDal.PatientDal import PatientDal
from TeachDal.TestForPatientDal import TestForPatientDal
from TeachModels.TestForPatient import TestResult

from PDFGeneration.Save_pdf import Results_as_pdf

""" This is the new patient page itself, keeps track of all the variables values """

class New_patient(ttk.Frame):

	def __init__(self, container, **kwargs):
		super().__init__(container, **kwargs)

		self.container = container

		self.rowconfigure(1, weight=1)
		self.columnconfigure(0, weight=1)

		# -- Navbar --
		self._make_navbar(container)
		# -- BottomButtons --
		self._make_buttons_bar(container)
		""" -- Form for new patients --"""

		# -- Setting the variables --
		self._reinitialize_values()

		# Putting the form in window
		self.new_patient_form = New_patient_form(self)
		self.new_patient_form.grid(row=1, column=0, sticky="NESW")

		self.new_patient_form.new_patient_form_frame.name_input.focus_set()

		""" -- Form for new patients end """

	def _make_navbar(self, container):
		# -- Navbar --
		self.button_frame = GradientFrameUpToBottom(self, container.COLOUR_PRIMARY, container.COLOUR_SECONDARY)
		self.button_frame.columnconfigure(0, weight=1)
		self.button_frame.rowconfigure(0, weight=1)
		self.button_frame.grid(row=0, column=0, sticky="NESW")

		self.edit_patient_button = ttk.Button(
			self.button_frame,
			text="Éditer un patient",
			command=lambda: self._show_frame("Edit_patient_window"),
			style="NavbarButton.TButton"
			)

		self.edit_patient_button.grid(row=0, column=0, sticky="NW", padx=15, pady=(15, 25))

	def _make_buttons_bar(self, container):
		# -- Buttonsbar --
		self.button_frame = GradientFrameUpToBottom(self, container.COLOUR_SECONDARY, container.COLOUR_PRIMARY)
		self.button_frame.columnconfigure(0, weight=1)
		self.button_frame.rowconfigure(0, weight=1)
		self.button_frame.grid(row=2, column=0, sticky="NESW")

		self.save_button = ttk.Button(
			self.button_frame,
			text="Sauvegarder",
			command=self._save_patient,
			style="NavbarButton.TButton"
			)
		self.generate_pdf_button = ttk.Button(
			self.button_frame,
			text="Générer PDF",
			command=self._make_pdf,
			style="NavbarButton.TButton"
			)

		self.generate_pdf_button.pack(side="right", padx=(5, 15), pady=(50, 15))
		self.save_button.pack(side="right", pady=(50, 15))

	def _show_frame(self, window):

		if self._check_if_any_grade_is_defined() is True or self._check_if_any_info_is_defined() is True:
			answer = messagebox.askyesnocancel("Données en attente",
			                                   "Voulez-vous réinitialiser les éléments de la page ? "
			                                   "Tout élément non sauvegardé sera perdu.",
			                                   icon="warning")
			if answer is True:
				self._reinitialize_values()
				self.container.show_frame(window)
			elif answer is False:
				self.container.show_frame(window)
			else:
				pass
		else:
			self.container.show_frame(window)

	def _reinitialize_values(self):
		# -- Setting the variables --
		self.last_name = tk.StringVar()
		self.first_name = tk.StringVar()

		self.jour = tk.StringVar()  # Input variable
		self.mois = tk.StringVar()  # Input variable
		self.annee = tk.StringVar()  # Input variable

		self.age_text = tk.StringVar()  # Output variable with calculated age
		self.age_text.set("N/D ans, N/D mois")
		self.equivalent_age_text = tk.StringVar()  # Output variable with calculated equivalent_age
		self.equivalent_age_text.set("N/D ans")
		self.passation_date = tk.StringVar()  # Output variable with calculated equivalent_age
		self.passation_date.set("jj-mm-aaaa")

		self.age_month = tk.IntVar()  # Used to calculate the age
		self.age_year = tk.IntVar()  # Used to calculate the age
		self.equivalent_age = tk.IntVar()  # Used to calculate the equivalent_age

		self.my_variables = {}

		for i in ["A", "C", "D", "F", "G", "J", "L", "O", "P", "R", "S", "T", "one", "four", "Z", "two", "three",
		          "AA"]:
			self.my_variables[i] = tk.DoubleVar()
			self.my_variables[i].trace("w", self._limit_size_float)

		for i in ["B", "E", "H", "I", "K", "M", "N", "Q", "U", "V", "W", "X", "Y", "BB"]:
			self.my_variables[i] = tk.IntVar()
			self.my_variables[i].trace("w", self._limit_size_int)

		for i in ["Bp", "Cp", "Gp", "Hp", "Ip", "Lp", "Tp", "Up", "Xp", "Yp", "Zp", "AAp", "BBp"]:
			self.my_variables[i] = tk.IntVar()

	def delete_passation_date_if_focus(self):

		""" Checks if the focus is on passation_date, removes its content if nothing was written """

		date_entry = self.new_patient_form.new_patient_form_frame.date_de_passation_entry
		date_variable = self.passation_date

		if self.focus_get() == date_entry and date_variable.get() == "jj-mm-aaaa":
			date_variable.set("")
		elif self.focus_get() != date_entry and date_variable.get() == "":
			date_variable.set("jj-mm-aaaa")

	def delete_birthdate_if_focus(self):

		""" Checks if the focus is on one of the elements of the birthdate, removes its content if nothing was written """

		day_input = self.new_patient_form.new_patient_form_frame.day_input
		month_input = self.new_patient_form.new_patient_form_frame.month_input
		year_input = self.new_patient_form.new_patient_form_frame.year_input

		if self.focus_get() == day_input and day_input.get() == "Jour":
			day_input.set("")
		elif self.focus_get() != day_input and day_input.get() == "":
			day_input.set("Jour")

		if self.focus_get() == month_input and month_input.get() == "Mois":
			month_input.set("")
		elif self.focus_get() != month_input and month_input.get() == "":
			month_input.set("Mois")

		if self.focus_get() == year_input and year_input.get() == "Année":
			year_input.set("")
		elif self.focus_get() != year_input and year_input.get() == "":
			year_input.set("Année")

	def make_isoformat(self):

		""" Checks if the cursor is in the passation_date entry widget
		adds '-' on defined places to create a date of format 'dd-mm-yyyy' """

		date_entry = self.new_patient_form.new_patient_form_frame.date_de_passation_entry
		date_variable = self.passation_date
		if self.focus_get() == date_entry:
			if len(date_variable.get()) == 2 and date_variable.get()[-1] != "-":
				date_variable.set(date_variable.get() + "-")
				date_entry.icursor(5)

			elif len(date_variable.get()) == 5 and date_variable.get()[-1] != "-":
				date_variable.set(date_variable.get() + "-")
				date_entry.icursor(8)
			elif len(date_variable.get()) >= 11:
				date_variable.set(date_variable.get()[0:10])
			else:
				pass

	def _limit_size_float(self, *args):
		""" Limits the size of float entries to a defined number of characters """
		try:
			value = str(self.my_variables[args[0]].get())
			if len(value) > 4:
				self.my_variables[args[0]].set(np.around(float(value), 1))
		except:
			pass

	def _limit_size_int(self, *args):
		""" Limits the size of int entries to a defined number of characters """
		try:
			value = str(self.my_variables[args[0]].get())
			if len(value) > 2:
				self.my_variables[args[0]].set(int(value[:2]))
		except:
			pass

	def _calculate_age(self):
		# Returns the age of the patient in years and months
		passationDate_temp = date.fromisoformat(datetime.strptime(self.passation_date.get(), "%d-%m-%Y").strftime("%Y-%m-%d"))
		today = passationDate_temp
		years = today.year - self.birthDate.year - \
		        ((today.month, today.day) < (self.birthDate.month, self.birthDate.day))
		if today.month > self.birthDate.month:
			months = today.month - self.birthDate.month
		else:
			months = 12 - (self.birthDate.month - today.month)
			if months == 12:
				if today.day>self.birthDate.day:
					months = 0
				else:
					months = 11
			else:
				pass

		return years, months

	def _calculate_equivalent_age(self):
		# Returns the equivalent age of the patient on the conversion tables (6, 7, 9 or 11)

		if 7 > self.age[0] >= 6:
			eage = 6
		elif 9 > self.age[0] >= 7:
			eage = 7
		elif 11 > self.age[0] >= 9:
			eage = 9
		elif self.age[0] < 6:
			eage = 6
		else:
			eage = 11

		return eage

	def _set_values(self, j, m, y):

		if y.get() != "0" and m.get() != "0" and j.get() != "0" and y.get() != "Année" and m.get() != "Mois" and \
				j.get() != "Jour":
			self.birthDate = date(int(y.get()), int(m.get()), int(j.get()))
			self.age = self._calculate_age()
			self.equivalent_age.set(self._calculate_equivalent_age())
			self.age_year.set(self.age[0])
			self.age_month.set(self.age[1])
			self.age_text.set(f"{self.age_year.get()} ans, {self.age_month.get()} mois")
			self.equivalent_age_text.set(f"{self.equivalent_age.get()} ans")

	def _update_birthdate_values(self):
		self._set_values(self.jour, self.mois, self.annee)

	def _calculate_results(self, v):

		if v["B"].get() != 0:
			v["C"].set(np.around(v["A"].get() / v["B"].get(), 2))

		if v["E"].get() != 0:
			if v["E"].get() < 15:
				# If E is smaller than 15
				if not self.new_patient_form.new_patient_grades_frame.recherche_dans_le_ciel_frame.e_smaller_than_fifteen.winfo_ismapped():
					# If e_smaller_than_fifteen label isn't shown in the window
					self.new_patient_form.new_patient_grades_frame.recherche_dans_le_ciel_frame.e_smaller_than_fifteen.pack()
					# Show the label
			else:
				# If E is higher than 15, remove the label from the window but don't delete it
				self.new_patient_form.new_patient_grades_frame.recherche_dans_le_ciel_frame.e_smaller_than_fifteen\
					.forget()

			v["F"].set(np.around(v["D"].get() / v["E"].get(), 2))

		v["G"].set(np.around(v["C"].get() - v["F"].get(), 2))

		if v["I"].get() > 3:
			if v["K"].get() != 0:
				v["L"].set(np.around(v["J"].get() / v["K"].get(), 2))
		else:
			v["L"].set(0.0)

		if v["N"].get() != 0:
			v["O"].set(np.around(v["M"].get() / v["N"].get(), 2))

		if v["Q"].get() != 0:
			v["R"].set(np.around(v["P"].get() / v["Q"].get(), 2))

		if v["O"].get() != 0:
			v["S"].set(np.around(v["R"].get() / v["O"].get(), 2))

		v["T"].set(np.around(v["S"].get() - v["C"].get(), 2))
		v["X"].set(np.around(v["V"].get() + v["W"].get(), 2))
		v["Z"].set(np.around(v["one"].get() + v["four"].get(), 2))
		v["AA"].set(np.around(v["two"].get() + v["three"].get(), 2))

	def _calculate_percentils(self, v):
		v["Bp"].set(pourcentage_voulu("B", self.equivalent_age.get(), v["B"].get()))
		v["Cp"].set(pourcentage_voulu("C", self.equivalent_age.get(), v["C"].get()))
		v["Gp"].set(pourcentage_voulu("G", self.equivalent_age.get(), v["G"].get()))
		v["Hp"].set(pourcentage_voulu("H", self.equivalent_age.get(), v["H"].get()))
		v["Ip"].set(pourcentage_voulu("I", self.equivalent_age.get(), v["I"].get()))
		v["Lp"].set(pourcentage_voulu("L", self.equivalent_age.get(), v["L"].get()))
		v["Tp"].set(pourcentage_voulu("T", self.equivalent_age.get(), v["T"].get()))
		v["Up"].set(pourcentage_voulu("U", self.equivalent_age.get(), v["U"].get()))
		v["Xp"].set(pourcentage_voulu("X", self.equivalent_age.get(), v["X"].get()))
		v["Yp"].set(pourcentage_voulu("Y", self.equivalent_age.get(), v["Y"].get()))
		v["Zp"].set(pourcentage_voulu("Z", self.equivalent_age.get(), v["Z"].get()))
		v["AAp"].set(pourcentage_voulu("AA", self.equivalent_age.get(), v["AA"].get()))
		v["BBp"].set(pourcentage_voulu("BB", self.equivalent_age.get(), v["BB"].get()))

	def _check_if_all_infos_are_defined(self):
		""" This function checks if all the patient infos are defined and returns True if they are all defined """
		for i in (self.last_name, self.first_name, self.jour, self.mois, self.annee):
			if i.get() == '':
				return False
			elif int(self.jour.get())<1 or int(self.jour.get())>31 or int(self.mois.get())<1 or int(self.mois.get())>12:
				return False
		return True

	def _check_if_all_grades_are_defined(self):
		""" This function checks if all the grades are defined returns True if they are all defined """
		p = ["Bp", "Cp", "Gp", "Hp", "Ip", "Lp", "Tp", "Up", "Xp", "Yp", "Zp", "AAp", "BBp"]
		for i in p:
			if self.my_variables[i].get() == 0 or self.my_variables[i].get() == 0.0:
				return False
		return True

	def _check_if_any_grade_is_defined(self):
		""" This function checks if any grade is defined returns True if any is defined """
		for i in self.my_variables.values():
			if i.get() != 0 or i.get() != 0.0:
				return True
		return False

	def _check_if_any_info_is_defined(self):
		""" This function checks if any of the patient infos is defined and returns True if any is defined """
		for i in (self.last_name, self.first_name, self.jour, self.mois, self.annee):
			if i.get() != '':
				return True
		return False

	def _check_if_grades_contain_letters(self):
		""" This function checks if any of the grades entry fields contains a letter and returns True if any entry
		does"""
		for i in self.my_variables.values():
			try:
				test = float(i.get())
			except:
				return True
		return False

	def _save_patient(self):
		""" This function saves the new patient and its results in the DB """
		if self._check_if_all_grades_are_defined() == True and self._check_if_all_infos_are_defined() == True and \
				self._check_if_grades_contain_letters() == False:
			# Checking if all the grades have been defined, if all of the patients infos have been defined, and if any
			# grade entry field contains a letter
			if not PatientDal.check_patient_exists(self.last_name.get(), self.first_name.get(), self.birthDate):
				# Checking if a patient with the same name and birthdate exists in the DB
				# Making the date in the right format
				passationDate_temp = date.fromisoformat(datetime.strptime(self.passation_date.get(), "%d-%m-%Y").strftime("%Y-%m-%d"))
				patient_temp = Patient(self.last_name.get(), self.first_name.get(), self.birthDate, passationDate_temp)
				PatientDal.add_patient(patient_temp)
				self._save_patient_results(patient_temp)
			else:
				messagebox.showerror("Conflit dans la base de données",
				                     "Un patient avec les mêmes coordonnées existe dans la base de données. "
				                     "Pour le modifier veuillez utiliser l'outil d'édition d'un patient.")
		else:
			# If an error occurs
			if self._check_if_grades_contain_letters():
				# Check if a field contains a letter
				messagebox.showerror("Valeurs invalides", "Une note ne peut pas contenir de lettre.")
			elif self._check_if_all_infos_are_defined() == False:
				messagebox.showerror("Valeurs invalides", "Vérifier les informations du patient.")
			else:
				# If no field contains a letter, tell the user that all the fields aren't defined
				messagebox.showerror("Valeurs invalides", "Tous les champs n'ont pas été définis.")

	def _save_patient_results(self, patient_temp):
		""" This function saves the patient's results in the DB """

		tests = TestDal.get_all_tests() # Getting the test names and ids
		patient_results = {}
		try:
			for test in tests:
				patient_results[test] = TestResult(testId=tests[test],  # TestResult is the class containing a result
				                                   note=self.my_variables[test].get(),
				                                   patientId=patient_temp.Id,
				                                   testName=test)  # Making a Dict containing all the results
		except Exception as error:
			print(error)
			messagebox.showerror("Valeurs invalides", error)

		for result in patient_results.values():  # Calling the database saving function for each testresult (28 times,
			# this needs to be optimized)
			TestForPatientDal.add_test_result(result)

	def _results_for_graph(self):

		results = {
			"Sélective":
				{
					"B": self.my_variables["Bp"].get(), "C": self.my_variables["Cp"].get(),
					"G": self.my_variables["Gp"].get(), "U": self.my_variables["Up"].get()
					},
			"Soutenue":
				{"H": self.my_variables["Hp"].get(), "BB": self.my_variables["BBp"].get()},
			"Divisée":
				{"X": self.my_variables["Xp"].get(), "T": self.my_variables["Tp"].get()},
			"Flexibilité":
				{
					"I": self.my_variables["Ip"].get(), "L": self.my_variables["Lp"].get(),
					"Z": self.my_variables["Zp"].get(), "AA": self.my_variables["AAp"].get()
					},
			"Ini":
				{"Y": self.my_variables["Yp"].get()}
			}

		return results

	@staticmethod
	def file_save():
		f = filedialog.askdirectory()
		return f

	def _make_pdf(self):

		if self._check_if_all_grades_are_defined() == True and self._check_if_all_infos_are_defined() == True and \
				self._check_if_grades_contain_letters() == False:
			# Checking if all the grades have been defined, if all of the patients infos have been defined, and if any
			# grade entry field contains a letter
			passationDate_temp = date.fromisoformat(datetime.strptime(self.passation_date.get(), "%d-%m-%Y").strftime("%Y-%m-%d"))
			patient_temp = Patient(self.last_name.get(), self.first_name.get(), self.birthDate, passationDate_temp)
			saving_location = self.file_save()

			if saving_location == '':
				pass
			else:
				results_for_graph = self._results_for_graph()
				Results_as_pdf(patient_temp, results_for_graph, self.my_variables, saving_location)

		else:
			# If an error occurs
			if self._check_if_grades_contain_letters():
				# Check if a field contains a letter
				messagebox.showerror("Valeurs invalides", "Une note ne peut pas contenir de lettre.")
			elif self._check_if_all_infos_are_defined() == False:
				messagebox.showerror("Valeurs invalides", "Vérifier les informations du patient.")
			else:
				# If no field contains a letter, tell the user that all the fields aren't defined
				messagebox.showerror("Valeurs invalides", "Tous les champs n'ont pas été définis.")

	def update_dates(self):

		try:
			self.make_isoformat()
			self.delete_passation_date_if_focus()
			self.delete_birthdate_if_focus()
		except Exception as error:
			print(error)

	def update_all(self):

		self.update_dates()

		try:
			self._update_birthdate_values()
			self._calculate_results(self.my_variables)
			self._calculate_percentils(self.my_variables)
		except Exception as error:
			print(error)

		self.after(100, self.update_all)