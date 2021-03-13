from tkinter import ttk
from PIL import Image, ImageTk

""" This the part of the patient form that contains the grades """

class New_patient_grades(ttk.Frame):

	def __init__(self, container, master, **kwargs): # container = new_patient_form, master = new_patient, controller = main
		super().__init__(container, **kwargs)

		self.master = master

		self.rowconfigure(0, weight=1)
		self.columnconfigure(0, weight=1)

		# -- Formulaire notes du patient --
		self.grades_frame = ttk.Frame(self, style="White.TFrame")
		self.grades_frame.grid(row=0, column=0, sticky="NESW")

		self._make_grades_form(master)
		# -- Formulaire notes du patient end --

		for i in range(0, self.grades_frame.grid_size()[1]):
			self.grades_frame.rowconfigure(i, weight=1)

		for i in range(0, self.grades_frame.grid_size()[0]):
			self.grades_frame.columnconfigure(i, weight=1)

		master.update_all()

	def _make_grades_form(self, master):
		self._make_recherche_dans_le_ciel_form(master)
		self._make_coup_de_fusil_form(master)
		self._make_les_petits_hommes_verts_frame(master)
		self._make_faire_deux_choses_a_la_fois_form(master)
		self._make_carte_geographique_form(master)
		self._make_ecouter_deux_choses_a_la_fois_form(master)
		self._make_marche_arrete_form(master)
		self._make_mondes_contraires_form(master)
		self._make_transmission_de_codes_form(master)

	def _make_recherche_dans_le_ciel_form(self, master):
		# -- Frame contenant tout le subtest --
		self.recherche_dans_le_ciel_frame = ttk.Frame(self.grades_frame, style="White.TFrame")
		self.recherche_dans_le_ciel_frame.grid(row=0, column=0, columnspan=4, pady=(10, 5), padx=2, sticky="NESW")

		# -- Titre du subtest --
		subtest_title_frame = ttk.Frame(self.recherche_dans_le_ciel_frame, style="Subtest.TFrame")
		subtest_title_frame.pack(expand=True, fill='both', pady=10, ipady=5, padx=70)

		subtesttitle = ttk.Label(subtest_title_frame, text="Recherche dans le ciel", style="Subtest.TLabel")
		subtesttitle.pack(fill="both", expand=True)

		# -- Notes du subtest --
		grades_frame = ttk.Frame(self.recherche_dans_le_ciel_frame, style="White.TFrame")
		grades_frame.pack(fill="both", pady=5)

		A_frame = ttk.Frame(grades_frame, style="White.TFrame")
		A_frame.pack(side="left", pady=2, padx=(70, 0), expand=True)
		A = ttk.Label(A_frame, text="A", style="GradeName.TLabel")
		A.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		A_input = ttk.Entry(A_frame, textvariable=master.my_variables["A"], width=5, style="EntryGrades.TEntry", justify="center")
		A_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		B_frame = ttk.Frame(grades_frame, style="White.TFrame")
		B_frame.pack(side="left", pady=2, expand=True)
		B = ttk.Label(B_frame, text="B", style="GradeName.TLabel")
		B.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		B_input = ttk.Entry(B_frame, textvariable=master.my_variables["B"], width=5, style="EntryGrades.TEntry", justify="center")
		B_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Bp_input = ttk.Entry(B_frame, textvariable=master.my_variables["Bp"], width=5, style="EntryGradesPercentage.TEntry", justify="center")
		Bp_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		C_frame = ttk.Frame(grades_frame, style="White.TFrame")
		C_frame.pack(side="left", pady=2, expand=True)
		C = ttk.Label(C_frame, text="C", style="GradeName.TLabel")
		C.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		C_input = ttk.Entry(C_frame, textvariable=master.my_variables["C"], width=5, style="EntryGrades.TEntry", justify="center")
		C_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Cp_input = ttk.Entry(C_frame, textvariable=master.my_variables["Cp"], width=5, style="EntryGradesPercentage.TEntry", justify="center")
		Cp_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		D_frame = ttk.Frame(grades_frame, style="White.TFrame")
		D_frame.pack(side="left", pady=2, expand=True)
		D = ttk.Label(D_frame, text="D", style="GradeName.TLabel")
		D.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		D_input = ttk.Entry(D_frame, textvariable=master.my_variables["D"], width=5, style="EntryGrades.TEntry", justify="center")
		D_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		E_frame = ttk.Frame(grades_frame, style="White.TFrame")
		E_frame.pack(side="left", pady=2, expand=True)
		E = ttk.Label(E_frame, text="E", style="GradeName.TLabel")
		E.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		E_input = ttk.Entry(E_frame, textvariable=master.my_variables["E"], width=5, style="EntryGrades.TEntry", justify="center")
		E_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		# Label that shows up in case E is smaller than fifteen
		self.warning_frame = ttk.Frame(self.recherche_dans_le_ciel_frame, style="White.TFrame")

		self.warning_image = Image.open("static/warning.png")
		self.warning_image = self.warning_image.resize((25, 25))
		self.warning_photo = ImageTk.PhotoImage(self.warning_image)

		self.recherche_dans_le_ciel_frame.e_smaller_than_fifteen = ttk.Label(
			self.warning_frame,
			text="La valeur de E est inférieure à 15",
			compound="left", justify="left", style="Esmallerthanfifteen.TLabel")
		self.recherche_dans_le_ciel_frame.e_smaller_than_fifteen["image"] = self.warning_photo
		self.recherche_dans_le_ciel_frame.e_smaller_than_fifteen.pack()
		self.warning_frame.pack()

		F_frame = ttk.Frame(grades_frame, style="White.TFrame")
		F_frame.pack(side="left", pady=2, expand=True)
		F = ttk.Label(F_frame, text="F", style="GradeName.TLabel")
		F.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		F_input = ttk.Entry(F_frame, textvariable=master.my_variables["F"], width=5, style="EntryGrades.TEntry", justify="center")
		F_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		G_frame = ttk.Frame(grades_frame, style="White.TFrame")
		G_frame.pack(side="left", pady=2, padx=(0, 70), expand=True)
		G = ttk.Label(G_frame, text="G", style="GradeName.TLabel")
		G.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		G_input = ttk.Entry(G_frame, textvariable=master.my_variables["G"], width=5, style="EntryGrades.TEntry", justify="center")
		G_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Gp_input = ttk.Entry(G_frame, textvariable=master.my_variables["Gp"], width=5, style="EntryGradesPercentage.TEntry", justify="center")
		Gp_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		for i in range(0, self.recherche_dans_le_ciel_frame.grid_size()[1]):
			self.recherche_dans_le_ciel_frame.rowconfigure(i, weight=1)
		for i in range(0, self.recherche_dans_le_ciel_frame.grid_size()[0]):
			self.recherche_dans_le_ciel_frame.columnconfigure(i, weight=1)

	def _make_coup_de_fusil_form(self, master):
		# -- Frame contenant tout le subtest --
		self.coup_de_fusil_frame = ttk.Frame(self.grades_frame, style="White.TFrame")
		self.coup_de_fusil_frame.grid(row=1, column=0, padx=2, pady=(2, 10), sticky="NESW")

		# -- Titre du subtest --
		subtest_title_frame = ttk.Frame(self.coup_de_fusil_frame, style="Subtest.TFrame")
		subtest_title_frame.pack(expand=True, fill='both', ipady=5, padx=(70, 15))

		subtesttitle = ttk.Label(subtest_title_frame, text="Coup de fusils", style="Subtest.TLabel")
		subtesttitle.pack(fill="both", expand=True)

		# -- Notes du subtest --
		grades_frame = ttk.Frame(self.coup_de_fusil_frame, style="White.TFrame")
		grades_frame.pack(fill="both", pady=5)

		H_frame = ttk.Frame(grades_frame, style="White.TFrame")
		H_frame.pack(side="left", pady=2, padx=(70, 30), expand=True)
		H = ttk.Label(H_frame, text="H", style="GradeName.TLabel")
		H.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		H_input = ttk.Entry(H_frame, textvariable=master.my_variables["H"], width=5, style="EntryGrades.TEntry", justify="center")
		H_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Hp_input = ttk.Entry(H_frame, textvariable=master.my_variables["Hp"], width=5, style="EntryGradesPercentage.TEntry", justify="center")
		Hp_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		for i in range(0, self.coup_de_fusil_frame.grid_size()[1]):
			self.coup_de_fusil_frame.rowconfigure(i, weight=1)
		for i in range(0, self.coup_de_fusil_frame.grid_size()[0]):
			self.coup_de_fusil_frame.columnconfigure(i, weight=1)

	def _make_les_petits_hommes_verts_frame(self, master):
		# -- Frame contenant tout le subtest --
		self.les_petits_hommes_verts_frame = ttk.Frame(self.grades_frame, style="White.TFrame")
		self.les_petits_hommes_verts_frame.grid(row=1, column=1, columnspan=3, pady=(2, 10), padx=2, sticky="NESW")

		# -- Titre du subtest --
		subtest_title_frame = ttk.Frame(self.les_petits_hommes_verts_frame, style="SubtestLabel.TFrame")
		subtest_title_frame.pack(expand=True, fill='both', ipady=5, padx=(15, 70))

		subtesttitle = ttk.Label(subtest_title_frame, text="Les petits hommes verts", style="Subtest.TLabel")
		subtesttitle.pack(fill="both", expand=True)

		# -- Notes du subtest --
		grades_frame = ttk.Frame(self.les_petits_hommes_verts_frame, style="White.TFrame")
		grades_frame.pack(fill="both", pady=5)

		I_frame = ttk.Frame(grades_frame, style="White.TFrame")
		I_frame.pack(side="left", pady=2,  padx=(30, 70), expand=True)
		I = ttk.Label(I_frame, text="I", style="GradeName.TLabel")
		I.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		I_input = ttk.Entry(I_frame, textvariable=master.my_variables["I"], width=5, style="EntryGrades.TEntry", justify="center")
		I_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Ip_input = ttk.Entry(I_frame, textvariable=master.my_variables["Ip"], width=5, style="EntryGradesPercentage.TEntry", justify="center")
		Ip_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		J_frame = ttk.Frame(grades_frame, style="White.TFrame")
		J_frame.pack(side="left", pady=2, expand=True)
		J = ttk.Label(J_frame, text="J", style="GradeName.TLabel")
		J.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		J_input = ttk.Entry(J_frame, textvariable=master.my_variables["J"], width=5, style="EntryGrades.TEntry", justify="center")
		J_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		K_frame = ttk.Frame(grades_frame, style="White.TFrame")
		K_frame.pack(side="left", pady=2, expand=True)
		K = ttk.Label(K_frame, text="K", style="GradeName.TLabel")
		K.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		K_input = ttk.Entry(K_frame, textvariable=master.my_variables["K"], width=5, style="EntryGrades.TEntry", justify="center")
		K_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		L_frame = ttk.Frame(grades_frame, style="White.TFrame")
		L_frame.pack(side="left", pady=2,  padx=(0, 70), expand=True)
		L = ttk.Label(L_frame, text="L", style="GradeName.TLabel")
		L.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		L_input = ttk.Entry(L_frame, textvariable=master.my_variables["L"], width=5, style="EntryGrades.TEntry", justify="center")
		L_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Lp_input = ttk.Entry(L_frame, textvariable=master.my_variables["Lp"], width=5, style="EntryGradesPercentage.TEntry", justify="center")
		Lp_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		for i in range(0, self.les_petits_hommes_verts_frame.grid_size()[1]):
			self.les_petits_hommes_verts_frame.rowconfigure(i, weight=1)
		for i in range(0, self.les_petits_hommes_verts_frame.grid_size()[0]):
			self.les_petits_hommes_verts_frame.columnconfigure(i, weight=1)

	def _make_faire_deux_choses_a_la_fois_form(self, master):
		# -- Frame contenant tout le subtest --
		self.faire_deux_choses_a_la_fois_frame = ttk.Frame(self.grades_frame, style="White.TFrame")
		self.faire_deux_choses_a_la_fois_frame.grid(row=2, column=0, columnspan=4, pady=10, padx=2, sticky="NESW")

		# -- Titre du subtest --
		subtest_title_frame = ttk.Frame(self.faire_deux_choses_a_la_fois_frame, style="SubtestLabel.TFrame")
		subtest_title_frame.pack(expand=True, fill='both', ipady=5, padx=70)

		subtesttitle = ttk.Label(subtest_title_frame, text="Faire deux choses à la fois", style="Subtest.TLabel")
		subtesttitle.pack(fill="both", expand=True)

		# -- Notes du subtest --
		grades_frame = ttk.Frame(self.faire_deux_choses_a_la_fois_frame, style="White.TFrame")
		grades_frame.pack(fill="both", pady=5)

		M_frame = ttk.Frame(grades_frame, style="White.TFrame")
		M_frame.pack(side="left", pady=2,  padx=(70, 0), expand=True)
		M = ttk.Label(M_frame, text="M", style="GradeName.TLabel")
		M.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		M_input = ttk.Entry(M_frame, textvariable=master.my_variables["M"], width=5, style="EntryGrades.TEntry", justify="center")
		M_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		N_frame = ttk.Frame(grades_frame, style="White.TFrame")
		N_frame.pack(side="left", pady=2, expand=True)
		N = ttk.Label(N_frame, text="N", style="GradeName.TLabel")
		N.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		N_input = ttk.Entry(N_frame, textvariable=master.my_variables["N"], width=5, style="EntryGrades.TEntry", justify="center")
		N_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		O_frame = ttk.Frame(grades_frame, style="White.TFrame")
		O_frame.pack(side="left", pady=2, expand=True)
		O = ttk.Label(O_frame, text="O", style="GradeName.TLabel")
		O.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		O_input = ttk.Entry(O_frame, textvariable=master.my_variables["O"], width=5, style="EntryGrades.TEntry", justify="center")
		O_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		P_frame = ttk.Frame(grades_frame, style="White.TFrame")
		P_frame.pack(side="left", pady=2, expand=True)
		P = ttk.Label(P_frame, text="P", style="GradeName.TLabel")
		P.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		P_input = ttk.Entry(P_frame, textvariable=master.my_variables["P"], width=5, style="EntryGrades.TEntry", justify="center")
		P_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		Q_frame = ttk.Frame(grades_frame, style="White.TFrame")
		Q_frame.pack(side="left", pady=2, expand=True)
		Q = ttk.Label(Q_frame, text="Q", style="GradeName.TLabel")
		Q.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Q_input = ttk.Entry(Q_frame, textvariable=master.my_variables["Q"], width=5, style="EntryGrades.TEntry", justify="center")
		Q_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		R_frame = ttk.Frame(grades_frame, style="White.TFrame")
		R_frame.pack(side="left", pady=2, expand=True)
		R = ttk.Label(R_frame, text="R", style="GradeName.TLabel")
		R.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		R_input = ttk.Entry(R_frame, textvariable=master.my_variables["R"], width=5, style="EntryGrades.TEntry", justify="center")
		R_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		S_frame = ttk.Frame(grades_frame, style="White.TFrame")
		S_frame.pack(side="left", pady=2, expand=True)
		S = ttk.Label(S_frame, text="S", style="GradeName.TLabel")
		S.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		S_input = ttk.Entry(S_frame, textvariable=master.my_variables["S"], width=5, style="EntryGrades.TEntry", justify="center")
		S_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		T_frame = ttk.Frame(grades_frame, style="White.TFrame")
		T_frame.pack(side="left", pady=2,  padx=(0, 70), expand=True)
		T = ttk.Label(T_frame, text="T", style="GradeName.TLabel")
		T.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		T_input = ttk.Entry(T_frame, textvariable=master.my_variables["T"], width=5, style="EntryGrades.TEntry", justify="center")
		T_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Tp_input = ttk.Entry(T_frame, textvariable=master.my_variables["Tp"], width=5, style="EntryGradesPercentage.TEntry", justify="center")
		Tp_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		for i in range(0, self.faire_deux_choses_a_la_fois_frame.grid_size()[1]):
			self.faire_deux_choses_a_la_fois_frame.rowconfigure(i, weight=1)
		for i in range(0, self.faire_deux_choses_a_la_fois_frame.grid_size()[0]):
			self.faire_deux_choses_a_la_fois_frame.columnconfigure(i, weight=1)

	def _make_carte_geographique_form(self, master):
		# -- Frame contenant tout le subtest --
		self.carte_geographique_frame = ttk.Frame(self.grades_frame, style="White.TFrame")
		self.carte_geographique_frame.grid(row=3, column=0, padx=3, pady=10, sticky="NESW")

		# -- Titre du subtest --
		subtest_title_frame = ttk.Frame(self.carte_geographique_frame, style="SubtestLabel.TFrame")
		subtest_title_frame.pack(expand=True, fill='both', ipady=5, padx=(70, 15))

		subtesttitle = ttk.Label(subtest_title_frame, text="Carte géographique", style="Subtest.TLabel")
		subtesttitle.pack(fill="both", expand=True)

		# -- Notes du subtest --
		grades_frame = ttk.Frame(self.carte_geographique_frame, style="White.TFrame")
		grades_frame.pack(fill="both", pady=5)

		U_frame = ttk.Frame(grades_frame, style="White.TFrame")
		U_frame.pack(side="left", pady=2,  padx=(70, 30), expand=True)
		U = ttk.Label(U_frame, text="U", style="GradeName.TLabel")
		U.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		U_input = ttk.Entry(U_frame, textvariable=master.my_variables["U"], width=5, style="EntryGrades.TEntry", justify="center")
		U_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		U_input = ttk.Entry(U_frame, textvariable=master.my_variables["Up"], width=5, style="EntryGrades.TEntry", justify="center")
		U_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		for i in range(0, self.carte_geographique_frame.grid_size()[1]):
			self.carte_geographique_frame.rowconfigure(i, weight=1)
		for i in range(0, self.carte_geographique_frame.grid_size()[0]):
			self.carte_geographique_frame.columnconfigure(i, weight=1)

	def _make_ecouter_deux_choses_a_la_fois_form(self, master):
		# -- Frame contenant tout le subtest --
		self.ecouter_deux_choses_a_la_fois_frame = ttk.Frame(self.grades_frame, style="White.TFrame")
		self.ecouter_deux_choses_a_la_fois_frame.grid(row=3, column=1, columnspan=2, pady=10, padx=2, sticky="NESW")

		# -- Titre du subtest --
		subtest_title_frame = ttk.Frame(self.ecouter_deux_choses_a_la_fois_frame, style="SubtestLabel.TFrame")
		subtest_title_frame.pack(expand=True, fill='both', ipady=5, padx=15)

		subtesttitle = ttk.Label(subtest_title_frame, text="Écouter deux choses à la fois", style="Subtest.TLabel")
		subtesttitle.pack(fill="both", expand=True)

		# -- Notes du subtest --
		grades_frame = ttk.Frame(self.ecouter_deux_choses_a_la_fois_frame, style="White.TFrame")
		grades_frame.pack(fill="both", pady=5)

		V_frame = ttk.Frame(grades_frame, style="White.TFrame")
		V_frame.pack(side="left", pady=2,  padx=(30, 0), expand=True)
		V = ttk.Label(V_frame, text="V", style="GradeName.TLabel")
		V.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		V_input = ttk.Entry(V_frame, textvariable=master.my_variables["V"], width=5, style="EntryGrades.TEntry", justify="center")
		V_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		W_frame = ttk.Frame(grades_frame, style="White.TFrame")
		W_frame.pack(side="left", pady=2, expand=True)
		W = ttk.Label(W_frame, text="W", style="GradeName.TLabel")
		W.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		W_input = ttk.Entry(W_frame, textvariable=master.my_variables["W"], width=5, style="EntryGrades.TEntry", justify="center")
		W_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		X_frame = ttk.Frame(grades_frame, style="White.TFrame")
		X_frame.pack(side="left", pady=2,  padx=(0, 30), expand=True)
		X = ttk.Label(X_frame, text="X", style="GradeName.TLabel")
		X.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		X_input = ttk.Entry(X_frame, textvariable=master.my_variables["X"], width=5, style="EntryGrades.TEntry", justify="center")
		X_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Xp_input = ttk.Entry(X_frame, textvariable=master.my_variables["Xp"], width=5, style="EntryGradesPercentage.TEntry", justify="center")
		Xp_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		for i in range(0, self.ecouter_deux_choses_a_la_fois_frame.grid_size()[1]):
			self.ecouter_deux_choses_a_la_fois_frame.rowconfigure(i, weight=1)
		for i in range(0, self.ecouter_deux_choses_a_la_fois_frame.grid_size()[0]):
			self.ecouter_deux_choses_a_la_fois_frame.columnconfigure(i, weight=1)

	def _make_marche_arrete_form(self, master):
		# -- Frame contenant tout le subtest --
		self.marche_arrete_frame = ttk.Frame(self.grades_frame, style="White.TFrame")
		self.marche_arrete_frame.grid(row=3, column=3, padx=2, pady=10, sticky="NESW")

		# -- Titre du subtest --
		subtest_title_frame = ttk.Frame(self.marche_arrete_frame, style="SubtestLabel.TFrame")
		subtest_title_frame.pack(expand=True, fill='both', ipady=5, padx=(15, 70))

		subtesttitle = ttk.Label(subtest_title_frame, text="Marche - Arrête", style="Subtest.TLabel")
		subtesttitle.pack(fill="both", expand=True)

		# -- Notes du subtest --
		grades_frame = ttk.Frame(self.marche_arrete_frame, style="White.TFrame")
		grades_frame.pack(fill="both", pady=5)

		Y_frame = ttk.Frame(grades_frame, style="White.TFrame")
		Y_frame.pack(side="left", pady=2,  padx=(30, 70), expand=True)
		Y = ttk.Label(Y_frame, text="Y", style="GradeName.TLabel")
		Y.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Y_input = ttk.Entry(Y_frame, textvariable=master.my_variables["Y"], width=5, style="EntryGrades.TEntry", justify="center")
		Y_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Yp_input = ttk.Entry(Y_frame, textvariable=master.my_variables["Yp"], width=5, style="EntryGradesPercentage.TEntry", justify="center")
		Yp_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		for i in range(0, self.marche_arrete_frame.grid_size()[1]):
			self.marche_arrete_frame.rowconfigure(i, weight=1)
		for i in range(0, self.marche_arrete_frame.grid_size()[0]):
			self.marche_arrete_frame.columnconfigure(i, weight=1)

	def _make_mondes_contraires_form(self, master):
		# -- Frame contenant tout le subtest --
		self.mondes_contraires_frame = ttk.Frame(self.grades_frame, style="White.TFrame")
		self.mondes_contraires_frame.grid(row=4, column=0, columnspan=3, padx=3, pady=10, sticky="NESW")

		# -- Titre du subtest --
		subtest_title_frame = ttk.Frame(self.mondes_contraires_frame, style="SubtestLabel.TFrame")
		subtest_title_frame.pack(expand=True, fill='both', ipady=5, padx=(70, 15))

		subtesttitle = ttk.Label(subtest_title_frame, text="Mondes contraires", style="Subtest.TLabel")
		subtesttitle.pack(fill="both", expand=True)

		# -- Notes du subtest --
		grades_frame = ttk.Frame(self.mondes_contraires_frame, style="White.TFrame")
		grades_frame.pack(fill="both", pady=5)

		one_frame = ttk.Frame(grades_frame, style="White.TFrame")
		one_frame.pack(side="left", pady=2,  padx=(70, 0), expand=True)
		one = ttk.Label(one_frame, text="1", style="GradeName.TLabel")
		one.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		one_input = ttk.Entry(one_frame, textvariable=master.my_variables["one"], width=5, style="EntryGrades.TEntry", justify="center")
		one_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		four_frame = ttk.Frame(grades_frame, style="White.TFrame")
		four_frame.pack(side="left", pady=2, expand=True)
		four = ttk.Label(four_frame, text="4", style="GradeName.TLabel")
		four.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		four_input = ttk.Entry(four_frame, textvariable=master.my_variables["four"], width=5, style="EntryGrades.TEntry", justify="center")
		four_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		Z_frame = ttk.Frame(grades_frame, style="White.TFrame")
		Z_frame.pack(side="left", pady=2, expand=True)
		Z = ttk.Label(Z_frame, text="Z", style="GradeName.TLabel")
		Z.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Z_input = ttk.Entry(Z_frame, textvariable=master.my_variables["Z"], width=5, style="EntryGrades.TEntry", justify="center")
		Z_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		Zp_input = ttk.Entry(Z_frame, textvariable=master.my_variables["Zp"], width=5, style="EntryGradesPercentage.TEntry", justify="center")
		Zp_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		two_frame = ttk.Frame(grades_frame, style="White.TFrame")
		two_frame.pack(side="left", pady=2, expand=True)
		two = ttk.Label(two_frame, text="2", style="GradeName.TLabel")
		two.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		two_input = ttk.Entry(two_frame, textvariable=master.my_variables["two"], width=5, style="EntryGrades.TEntry", justify="center")
		two_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		three_frame = ttk.Frame(grades_frame, style="White.TFrame")
		three_frame.pack(side="left", pady=2, expand=True)
		three = ttk.Label(three_frame, text="3", style="GradeName.TLabel")
		three.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		three_input = ttk.Entry(three_frame, textvariable=master.my_variables["three"], width=5, style="EntryGrades.TEntry", justify="center")
		three_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		AA_frame = ttk.Frame(grades_frame, style="White.TFrame")
		AA_frame.pack(side="left", pady=2,  padx=(0, 30), expand=True)
		AA = ttk.Label(AA_frame, text="AA", style="GradeName.TLabel")
		AA.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		AA_input = ttk.Entry(AA_frame, textvariable=master.my_variables["AA"], width=5, style="EntryGrades.TEntry", justify="center")
		AA_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		AAp_input = ttk.Entry(AA_frame, textvariable=master.my_variables["AAp"], width=5, style="EntryGradesPercentage.TEntry", justify="center")
		AAp_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		for i in range(0, self.mondes_contraires_frame.grid_size()[1]):
			self.mondes_contraires_frame.rowconfigure(i, weight=1)
		for i in range(0, self.mondes_contraires_frame.grid_size()[0]):
			self.mondes_contraires_frame.columnconfigure(i, weight=1)

	def _make_transmission_de_codes_form(self, master):
		# -- Frame contenant tout le subtest --
		self.transmission_de_codes_frame = ttk.Frame(self.grades_frame, style="White.TFrame")
		self.transmission_de_codes_frame.grid(row=4, column=3, pady=10, padx=2, sticky="NESW")

		# -- Titre du subtest --
		subtest_title_frame = ttk.Frame(self.transmission_de_codes_frame, style="SubtestLabel.TFrame")
		subtest_title_frame.pack(expand=True, fill='both', ipady=5, padx=(15, 70))

		subtesttitle = ttk.Label(subtest_title_frame, text="Transmission de codes", style="Subtest.TLabel")
		subtesttitle.pack(fill="both", expand=True)

		# -- Notes du subtest --
		grades_frame = ttk.Frame(self.transmission_de_codes_frame, style="White.TFrame")
		grades_frame.pack(fill="both", pady=5)

		BB_frame = ttk.Frame(grades_frame, style="White.TFrame")
		BB_frame.pack(side="left", pady=2,  padx=(30, 70), expand=True)
		BB = ttk.Label(BB_frame, text="BB", style="GradeName.TLabel")
		BB.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		BB_input = ttk.Entry(BB_frame, textvariable=master.my_variables["BB"], width=5, style="EntryGrades.TEntry", justify="center")
		BB_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)
		BBp_input = ttk.Entry(BB_frame, textvariable=master.my_variables["BBp"], width=5, style="EntryGradesPercentage.TEntry", justify="center")
		BBp_input.pack(side="left", fill="both", ipady=2, ipadx=2, pady=2, padx=2)

		for i in range(0, self.transmission_de_codes_frame.grid_size()[1]):
			self.transmission_de_codes_frame.rowconfigure(i, weight=1)
		for i in range(0, self.transmission_de_codes_frame.grid_size()[0]):
			self.transmission_de_codes_frame.columnconfigure(i, weight=1)
