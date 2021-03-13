import tkinter as tk
from tkinter import ttk
from Frames.Gradient_Frames import GradientFrameUpToBottom
from PIL import Image, ImageTk

class First_window(ttk.Frame):
	def __init__(self, container, **kwargs):
		super().__init__(container, **kwargs)

		self.container = container

		self.columnconfigure(0, weight=1)
		self.rowconfigure(0, weight=1)

		self.gradient_frame = GradientFrameUpToBottom(self, self.container.COLOUR_PRIMARY, self.container.COLOUR_SECONDARY) # The class GradientFrameUpToBottom is a tkCanvas used to make a gradient in the bg
		self.gradient_frame.grid_propagate(False)
		self.gradient_frame.columnconfigure(0, weight=1)
		self.gradient_frame.rowconfigure(1, weight=1)
		self.gradient_frame.pack(expand=True, fill="both")

		self.image_teach = Image.open("static/tea-ch.jpg")
		self.image_teach = self.image_teach.resize((40, 40))
		self.photo_teach = ImageTk.PhotoImage(self.image_teach)
		self.app_label = ttk.Label(self.gradient_frame, text=" TEA-Ch", style="BigTitles.TLabel", compound="left", justify="left")
		self.app_label["image"] = self.photo_teach
		self.app_label.grid(row=0, column=0, padx=50, pady=50, sticky="W")

		self.test_label = ttk.Label(self.gradient_frame, text="Évaluation de l'attention", style="SmallTitles.TLabel", justify="left")
		self.test_label.grid(row=0, column=0, padx=50, pady=50, sticky="E")

		# -- Available options --
		self.button_frame = ttk.Frame(self.gradient_frame, padding=0, style="FirstPageButtons.TFrame")
		self.button_frame.grid(row=1, column=0)

		self.new_patient_button = ttk.Button(
			self.button_frame,
			text="Nouveau patient",
			command=lambda: container.show_frame("New_patient_window"),
			style="MyButton.TButton"
			)

		self.edit_patient_button = ttk.Button(
			self.button_frame,
			text="Éditer un patient",
			command=lambda: container.show_frame("Edit_patient_window"),
			style="MyButton.TButton"
			)

		self.new_patient_button.grid(row=0, column=0)
		self.edit_patient_button.grid(row=0, column=1, padx=(10, 0))
