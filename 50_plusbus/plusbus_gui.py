import tkinter as tk
from tkinter import ttk
import plusbus_data as pbd
import plusbus_database as pbdb


class Plusbus:
	def __init__(self):
		self.gui_background_color = "#2E2E2E"
		self.secondary_bg_color = "#4F4F4F"
		self.test_color = "#0045FF"
		self.button_press_color = "#696969"
		self.text_color = "#FFFFFF"
		self.error_color = "#FF0000"
		self.successful_color = "#00ff26"
		self.tree_view_selected = "#262626"
		self.evenrow_background = "#4A4A4A"
		self.oddrow_background = "#757575"
		self.row_height = 20
		self.kundeid = -1
		self.auth = 0
		self.selected = [-1, "", 0]

		self.gui = tk.Tk()
		self.gui.title("Plus bus app")
		self.gui.geometry("1200x700")
		self.gui.configure(bg=self.gui_background_color)

		#  Account login / Create account

		self.acc_frame = tk.Frame(self.gui, bg=self.gui_background_color)
		self.acc_frame.place(relx=0.5, rely=0.5, anchor="center")

		self.current_window = self.acc_frame

		self.acc_header_frame = tk.Frame(self.acc_frame)
		self.acc_header_frame.pack()

		self.acc_header_label = tk.Label(self.acc_header_frame, text="Login på din account", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 50))
		self.acc_header_label.grid(row=0, column=0)

		self.acc_acc_frame = tk.Frame(self.acc_frame, bg=self.gui_background_color)
		self.acc_acc_frame.pack()

		self.tree_view_style = ttk.Style()
		self.tree_view_style.theme_use("default")
		self.tree_view_style.configure("Treeview", bg=self.gui_background_color, fg=self.text_color, rowheight=self.row_height, fieldbackground=self.secondary_bg_color)
		self.tree_view_style.map("Treeview", background=[("selected", self.tree_view_selected)])

		self.acc_scrollbar = tk.Scrollbar(self.acc_acc_frame)
		self.acc_scrollbar.grid(row=0, column=1, pady=(30, 0), sticky="ns")
		self.acc_treeview = ttk.Treeview(self.acc_acc_frame, yscrollcommand=self.acc_scrollbar.set, selectmode="browse")
		self.acc_treeview.grid(row=0, column=0, pady=(30, 0))
		self.acc_scrollbar.config(command=self.acc_treeview.yview)

		self.acc_treeview['columns'] = ("id", "efternavn", "kontakt", "auth")
		self.acc_treeview.column("#0", width=0, stretch=tk.NO)
		self.acc_treeview.column("id", width=50, anchor="w")
		self.acc_treeview.column("efternavn", width=125, anchor="w")
		self.acc_treeview.column("kontakt", width=125, anchor="w")
		self.acc_treeview.column("auth", width=35, anchor="w")

		self.acc_treeview.heading("#0", text="", anchor="w")
		self.acc_treeview.heading("id", text="Id", anchor="center")
		self.acc_treeview.heading("efternavn", text="Efternavn", anchor="center")
		self.acc_treeview.heading("kontakt", text="Kontakt", anchor="center")
		self.acc_treeview.heading("auth", text="Auth", anchor="center")

		self.acc_treeview.tag_configure("evenrow", background=self.evenrow_background, foreground=self.text_color)
		self.acc_treeview.tag_configure("oddrow", background=self.oddrow_background, foreground=self.text_color)

		self.acc_treeview.bind("<ButtonRelease-1>", lambda event: self.select_id(self.acc_treeview, "kundeid"))

		fill_treeview(self.acc_treeview, pbdb.select_all(pbd.Kunde))

		self.acc_button_frame = tk.Frame(self.acc_frame, bg=self.gui_background_color)
		self.acc_button_frame.pack()

		self.acc_button_login = tk.Button(self.acc_button_frame, text="Login", relief="flat", bg=self.secondary_bg_color,
										  fg=self.text_color, activebackground=self.button_press_color, font=("Arial", 15), command=self.login)
		self.acc_button_login.grid(row=0, column=0, pady=(50, 0))

		self.acc_button_label = tk.Label(self.acc_button_frame, text="Har du ikke en account?", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 15))
		self.acc_button_label.grid(row=1, column=0, pady=(30, 0))
		self.acc_button_create_button = tk.Button(self.acc_button_frame, text="Opret account", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
												  activebackground=self.button_press_color, font=("Arial", 15), command=lambda: self.change_window(self.acc_create_frame))
		self.acc_button_create_button.grid(row=2, column=0, pady=(5, 80))

		#  Create account

		self.acc_create_frame = tk.Frame(self.gui, bg=self.gui_background_color)
		# self.acc_create_frame.place(relx=0.5, rely=0.5, anchor="center")

		self.acc_create_label = tk.Label(self.acc_create_frame, text="Opret din account", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 40))
		self.acc_create_label.grid(row=0, column=0)

		self.acc_create_label_frame = tk.Frame(self.acc_create_frame, bg=self.gui_background_color)
		self.acc_create_label_frame.grid(row=1, column=0)

		self.acc_create_label_frame_label_efternavn = tk.Label(self.acc_create_label_frame, text="Efternavn", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 20))
		self.acc_create_label_frame_label_efternavn.grid(row=0, column=0, padx=(0, 30))

		self.acc_create_label_frame_label_kontaktinfo = tk.Label(self.acc_create_label_frame, text="Kontaktinfo", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 20))
		self.acc_create_label_frame_label_kontaktinfo.grid(row=0, column=1)

		self.acc_create_label_frame_entry_efternavn = tk.Entry(self.acc_create_label_frame, font=("Arial", 20), width=10)
		self.acc_create_label_frame_entry_efternavn.grid(row=1, column=0, padx=(0, 30))

		self.acc_create_label_frame_entry_kontaktinfo = tk.Entry(self.acc_create_label_frame, font=("Arial", 20), width=10)
		self.acc_create_label_frame_entry_kontaktinfo.grid(row=1, column=1)

		self.acc_create_back_button = tk.Button(self.acc_create_label_frame, text="Annuller", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
												activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.change_window(self.acc_frame))
		self.acc_create_back_button.grid(row=2, column=0, pady=(30, 0), padx=(0, 30))

		self.acc_create_create_account_button = tk.Button(self.acc_create_label_frame, text="Opret account", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
														  activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.create_account())
		self.acc_create_create_account_button.grid(row=2, column=1, pady=(30, 0))
		self.acc_create_label_frame_label_missing_info = tk.Label(self.acc_create_frame, text="", bg=self.gui_background_color, fg=self.error_color, font=("Arial", 50))
		self.acc_create_label_frame_label_missing_info.grid(row=2, column=0, pady=(30, 0))

		# Admin menu

		self.admin_frame = tk.Frame(self.gui, bg=self.gui_background_color)

		self.admin_frame_label = tk.Label(self.admin_frame, text="Admin panel", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 40))
		self.admin_frame_label.grid(row=0, column=0)

		self.admin_rejse_frame = tk.Frame(self.admin_frame, bg=self.gui_background_color)
		self.admin_rejse_frame.grid(row=1, column=0)

		self.admin_scrollbar = tk.Scrollbar(self.admin_rejse_frame)
		self.admin_scrollbar.grid(row=0, column=1, pady=(30, 0), sticky="ns")
		self.admin_treeview = ttk.Treeview(self.admin_rejse_frame, yscrollcommand=self.admin_scrollbar.set, selectmode="browse")
		self.admin_treeview.grid(row=0, column=0, pady=(30, 0))
		self.admin_scrollbar.config(command=self.admin_treeview.yview)

		self.admin_treeview['columns'] = ("id", "rute", "dato", "pladskapacitet")
		self.admin_treeview.column("#0", width=0, stretch=tk.NO)
		self.admin_treeview.column("id", width=50, anchor="w")
		self.admin_treeview.column("rute", width=125, anchor="w")
		self.admin_treeview.column("dato", width=125, anchor="w")
		self.admin_treeview.column("pladskapacitet", width=150, anchor="w")

		self.admin_treeview.heading("#0", text="", anchor="w")
		self.admin_treeview.heading("id", text="Id", anchor="center")
		self.admin_treeview.heading("rute", text="Rute", anchor="center")
		self.admin_treeview.heading("dato", text="Dato", anchor="center")
		self.admin_treeview.heading("pladskapacitet", text="Pladskapacitet", anchor="center")

		self.admin_treeview.tag_configure("evenrow", background=self.evenrow_background, foreground=self.text_color)
		self.admin_treeview.tag_configure("oddrow", background=self.oddrow_background, foreground=self.text_color)

		self.admin_treeview.bind("<ButtonRelease-1>", lambda event: self.select_id(self.admin_treeview, "rejseid"))

		fill_treeview(self.admin_treeview, pbdb.select_all(pbd.Rejse))

		self.admin_entry_frame = tk.Frame(self.admin_frame, bg=self.gui_background_color)
		self.admin_entry_frame.grid(row=2, column=0)

		self.admin_entry_frame_rute_label = tk.Label(self.admin_entry_frame, text="Rute", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 20))
		self.admin_entry_frame_rute_label.grid(row=0, column=0, padx=(0, 30))

		self.admin_entry_frame_dato_label = tk.Label(self.admin_entry_frame, text="Dato", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 20))
		self.admin_entry_frame_dato_label.grid(row=0, column=1, padx=(0, 30))

		self.admin_entry_frame_pladskapacitet_label = tk.Label(self.admin_entry_frame, text="Pladskapacitet", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 20))
		self.admin_entry_frame_pladskapacitet_label.grid(row=0, column=2)

		self.admin_entry_frame_rute_entry = tk.Entry(self.admin_entry_frame, font=("Arial", 20), width=10)
		self.admin_entry_frame_rute_entry.grid(row=1, column=0, padx=(0, 30))

		self.admin_entry_frame_dato_entry = tk.Entry(self.admin_entry_frame, font=("Arial", 20), width=10)
		self.admin_entry_frame_dato_entry.grid(row=1, column=1, padx=(0, 30))

		self.admin_entry_frame_pladskapacitet_entry = tk.Entry(self.admin_entry_frame, font=("Arial", 20), width=10)
		self.admin_entry_frame_pladskapacitet_entry.grid(row=1, column=2)

		self.admin_button_frame = tk.Frame(self.admin_frame, bg=self.gui_background_color)
		self.admin_button_frame.grid(row=3, column=0, pady=(30, 0))

		self.admin_back_button = tk.Button(self.admin_button_frame, text="Tilbage", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
										   activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.change_window(self.acc_frame))
		self.admin_back_button.grid(row=0, column=0, padx=(0, 30))

		self.admin_slet_rejse_button = tk.Button(self.admin_button_frame, text="Slet rejse", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
												 activebackground=self.button_press_color, font=("Arial", 20), command=self.delete_rejse)
		self.admin_slet_rejse_button.grid(row=0, column=1, padx=(0, 30))

		self.admin_opret_rejse_button = tk.Button(self.admin_button_frame, text="Opret rejse", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
												  activebackground=self.button_press_color, font=("Arial", 20), command=self.opret_rejse)
		self.admin_opret_rejse_button.grid(row=0, column=2, padx=(0, 30))

		self.admin_rediger_rejse_button = tk.Button(self.admin_button_frame, text="Rediger rejse", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
													activebackground=self.button_press_color, font=("Arial", 20), command=self.rediger_rejse)
		self.admin_rediger_rejse_button.grid(row=0, column=3)

		self.acc_create_label_frame_label_error = tk.Label(self.admin_frame, text="", bg=self.gui_background_color, fg=self.error_color, font=("Arial", 30))
		self.acc_create_label_frame_label_error.grid(row=4, column=0, pady=(30, 0))

		# Rediger rejse menu

		self.rediger_rejse_frame = tk.Frame(self.gui, bg=self.gui_background_color)

		self.rediger_rejse_label_1 = tk.Label(self.rediger_rejse_frame, text="", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.rediger_rejse_label_1.grid(row=0, column=0)

		self.rediger_rejse_frame_frame = tk.Frame(self.rediger_rejse_frame, bg=self.gui_background_color)
		self.rediger_rejse_frame_frame.grid(row=1, column=0, pady=(30, 0))

		self.rediger_rejse_label_2 = tk.Label(self.rediger_rejse_frame_frame, text="Rute", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.rediger_rejse_label_2.grid(row=0, column=0, padx=(0, 30))
		self.rediger_rejse_label_3 = tk.Label(self.rediger_rejse_frame_frame, text="Dato", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.rediger_rejse_label_3.grid(row=0, column=1, padx=(0, 30))
		self.rediger_rejse_label_4 = tk.Label(self.rediger_rejse_frame_frame, text="Pladskapacitet", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.rediger_rejse_label_4.grid(row=0, column=2)
		self.rediger_rejse_entry_1 = tk.Entry(self.rediger_rejse_frame_frame, font=("Arial", 30), width=10)
		self.rediger_rejse_entry_1.grid(row=1, column=0, padx=(0, 30))
		self.rediger_rejse_entry_2 = tk.Entry(self.rediger_rejse_frame_frame, font=("Arial", 30), width=10)
		self.rediger_rejse_entry_2.grid(row=1, column=1, padx=(0, 30))
		self.rediger_rejse_entry_3 = tk.Entry(self.rediger_rejse_frame_frame, font=("Arial", 30), width=10)
		self.rediger_rejse_entry_3.grid(row=1, column=2)

		self.rediger_rejse_button_frame = tk.Frame(self.rediger_rejse_frame, bg=self.gui_background_color)
		self.rediger_rejse_button_frame.grid(row=2, column=0)

		self.rediger_rejse_back_button = tk.Button(self.rediger_rejse_button_frame, text="Annuller", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
												   activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.change_window(self.admin_frame))
		self.rediger_rejse_back_button.grid(row=0, column=0, pady=(30, 0), padx=(0, 30))

		self.rediger_rejse_save_button = tk.Button(self.rediger_rejse_button_frame, text="Save", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
												   activebackground=self.button_press_color, font=("Arial", 20), command=self.save_rejse)
		self.rediger_rejse_save_button.grid(row=0, column=1, pady=(30, 0))

		self.rediger_rejse_label_missing_info = tk.Label(self.rediger_rejse_frame, text="", bg=self.gui_background_color, fg=self.error_color, font=("Arial", 50))
		self.rediger_rejse_label_missing_info.grid(row=3, column=0, pady=(30, 0))

		# Kunde menu

		self.kunde_frame = tk.Frame(self.gui, bg=self.gui_background_color)
		self.kunde_frame_treeview_frame = tk.Frame(self.kunde_frame, bg=self.gui_background_color)
		self.kunde_frame_treeview_frame.grid(row=0, column=0)

		# Rejser man kan booke treeview

		self.kunde_frame_treeview_rejse_frame = tk.Frame(self.kunde_frame_treeview_frame, bg=self.gui_background_color)
		self.kunde_frame_treeview_rejse_frame.grid(row=0, column=0)

		self.kunde_frame_treeview_rejse_label = tk.Label(self.kunde_frame_treeview_rejse_frame, text="Rejser du kan booke", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.kunde_frame_treeview_rejse_label.grid(row=0, column=0)

		self.kunde_frame_treeview_rejse_scrollbar = tk.Scrollbar(self.kunde_frame_treeview_rejse_frame)
		self.kunde_frame_treeview_rejse_scrollbar.grid(row=1, column=1, pady=(30, 0), sticky="ns")
		self.kunde_frame_treeview_rejse_treeview = ttk.Treeview(self.kunde_frame_treeview_rejse_frame, yscrollcommand=self.kunde_frame_treeview_rejse_scrollbar.set, selectmode="browse")
		self.kunde_frame_treeview_rejse_treeview.grid(row=1, column=0, pady=(30, 0))
		self.kunde_frame_treeview_rejse_scrollbar.config(command=self.kunde_frame_treeview_rejse_treeview.yview)

		self.kunde_frame_treeview_rejse_treeview['columns'] = ("id", "rute", "dato", "pladskapacitet")
		self.kunde_frame_treeview_rejse_treeview.column("#0", width=0, stretch=tk.NO)
		self.kunde_frame_treeview_rejse_treeview.column("id", width=50, anchor="w")
		self.kunde_frame_treeview_rejse_treeview.column("rute", width=125, anchor="w")
		self.kunde_frame_treeview_rejse_treeview.column("dato", width=125, anchor="w")
		self.kunde_frame_treeview_rejse_treeview.column("pladskapacitet", width=150, anchor="w")

		self.kunde_frame_treeview_rejse_treeview.heading("#0", text="", anchor="w")
		self.kunde_frame_treeview_rejse_treeview.heading("id", text="Id", anchor="center")
		self.kunde_frame_treeview_rejse_treeview.heading("rute", text="Rute", anchor="center")
		self.kunde_frame_treeview_rejse_treeview.heading("dato", text="Dato", anchor="center")
		self.kunde_frame_treeview_rejse_treeview.heading("pladskapacitet", text="Pladskapacitet", anchor="center")

		self.kunde_frame_treeview_rejse_treeview.tag_configure("evenrow", background=self.evenrow_background, foreground=self.text_color)
		self.kunde_frame_treeview_rejse_treeview.tag_configure("oddrow", background=self.oddrow_background, foreground=self.text_color)

		self.kunde_frame_treeview_rejse_treeview.bind("<ButtonRelease-1>", lambda event: self.select_id(self.kunde_frame_treeview_rejse_treeview, "bookrejse"))

		# Bookinger treeview

		self.kunde_frame_treeview_bookinger_frame = tk.Frame(self.kunde_frame_treeview_frame, bg=self.gui_background_color)
		self.kunde_frame_treeview_bookinger_frame.grid(row=0, column=1, padx=(50, 0))

		self.kunde_frame_treeview_bookinger_label = tk.Label(self.kunde_frame_treeview_bookinger_frame, text="Dine bookinger", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.kunde_frame_treeview_bookinger_label.grid(row=0, column=1)

		self.kunde_frame_treeview_bookinger_scrollbar = tk.Scrollbar(self.kunde_frame_treeview_bookinger_frame)
		self.kunde_frame_treeview_bookinger_scrollbar.grid(row=1, column=2, pady=(30, 0), sticky="ns")
		self.kunde_frame_treeview_bookinger_treeview = ttk.Treeview(self.kunde_frame_treeview_bookinger_frame, yscrollcommand=self.kunde_frame_treeview_bookinger_scrollbar.set, selectmode="browse")
		self.kunde_frame_treeview_bookinger_treeview.grid(row=1, column=1, pady=(30, 0))
		self.kunde_frame_treeview_bookinger_scrollbar.config(command=self.kunde_frame_treeview_bookinger_treeview.yview)

		self.kunde_frame_treeview_bookinger_treeview['columns'] = ("id", "rute", "dato", "pladser")
		self.kunde_frame_treeview_bookinger_treeview.column("#0", width=0, stretch=tk.NO)
		self.kunde_frame_treeview_bookinger_treeview.column("id", width=50, anchor="w")
		self.kunde_frame_treeview_bookinger_treeview.column("rute", width=125, anchor="w")
		self.kunde_frame_treeview_bookinger_treeview.column("dato", width=125, anchor="w")
		self.kunde_frame_treeview_bookinger_treeview.column("pladser", width=150, anchor="w")

		self.kunde_frame_treeview_bookinger_treeview.heading("#0", text="", anchor="w")
		self.kunde_frame_treeview_bookinger_treeview.heading("id", text="Id", anchor="center")
		self.kunde_frame_treeview_bookinger_treeview.heading("rute", text="Rute", anchor="center")
		self.kunde_frame_treeview_bookinger_treeview.heading("dato", text="Dato", anchor="center")
		self.kunde_frame_treeview_bookinger_treeview.heading("pladser", text="Pladser booket", anchor="center")

		self.kunde_frame_treeview_bookinger_treeview.tag_configure("evenrow", background=self.evenrow_background, foreground=self.text_color)
		self.kunde_frame_treeview_bookinger_treeview.tag_configure("oddrow", background=self.oddrow_background, foreground=self.text_color)

		self.kunde_frame_treeview_bookinger_treeview.bind("<ButtonRelease-1>", lambda event: self.select_id(self.kunde_frame_treeview_bookinger_treeview, "bookingid"))

		# Kunde buttons

		self.kunde_frame_buttons = tk.Frame(self.kunde_frame, bg=self.gui_background_color)
		self.kunde_frame_buttons.grid(row=1, column=0, pady=(30, 0))

		self.kunde_frame_back_button = tk.Button(self.kunde_frame_buttons, text="Tilbage", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
												 activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.change_window(self.acc_frame))
		self.kunde_frame_back_button.grid(row=1, column=0, padx=(0, 30))

		self.kunde_frame_book_rejse_button = tk.Button(self.kunde_frame_buttons, text="Book rejse", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
													   activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.book_rejse())
		self.kunde_frame_book_rejse_button.grid(row=1, column=1, padx=(0, 30))

		self.kunde_frame_slet_rejse_button = tk.Button(self.kunde_frame_buttons, text="Slet rejse", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
													   activebackground=self.button_press_color, font=("Arial", 20), command=self.unbook_rejse)
		self.kunde_frame_slet_rejse_button.grid(row=1, column=2, padx=(0, 30))

		self.kunde_frame_rediger_rejse_button = tk.Button(self.kunde_frame_buttons, text="Rediger rejse", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
															activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.kunde_rediger_rejse())
		self.kunde_frame_rediger_rejse_button.grid(row=1, column=3, padx=(0, 30))

		self.kunde_frame_rediger_account_button = tk.Button(self.kunde_frame_buttons, text="Rediger account", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
															activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.change_window(self.rediger_account_frame))
		self.kunde_frame_rediger_account_button.grid(row=1, column=4)

		# Vælg pladser skærm

		self.kunde_book_rejse_frame = tk.Frame(self.gui, bg=self.gui_background_color)

		self.kunde_book_rejse_label_1 = tk.Label(self.kunde_book_rejse_frame, text="", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.kunde_book_rejse_label_1.grid(row=0, column=0)
		self.kunde_book_rejse_label_2 = tk.Label(self.kunde_book_rejse_frame, text="", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.kunde_book_rejse_label_2.grid(row=1, column=0, pady=(10, 0))
		self.kunde_book_rejse_label_3 = tk.Label(self.kunde_book_rejse_frame, text="", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.kunde_book_rejse_label_3.grid(row=2, column=0)
		self.kunde_book_rejse_label_4 = tk.Label(self.kunde_book_rejse_frame, text="", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.kunde_book_rejse_label_4.grid(row=3, column=0)
		self.kunde_book_rejse_label_pladser = tk.Label(self.kunde_book_rejse_frame, text="Hvor mange pladser vil du booke", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 30))
		self.kunde_book_rejse_label_pladser.grid(row=4, column=0, pady=(30, 0))
		self.kunde_book_rejse_entry_pladser = tk.Entry(self.kunde_book_rejse_frame, font=("Arial", 30), width=10)
		self.kunde_book_rejse_entry_pladser.grid(row=5, column=0)

		self.kunde_book_rejse_button_frame = tk.Frame(self.kunde_book_rejse_frame, bg=self.gui_background_color)
		self.kunde_book_rejse_button_frame.grid(row=6, column=0, pady=(30, 0))

		self.kunde_book_rejse_button_frame_back_button = tk.Button(self.kunde_book_rejse_button_frame, text="Annuller", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
																   activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.change_window(self.kunde_frame))
		self.kunde_book_rejse_button_frame_back_button.grid(row=0, column=0, padx=(0, 30))

		self.kunde_book_rejse_button_frame_book_rejse_button = tk.Button(self.kunde_book_rejse_button_frame, text="Book rejse", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
																		 activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.book_rejse(self.kunde_book_rejse_entry_pladser.get()))
		self.kunde_book_rejse_button_frame_book_rejse_button.grid(row=0, column=1)

		self.kunde_book_rejse_button_frame_label_missing_info = tk.Label(self.kunde_book_rejse_frame, text="", bg=self.gui_background_color, fg=self.error_color, font=("Arial", 50))
		self.kunde_book_rejse_button_frame_label_missing_info.grid(row=7, column=0, pady=(30, 0))

		# Rediger account

		self.rediger_account_frame = tk.Frame(self.gui, bg=self.gui_background_color)

		self.rediger_account_frame_frame = tk.Frame(self.rediger_account_frame, bg=self.gui_background_color)
		self.rediger_account_frame_frame.grid(row=0, column=0)

		self.rediger_account_label_1 = tk.Label(self.rediger_account_frame_frame, text="Efternavn", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 20))
		self.rediger_account_label_1.grid(row=0, column=0, padx=(0, 30))

		self.rediger_account_label_2 = tk.Label(self.rediger_account_frame_frame, text="Kontaktinfo", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 20))
		self.rediger_account_label_2.grid(row=0, column=1)

		self.rediger_account_entry_1 = tk.Entry(self.rediger_account_frame_frame, font=("Arial", 20), width=10)
		self.rediger_account_entry_1.grid(row=1, column=0, padx=(0, 30))

		self.rediger_account_entry_2 = tk.Entry(self.rediger_account_frame_frame, font=("Arial", 20), width=10)
		self.rediger_account_entry_2.grid(row=1, column=1)

		self.rediger_account_button_frame = tk.Frame(self.rediger_account_frame, bg=self.gui_background_color)
		self.rediger_account_button_frame.grid(row=1, column=0, pady=(30, 0))

		self.rediger_account_back_button = tk.Button(self.rediger_account_button_frame, text="Tilbage", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
												activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.change_window(self.kunde_frame))
		self.rediger_account_back_button.grid(row=0, column=0, padx=(0, 30))

		self.rediger_account_save_button = tk.Button(self.rediger_account_button_frame, text="Save", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
														  activebackground=self.button_press_color, font=("Arial", 20), command=self.save_account)
		self.rediger_account_save_button.grid(row=0, column=1, padx=(0, 30))

		self.rediger_account_delete_account_button = tk.Button(self.rediger_account_button_frame, text="Slet account", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
													 activebackground=self.button_press_color, font=("Arial", 20), command=self.delete_account)
		self.rediger_account_delete_account_button.grid(row=0, column=2)

		self.rediger_account_label_missing_info = tk.Label(self.rediger_account_frame, text="", bg=self.gui_background_color, fg=self.error_color, font=("Arial", 50))
		self.rediger_account_label_missing_info.grid(row=2, column=0, pady=(30, 0))

		# Rediger kunde booking

		self.rediger_kunde_rejse = tk.Frame(self.gui, bg=self.gui_background_color)

		self.rediger_kunde_rejse_label_1 = tk.Label(self.rediger_kunde_rejse, text="", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.rediger_kunde_rejse_label_1.grid(row=0, column=0)
		self.rediger_kunde_rejse_label_2 = tk.Label(self.rediger_kunde_rejse, text="", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.rediger_kunde_rejse_label_2.grid(row=1, column=0, pady=(10, 0))
		self.rediger_kunde_rejse_label_3 = tk.Label(self.rediger_kunde_rejse, text="", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.rediger_kunde_rejse_label_3.grid(row=2, column=0)
		self.rediger_kunde_rejse_label_4 = tk.Label(self.rediger_kunde_rejse, text="", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 25))
		self.rediger_kunde_rejse_label_4.grid(row=3, column=0)
		self.rediger_kunde_rejse_label_pladser = tk.Label(self.rediger_kunde_rejse, text="Hvor mange pladser vil du booke", bg=self.gui_background_color, fg=self.text_color, font=("Arial", 30))
		self.rediger_kunde_rejse_label_pladser.grid(row=4, column=0, pady=(30, 0))
		self.rediger_kunde_rejse_entry_pladser = tk.Entry(self.rediger_kunde_rejse, font=("Arial", 30), width=10)
		self.rediger_kunde_rejse_entry_pladser.grid(row=5, column=0)

		self.rediger_kunde_rejse_button_frame = tk.Frame(self.rediger_kunde_rejse, bg=self.gui_background_color)
		self.rediger_kunde_rejse_button_frame.grid(row=6, column=0, pady=(30, 0))

		self.rediger_kunde_rejse_button_frame_back_button = tk.Button(self.rediger_kunde_rejse_button_frame, text="Annuller", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
																   activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.change_window(self.kunde_frame))
		self.rediger_kunde_rejse_button_frame_back_button.grid(row=0, column=0, padx=(0, 30))

		self.rediger_kunde_rejse_button_frame_book_rejse_button = tk.Button(self.rediger_kunde_rejse_button_frame, text="Save", relief="flat", bg=self.secondary_bg_color, fg=self.text_color,
																		 activebackground=self.button_press_color, font=("Arial", 20), command=lambda: self.kunde_rediger_rejse(self.rediger_kunde_rejse_entry_pladser.get()))
		self.rediger_kunde_rejse_button_frame_book_rejse_button.grid(row=0, column=1)

		self.rediger_kunde_rejse_button_frame_label_missing_info = tk.Label(self.rediger_kunde_rejse, text="", bg=self.gui_background_color, fg=self.error_color, font=("Arial", 50))
		self.rediger_kunde_rejse_button_frame_label_missing_info.grid(row=7, column=0, pady=(30, 0))

	def kunde_rediger_rejse(self, pladser=None):
		if not self.selected[1] == "bookingid" or self.selected[0] == -1:
			return
		booking = pbdb.get_record(pbd.Booking, self.selected[0])
		rejse = pbdb.get_record(pbd.Rejse, booking.rejseid)
		remaining = get_remaining_slots(booking.rejseid) + booking.pladser
		if pladser is None:
			self.rediger_kunde_rejse_label_1.configure(text="Rejse id: " + str(rejse.id))
			self.rediger_kunde_rejse_label_2.configure(text="Rute: " + rejse.rute)
			self.rediger_kunde_rejse_label_3.configure(text="Dato: " + rejse.dato)
			self.rediger_kunde_rejse_label_4.configure(text="Pladser: " + str(remaining))
			self.change_window(self.rediger_kunde_rejse)
		else:
			if pladser == "":
				self.rediger_kunde_rejse_button_frame_label_missing_info.configure(text="Manglende information")
				return
			try:
				plads = int(pladser)
			except ValueError:
				self.rediger_kunde_rejse_button_frame_label_missing_info.configure(text="Vær sød kun at bruge tal")
				return
			if plads < 1:
				self.rediger_kunde_rejse_button_frame_label_missing_info.configure(text="Du kan ikke book færre end 1...")
				return
			if plads > remaining:
				self.rediger_kunde_rejse_button_frame_label_missing_info.configure(text="Der er ikke nok pladser")
				return
			pbdb.change_booking_data(booking.id, plads)
			self.rediger_kunde_rejse_button_frame_label_missing_info.configure(text="")
			self.rediger_kunde_rejse_entry_pladser.delete(0, tk.END)
			self.refresh_booking_treeview()
			self.selected = [-1, "", 0]
			self.change_window(self.kunde_frame)

	def delete_account(self):
		pbdb.soft_delete_account(pbdb.get_record(pbd.Kunde, self.kundeid))
		for bookinger in pbdb.get_all_bookinger(self.kundeid):
			pbdb.soft_delete_booking(bookinger)
		self.selected = [-1, "", 0]
		refresh_treeview(self.acc_treeview, pbdb.select_all(pbd.Kunde))
		self.change_window(self.acc_frame)

	def save_account(self):
		self.rediger_account_label_missing_info.configure(fg=self.error_color)
		efternavn = self.rediger_account_entry_1.get()
		kontaktinfo = self.rediger_account_entry_2.get()
		if efternavn == "" or kontaktinfo == "":
			self.rediger_account_label_missing_info.configure(text="Manglende information")
			return
		self.rediger_account_entry_1.delete(0, tk.END)
		self.rediger_account_entry_2.delete(0, tk.END)
		self.rediger_account_label_missing_info.configure(text="Saved", fg=self.successful_color)
		pbdb.change_account_data(self.kundeid, efternavn, kontaktinfo)
		refresh_treeview(self.acc_treeview, pbdb.select_all(pbd.Kunde))

	def save_rejse(self):
		self.rediger_rejse_label_missing_info.configure(fg=self.error_color)
		if self.rediger_rejse_entry_1.get() == "" or self.rediger_rejse_entry_2.get() == "":
			self.rediger_rejse_label_missing_info.configure(text="Manglende information")
			return
		try:
			plads = int(self.rediger_rejse_entry_3.get())
		except ValueError:
			self.rediger_rejse_label_missing_info.configure(text="Pladskapacitet skal være et tal!")
			return
		self.rediger_rejse_label_missing_info.configure(text="Saved", fg=self.successful_color)
		pbdb.change_rejse_data(self.selected[0], self.rediger_rejse_entry_1.get(), self.rediger_rejse_entry_2.get(), plads)
		refresh_treeview(self.admin_treeview, pbdb.select_all(pbd.Rejse))

	def rediger_rejse(self):
		if not self.selected[1] == "rejseid" or self.selected[0] == -1:
			return
		self.rediger_rejse_label_1.configure(text="Redigerer rejse id: " + str(self.selected[0]))
		rejse = pbdb.get_record(pbd.Rejse, self.selected[0])
		self.rediger_rejse_entry_1.delete(0, tk.END)
		self.rediger_rejse_entry_2.delete(0, tk.END)
		self.rediger_rejse_entry_3.delete(0, tk.END)
		self.rediger_rejse_entry_1.insert(0, rejse.rute)
		self.rediger_rejse_entry_2.insert(0, rejse.dato)
		self.rediger_rejse_entry_3.insert(0, rejse.pladskapacitet)
		self.change_window(self.rediger_rejse_frame)

	def unbook_rejse(self):
		if not self.selected[1] == "bookingid" or self.selected[0] == -1:
			return
		pbdb.soft_delete_booking(pbdb.get_record(pbd.Booking, self.selected[0]))
		self.selected = [-1, "", 0]
		self.refresh_booking_treeview()
		self.refresh_available_rejser_treeview()

	def book_rejse(self, pladser=None):
		if not self.selected[1] == "bookrejse" or self.selected[0] == -1:
			return
		rejse = pbdb.get_record(pbd.Rejse, self.selected[0])
		remaining = get_remaining_slots(rejse.id)
		if pladser is None:
			self.kunde_book_rejse_label_1.configure(text="Rejse id: " + str(rejse.id))
			self.kunde_book_rejse_label_2.configure(text="Rute: " + rejse.rute)
			self.kunde_book_rejse_label_3.configure(text="Dato: " + rejse.dato)
			self.kunde_book_rejse_label_4.configure(text="Plads tilbage: " + str(remaining))
			self.change_window(self.kunde_book_rejse_frame)
		elif pladser is not None:
			if pladser == "":
				self.kunde_book_rejse_button_frame_label_missing_info.configure(text="Manglende information")
				return
			try:
				plads = int(pladser)
			except ValueError:
				self.kunde_book_rejse_button_frame_label_missing_info.configure(text="Vær sød kun at bruge tal")
				return
			if plads < 1:
				self.kunde_book_rejse_button_frame_label_missing_info.configure(text="Du kan ikke book færre end 1...")
				return
			if plads > remaining:
				self.kunde_book_rejse_button_frame_label_missing_info.configure(text="Der er ikke nok pladser")
				return
			pbdb.insert_data(pbd.Booking(rejseid=rejse.id, kundeid=self.kundeid, pladser=plads))
			self.kunde_book_rejse_button_frame_label_missing_info.configure(text="")
			self.kunde_book_rejse_entry_pladser.delete(0, tk.END)
			self.refresh_available_rejser_treeview()
			self.refresh_booking_treeview()
			self.selected = [-1, "", 0]
			self.change_window(self.kunde_frame)

	def refresh_booking_treeview(self):
		empty_treeview(self.kunde_frame_treeview_bookinger_treeview)
		bookinger = pbdb.get_all_bookinger(self.kundeid)
		values = []
		for booking in bookinger:
			rejse = pbdb.get_record(pbd.Rejse, booking.rejseid)
			value = [booking.id, rejse.rute, rejse.dato, booking.pladser]
			values.append(value)
		self.fill_booking_treeview(bookinger, values)

	def fill_booking_treeview(self, bookinger, values):
		color = 0
		count = 0
		for records in bookinger:
			if records.valid():
				if color % 2 == 0:
					self.kunde_frame_treeview_bookinger_treeview.insert(parent='', index='end', text='', values=values[count], tags='evenrow')
				else:
					self.kunde_frame_treeview_bookinger_treeview.insert(parent='', index='end', text='', values=values[count], tags='oddrow')
				color += 1
			count += 1

	def refresh_available_rejser_treeview(self):
		empty_treeview(self.kunde_frame_treeview_rejse_treeview)
		self.fill_available_rejser_treeview()

	def fill_available_rejser_treeview(self):
		rejser = pbdb.select_all(pbd.Rejse)
		bookinger = pbdb.get_all_bookinger(self.kundeid)
		bookederejser = []
		rejselist = []
		for booking in bookinger:
			if booking.valid():
				bookederejser.append(booking.rejseid)
		for rejse in rejser:
			remaining = get_remaining_slots(rejse.id)
			if remaining > 0 and rejse.id not in bookederejser:
				rejse.pladskapacitet = remaining
				rejselist.append(rejse)
		fill_treeview(self.kunde_frame_treeview_rejse_treeview, rejselist)

	def delete_rejse(self):
		if not self.selected[1] == "rejseid" or self.selected[0] == -1:
			return
		pbdb.soft_delete_rejse(pbdb.get_record(pbd.Rejse, self.selected[0]))
		for bookinger in pbdb.get_all_rejse_bookinger(self.selected[0]):
			pbdb.soft_delete_booking(bookinger)
		self.selected = [-1, "", 0]
		refresh_treeview(self.admin_treeview, pbdb.select_all(pbd.Rejse))

	def opret_rejse(self):
		rute = self.admin_entry_frame_rute_entry.get()
		dato = self.admin_entry_frame_dato_entry.get()
		pladskapacitet = self.admin_entry_frame_pladskapacitet_entry.get()
		if rute == "" or dato == "" or pladskapacitet == "":
			self.acc_create_label_frame_label_error.configure(text="Manglende information")
			return
		try:
			pbdb.insert_data(pbdb.Rejse(rute=rute, dato=dato, pladskapacitet=int(pladskapacitet)))
		except ValueError:
			self.acc_create_label_frame_label_error.configure(text="Pladskapacitet skal være et tal!")
			return
		refresh_treeview(self.admin_treeview, pbdb.select_all(pbd.Rejse))
		self.acc_create_label_frame_label_error.configure(text="")
		self.admin_entry_frame_rute_entry.delete(0, tk.END)
		self.admin_entry_frame_dato_entry.delete(0, tk.END)
		self.admin_entry_frame_pladskapacitet_entry.delete(0, tk.END)

	def login(self):
		if not self.selected[1] == "kundeid" or self.selected[0] == -1:
			return
		self.kundeid = self.selected[0]
		self.auth = self.selected[2]
		self.selected = [-1, "", 0]
		if self.auth == 1:
			self.change_window(self.admin_frame)
		else:
			self.change_window(self.kunde_frame)
			self.refresh_available_rejser_treeview()
			self.refresh_booking_treeview()

	def change_window(self, next_window):
		self.current_window.place_forget()
		next_window.place(relx=0.5, rely=0.5, anchor="center")
		self.current_window = next_window

	def create_account(self):
		efternavn = self.acc_create_label_frame_entry_efternavn.get()
		kontaktinfo = self.acc_create_label_frame_entry_kontaktinfo.get()
		if efternavn == "" or kontaktinfo == "":
			self.acc_create_label_frame_label_missing_info.configure(text="Manglende information")
			return
		self.acc_create_label_frame_entry_efternavn.delete(0, tk.END)
		self.acc_create_label_frame_entry_kontaktinfo.delete(0, tk.END)
		self.acc_create_label_frame_label_missing_info.configure(text="")
		self.kundeid = pbdb.insert_data(pbd.Kunde(efternavn=efternavn, kontakt=kontaktinfo, auth=pbd.PermissionLevel.LOW))
		refresh_treeview(self.acc_treeview, pbdb.select_all(pbd.Kunde))
		self.selected = [self.kundeid, "kundeid", 0]
		self.login()

	def select_id(self, treeview, type_):
		sel = treeview.focus()
		if len(sel) < 1:
			return
		values = treeview.item(sel, "values")
		self.selected = [int(values[0]), type_, int(values[3])]


def get_remaining_slots(id_):
	rejse = pbdb.get_record(pbd.Rejse, id_)
	slots = rejse.pladskapacitet
	for bookinger in pbdb.get_all_rejse_bookinger(rejse.id):
		if bookinger.valid():
			slots -= (bookinger.pladser if bookinger.pladser > 0 else 0)
	return slots


def empty_treeview(treeview):
	treeview.delete(*treeview.get_children())


def refresh_treeview(treeview, values, cond1=()):
	empty_treeview(treeview)
	fill_treeview(treeview, values, cond1)


def fill_treeview(treeview, values, cond1=()):
	count = 0
	for records in values:
		if records.valid():
			if records not in cond1:
				if count % 2 == 0:
					treeview.insert(parent='', index='end', text='', values=records.convert_to_tuple(), tags='evenrow')
				else:
					treeview.insert(parent='', index='end', text='', values=records.convert_to_tuple(), tags='oddrow')
				count += 1


if __name__ == "__main__":
	plusbus = Plusbus()
	plusbus.gui.mainloop()
