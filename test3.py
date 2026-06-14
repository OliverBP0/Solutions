import tkinter as tk
from tkinter import ttk
import test as pbd
import test2 as pbdb


class Plusbus:
	def __init__(self):
		self.gui_background_color = "#2E2E2E"
		self.secondary_bg_color = "#4F4F4F"
		self.test_color = "#0045FF"
		self.button_press_color = "#696969"
		self.text_color = "#FFFFFF"
		self.error_color = "#FF0000"
		self.row_height = 20
		self.account = None

		self.gui = tk.Tk()
		self.gui.title("Plus bus app")
		self.gui.geometry("800x700")
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
		self.tree_view_style.map("Treeview", background=[("selected", self.text_color)])

		self.acc_scollbar = tk.Scrollbar(self.acc_acc_frame)
		self.acc_scollbar.grid(row=0, column=1, pady=(30, 0), sticky="ns")
		self.acc_treeview = ttk.Treeview(self.acc_acc_frame, yscrollcommand=self.acc_scollbar.set, selectmode="browse")
		self.acc_treeview.grid(row=0, column=0, pady=(30, 0))
		self.acc_scollbar.config(command=self.acc_treeview.yview)

		self.acc_treeview['columns'] = "accounts"
		self.acc_treeview.column("#0", width=0, stretch=tk.NO)
		self.acc_treeview.column("accounts", width=300, anchor="w")

		self.acc_treeview.heading("#0", text="", anchor="w")
		self.acc_treeview.heading("accounts", text="Accounts", anchor="center")

		self.acc_button_frame = tk.Frame(self.acc_frame, bg=self.gui_background_color)
		self.acc_button_frame.pack()

		self.acc_button_login = tk.Button(self.acc_button_frame, text="Login", relief="flat", bg=self.secondary_bg_color, fg=self.text_color, activebackground=self.button_press_color, font=("Arial", 15))
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
		self.account = Account(-1, efternavn, kontaktinfo, PermissionLevel.LOW)
		self.change_window(self.acc_frame)


class Account:
	def __init__(self, id_, efternavn, kontaktinfo, permissionlevel):
		self.id = id_
		self.efternavn = efternavn
		self.konktaktinfo = kontaktinfo
		self.auth = permissionlevel
		self.kunde = pbdb.get_record(pbd.Kunde, self.id)
		if self.kunde is None:
			self.id = pbdb.insert_data(pbd.Kunde(efternavn=self.efternavn, kontakt=kontaktinfo, auth=self.auth))
			self.kunde = pbdb.get_record(pbd.Kunde, self.id)


class PermissionLevel:
	LOW = 0
	HIGH = 1


if __name__ == "__main__":
	plusbus = Plusbus()
	plusbus.gui.mainloop()
