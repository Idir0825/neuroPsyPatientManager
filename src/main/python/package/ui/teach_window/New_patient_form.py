
from tkinter import ttk
from Frames.New_patient_form_frame import New_patient_form_frame
from Frames.New_patient_grades import New_patient_grades


""" This is the patient form itself """

class New_patient_form(ttk.Frame):

	def __init__(self, container, **kwargs):
		super().__init__(container, **kwargs)

		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		# -- All the form --
		self.all_form_frame = ttk.Frame(self, style="White.TFrame")
		self.all_form_frame.columnconfigure(0, weight=1)
		self.all_form_frame.rowconfigure(0, weight=1)
		self.all_form_frame.rowconfigure(1, weight=1)
		self.all_form_frame.grid(row=0, column=0, sticky="NESW") # Ne pas toucher au sticky ici

		# -- Form for new patients --
		self.new_patient_form_frame = New_patient_form_frame(self.all_form_frame, container, style="White.TFrame")
		self.new_patient_form_frame.pack(expand=True, fill="both") # Ne pas toucher au sticky ici

		# -- Grades for new patients --
		self.new_patient_grades_frame = New_patient_grades(self.all_form_frame, container, style="White.TFrame")
		self.new_patient_grades_frame.pack(expand=True, fill="both") # Ne pas toucher au sticky ici
