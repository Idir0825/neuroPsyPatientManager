import tkinter as tk
from tkinter import ttk

class GradientFrameUpToBottom(tk.Canvas):
	""" A gradient frame which uses a canvas to draw the background """

	def __init__(self, parent, color1, color2, **kwargs):
		tk.Canvas.__init__(self, parent, highlightthickness=0, **kwargs)
		self.color1 = color1 # Color on top of the frame
		self.color2 = color2 # Color at the bottom of the frame
		self.bind("<Configure>", self._draw_gradient)

	def _draw_gradient(self, event=None):
		""" Draw the gradient """
		self.delete("gradient")
		width = self.winfo_width()
		height = self.winfo_height()
		limit = height # Sets the number of steps to make the gradient
		(r1, g1, b1) = self.winfo_rgb(self.color1) #Finding the rgb of the colors
		(r2, g2, b2) = self.winfo_rgb(self.color2)
		r_ratio = float(r2 - r1) / limit
		g_ratio = float(g2 - g1) / limit
		b_ratio = float(b2 - b1) / limit

		for i in range(0, int(limit+1)):
			nr = int(r1 + (r_ratio * i))
			ng = int(g1 + (g_ratio * i))
			nb = int(b1 + (b_ratio * i))
			color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
			self.create_line(0, i, width, i, tags=("gradient",), fill=color)
		self.lower("gradient")

class GradientFrameLeftToRight(tk.Canvas):
	""" A gradient frame which uses a canvas to draw the background """

	def __init__(self, parent, controller, **kwargs):
		tk.Canvas.__init__(self, parent, highlightthickness=0, **kwargs)
		self._color1 = controller.COLOUR_SECONDARY
		self._color2 = controller.COLOUR_PRIMARY
		self.bind("<Configure>", self._draw_gradient)

	def _draw_gradient(self, event=None):
		""" Draw the gradient """
		self.delete("gradient")
		width = self.winfo_width()
		height = self.winfo_height()
		limit = height
		(r1, g1, b1) = self.winfo_rgb(self._color1)
		(r2, g2, b2) = self.winfo_rgb(self._color2)
		r_ratio = float(r2 - r1) / limit
		g_ratio = float(g2 - g1) / limit
		b_ratio = float(b2 - b1) / limit

		for i in range(0, limit+1):
			nr = int(r1 + (r_ratio * i))
			ng = int(g1 + (g_ratio * i))
			nb = int(b1 + (b_ratio * i))
			color = "#%4.4x%4.4x%4.4x" % (nr, ng, nb)
			self.create_line(i, 0, i, height, tags=("gradient",), fill=color)
		self.lower("gradient")