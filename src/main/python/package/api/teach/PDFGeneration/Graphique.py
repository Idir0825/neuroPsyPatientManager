import matplotlib.pyplot as plt
import os

class Make_Graph:
	""" This class is used to generate the graph in the TEACH test PDF, it takes a list of dictionary with the needed
	grades separated in attention as an argument """

	def __init__(self, patient, notes, saving_location):

		self.SAVING_LOCATION = f"{saving_location}/Graphiques"
		# -- Making the graph --
		fig = plt.figure(1, figsize=(16, 9))
		ax = fig.add_subplot(111)

		try:
			self.label_group_bar(ax, notes)
		except Exception as error:
			print(error)

		if not os.path.exists(self.SAVING_LOCATION):

			try:
				os.makedirs(self.SAVING_LOCATION)
			except OSError:
				print("Creation of the directory %s failed" % self.SAVING_LOCATION)
			else:
				print("Successfully created the directory %s" % self.SAVING_LOCATION)
		else:
			pass

		try:
			fig.savefig(
				f"{self.SAVING_LOCATION}/{patient.lastName}_{patient.firstName}_{patient.birthDate}.png",
				bbox_inches='tight'
				)
		except Exception as error:
			print(error)

	def mk_groups(self, data):
		""" Function to make the graph labels. The data arg is a dictionary of dictionaries which first keys are the
		attention categories, second keys are the test names and items are the grades """
		my_data = []
		group_temp = []
		for attention in data.keys():
			group_temp.append((attention, len(data[attention])))
		my_data.append(group_temp)
		group_temp = []
		for attention in data.keys():
			for subtest, note in data[attention].items():
				group_temp.append((subtest, note))
		my_data.append(group_temp)

		return my_data

	def add_line(self, ax, xpos, ypos):
		""" Function to add a vertical line on the graph to separate labels categories here """
		line = plt.Line2D([xpos, xpos], [ypos - 1.1, ypos],
		                  transform=ax.transAxes, color='black', linewidth=1)
		line.set_clip_on(False)
		ax.add_line(line)

	def label_group_bar(self, ax, data):
		""" Function to make a graph while separating the labels for the TEACH test results """
		groups = self.mk_groups(data)
		xy = groups.pop()
		x, y = zip(*xy)
		ly = len(y)

		xminorticks = [1.5, 2.5, 3.5, 5.5, 7.5, 9.5, 10.5, 11.5]

		xticks = range(1, ly + 1)

		ax.scatter(xticks, y, color="#0A3F97",
		           marker="+", linewidth=2, s=200)  # Original = ax.plot(xticks, y, color="#9CFFCD", marker="D", markerfacecolor="#0A3F97")
		ax.set_xticks(xticks)
		ax.set_xticklabels(x, font="Bell MT", fontsize=15)
		ax.set_xlim(.5, ly + .5)

		# -- Both axis parameters --
		ax.grid(which="minor")

		# -- X axis parameters --
		ax.xaxis.set_tick_params(length=10, which="both", color="white")  # Customizing the x axis ticks markers
		ax.set_xticks(xminorticks, minor=True)

		# -- Y axis parameters --
		ax.set_yticks(range(0, 110, 10))  # Setting the scale of the y axis ticks
		ax.set_ylabel("Pourcentages cumulés", font="Bell MT", fontsize=20,
		              style='italic')  # Putting a title for the y axis

		scale = 1. / ly

		ypos = 1  # Defines where the vertical lines start 1=Top of the graph

		while groups:
			group = groups.pop()
			pos = 0  # Has to be 0
			for label, rpos in group:
				lxpos = (pos + 0.5 * rpos) * scale  # Defines the position of the attention labels
				ax.text(lxpos, -0.1, label, ha='center',
				        transform=ax.transAxes, font="Bell MT",
				        fontsize=15)  # Second arg has to be -0.1 to put the attention labels under the
				# subtest labels
				self.add_line(ax, pos * scale, ypos)
				pos += rpos
			self.add_line(ax, pos * scale, ypos)

"""x, y = [0,1,2,3,4,5,6,7,8,9], [9,8,7,6,5,4,3,2,1,0]

plt.scatter(x, y, color="#0A3F97",marker="+", linewidth=2, s=200)  # Original = ax.plot(xticks, y, color="#9CFFCD", marker="D", markerfacecolor="#0A3F97")
plt.show()"""