import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Patient_list_window(tk.Canvas):

	def __init__(self, container, *args, **kwargs):  # background is applied already from the Chat class
		super().__init__(container, *args, **kwargs, highlightthickness=0)

		self.maintenance_frame = ttk.Frame(self, style="Maintenance.TFrame")
		self.maintenance_frame.pack(expand=True, fill="both")

		self.warning_image = Image.open("static/warning.png")
		self.warning_image = self.warning_image.resize((64, 64))
		self.warning_photo = ImageTk.PhotoImage(self.warning_image)

		self.maintenance_label = ttk.Label(
			self.maintenance_frame,
			text="Cette partie est en cours de maintenance, navré pour la gêne occasionnée",
			style="Maintenance.TLabel",
			compound="left",
			justify="left")
		self.maintenance_label["image"] = self.warning_photo
		self.maintenance_label.pack(expand=True)

		"""self.list_frame = ttk.Frame(self, style="Test3.TFrame")
		self.list_frame.columnconfigure(0, weight=1)
		self.list_frame.rowconfigure(0, weight=1)

		self.scrollable_window = self.create_window((0, 0), window=self.list_frame, anchor="nw")

		self.list_container = ttk.Frame(self.list_frame)
		self.list_container.grid(row=0, column=0)

		self.test = ttk.Label(self.list_container, text="Je sers de test !")
		self.test.grid(row=0, column=0)

		def configure_scroll_region(event):
			self.configure(scrollregion=self.bbox("all"))  # sets the scroll region to be all the frame

		def configure_window_size(event):  # this sets the max width of the message_frame = width of the canvas, 
		no x scroll
			self.itemconfig(self.scrollable_window, width=self.winfo_width())

		self.bind("<Configure>", configure_window_size)  # Changes the width of message_frame when canvas size changes
		self.list_frame.bind("<Configure>", configure_scroll_region)
		# updates the scroll region when the frame gets longer
		self.bind_all("<MouseWheel>", self._onmousewheel)  # bind_All = does not matter which widget is selected

		scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
		scrollbar.grid(row=1, column=1, sticky="NS")

		self.configure(yscrollcommand=scrollbar.set)
		self.yview_moveto(1.0)  # moves the scrollbar to the top everytime the app is opened

	def _onmousewheel(self, event):
		self.yview("scroll", -int(event.delta / 120), "units")
		# this depends on the operating system, explanation in resizing video"""
