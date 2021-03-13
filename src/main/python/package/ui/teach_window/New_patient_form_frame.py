import tkinter as tk
from tkinter import ttk
from datetime import date

""" This is the part of the patient form that contains the infos on the patient """

class New_patient_form_frame(ttk.Frame):

	def __init__(self, container, master, **kwargs): # container = new_patient_form, master = new_patient, controller = main
		super().__init__(container, **kwargs)

		self.master = master

		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		# -- Formulaire identité du patient --
		self.formulaire_frame = ttk.Frame(self, style="White.TFrame")
		self.formulaire_frame.grid(row=0, column=0, sticky="NESW")

		self._make_identity_form(master)
		# -- Formulaire identité du patient end --

		for i in range(0, self.formulaire_frame.grid_size()[1]):
			self.formulaire_frame.rowconfigure(i, weight=1)

		for i in range(0, self.formulaire_frame.grid_size()[0]):
			self.formulaire_frame.columnconfigure(i, weight=1)

	def _make_identity_form(self, master):

		identity_frame = ttk.Frame(self.formulaire_frame, style="White.TFrame")
		identity_frame.grid(row=1, column=0, pady=2, padx=2, sticky="NESW")

		# -- Left bloc --
		left_frame = ttk.Frame(identity_frame, style="White.TFrame")
		left_frame.pack(expand=True, side="left")

		# -- Right bloc --
		right_frame = ttk.Frame(identity_frame, style="White.TFrame")
		right_frame.pack(expand=True, side="right")

		# -- Name --
		name_frame_container = ttk.Frame(left_frame)
		name_frame_container.pack(expand=True, fill="both", pady=5)
		name_frame = ttk.Frame(name_frame_container, style="White.TFrame")
		name_frame.pack(expand=True, fill="both", side="left")
		name_label = ttk.Label(name_frame, text="Nom ", style="FormElement.TLabel")
		name_label.pack(side="left")
		self.name_input = ttk.Entry(name_frame, textvariable=master.last_name, width=20, style="FormEntry.TEntry", justify="center")
		self.name_input.pack(side="left", ipady=3)

		# -- FirstName --
		first_name_frame_container = ttk.Frame(left_frame)
		first_name_frame_container.pack(expand=True, fill="both", pady=5)
		first_name_frame = ttk.Frame(first_name_frame_container, style="White.TFrame")
		first_name_frame.pack(expand=True, fill="both", side="left")
		first_name_label = ttk.Label(first_name_frame, text="Prénom ", style="FormElement.TLabel")
		first_name_label.pack(side="left")
		self.first_name_input = ttk.Entry(first_name_frame, textvariable=master.first_name, width=20, style="FormEntry.TEntry", justify="center")
		self.first_name_input.pack(ipady=3, side="left")

		# -- BirthDate --
		l, v = ("Date de naissance ", (master.jour, master.mois, master.annee))

		birth_date_frame_container = ttk.Frame(left_frame)
		birth_date_frame_container.pack(expand=True, fill="both", pady=5)
		birth_date_frame = ttk.Frame(birth_date_frame_container, style="White.TFrame")
		birth_date_frame.pack(expand=True, fill="both", side="left")

		my_label_temp = ttk.Label(birth_date_frame, text=l, style="FormElement.TLabel")
		my_label_temp.pack(padx=(0, 2), side="left", fill="x", expand=True)

		self.day_input = ttk.Combobox(birth_date_frame, textvariable=v[0], width=5, style="FormBDate.TCombobox", justify="center")
		self.day_input["values"] = [i for i in range(1, 32)]
		self.day_input.set("Jour")
		self.day_input.pack(padx=(0, 0), side="left", ipady=3)

		self.month_input = ttk.Combobox(birth_date_frame, textvariable=v[1], width=5, style="FormBDate.TCombobox", justify="center")
		self.month_input["values"] = [i for i in range(1, 13)]
		self.month_input.set("Mois")
		self.month_input.pack(padx=(2, 2), side="left", ipady=3)

		self.year_input = ttk.Combobox(birth_date_frame, textvariable=v[2], width=6, style="FormBDate.TCombobox", justify="center")
		self.year_input["values"] = [i for i in range(2000, date.today().year + 1)]
		self.year_input.set("Année")
		self.year_input.pack(padx=(0, 20), side="left", ipady=3)

		# -- Date de passation --
		date_de_passation_frame_container = ttk.Frame(right_frame, style="White.TFrame")
		date_de_passation_frame_container.pack(expand=True, fill="both", pady=5)
		date_de_passation_frame = ttk.Frame(date_de_passation_frame_container, style="White.TFrame")
		date_de_passation_frame.pack(expand=True, fill="both", side="left")
		date_de_passation_label = ttk.Label(date_de_passation_frame, text="Date de passation ", style="FormElement.TLabel")
		self.date_de_passation_entry = ttk.Entry(date_de_passation_frame, textvariable=master.passation_date, style="FormEntry.TEntry", justify="center")
		self.date_de_passation_entry.pack(padx=(0, 5), side="right", ipady=3)
		date_de_passation_label.pack(padx=(0, 2), side="right")

		# -- Age --
		age_frame_container = ttk.Frame(right_frame, style="White.TFrame")
		age_frame_container.pack(expand=True, fill="both", pady=5)
		age_frame = ttk.Frame(age_frame_container, style="White.TFrame")
		age_frame.pack(expand=True, fill="both", side="left")
		age_label = ttk.Label(age_frame, text="Age ", style="FormElement.TLabel")
		calculated_age_label = ttk.Entry(age_frame, textvariable=master.age_text, style="FormEntry.TEntry", justify="center")
		calculated_age_label["state"] = "readonly"
		calculated_age_label.pack(padx=(0, 5), side="right", ipady=3)
		age_label.pack(padx=(5, 2), side="right")

		# -- Age equivalent --
		equivalent_age_frame_container = ttk.Frame(right_frame, style="White.TFrame")
		equivalent_age_frame_container.pack(expand=True, fill="both", pady=5)
		equivalent_age_frame = ttk.Frame(equivalent_age_frame_container, style="White.TFrame")
		equivalent_age_frame.pack(expand=True, fill="both", side="left")
		equivalent_age_label = ttk.Label(equivalent_age_frame, text="Age équivalent ", style="FormElement.TLabel")
		calculated_equivalent_age_label = ttk.Entry(equivalent_age_frame, textvariable=master.equivalent_age_text, style="FormEntry.TEntry", justify="center")
		calculated_equivalent_age_label["state"] = "readonly"
		calculated_equivalent_age_label.pack(padx=(0, 5), side="right", ipady=3)
		equivalent_age_label.pack(padx=(0, 2), side="right", expand=True)

		identity_frame.rowconfigure(0, weight=1)
		identity_frame.rowconfigure(1, weight=1)
		identity_frame.columnconfigure(0, weight=1)
		identity_frame.columnconfigure(1, weight=1)
		identity_frame.columnconfigure(2, weight=1)
		identity_frame.columnconfigure(3, weight=1)
