import tkinter as tk
from tkinter import ttk
from Frames.Edit_patient_list import Patient_list_window


class Edit_patient(ttk.Frame):

	def __init__(self, container, **kwargs):
		super().__init__(container, **kwargs)

		self.rowconfigure(1, weight=1)
		self.columnconfigure(0, weight=1)

		# -- Navbar --
		self.button_frame = ttk.Frame(self, padding=10)
		self.button_frame.grid(row=0, column=0, sticky="NESW")

		self.new_patient_button = ttk.Button(
			self.button_frame,
			text="Ajouter un patient",
			command=lambda: container.show_frame("New_patient_window"),
			style="NavbarButton.TButton"
			)
		self.new_patient_button.grid(row=0, column=0, sticky="NW", padx=5, pady=5)

		# -- List of patients --
		self.patients_list_window = Patient_list_window(self, background="#63F908")
		self.patients_list_window.grid(row=1, column=0, sticky="NESW")
