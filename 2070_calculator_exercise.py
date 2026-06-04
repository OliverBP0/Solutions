import tkinter as tk


class Calculator:

	def __init__(self):
		self.gui_background_color = "#202020"
		self.button_press_color = "#3F3B38"
		self.button_press_text_color = "#CECECE"
		self.button_color = "#35312D"
		self.equals_button_color = "#B9B3F7"
		self.equals_button_text_color = "#343245"
		self.equals_button_press_color = "#A9A4E1"
		self.equals_button_press_text_color = "#2F2E3F"
		self.text_color = "#FFFFFF"
		self.action_text = ""
		self.action_color = "#999999"
		self.font_size = 30
		self.action = 0
		self.number = [0.0, None]
		self.comma = False

		self.gui = tk.Tk()
		self.gui.title("Calculator")

		self.gui.resizable(False, False)
		self.gui.configure(bg=self.gui_background_color)

		self.result_frame = tk.Frame(self.gui, bg=self.gui_background_color, width=350, height=100)
		self.result_frame.grid_propagate(False)
		self.result_frame.grid(row=0, column=0)

		self.action_label = tk.Label(self.result_frame, bg=self.gui_background_color, text=self.action_text, font=("Arial", 20), fg=self.action_color)
		self.action_label.grid(row=0, column=0, pady=8, sticky="w")
		self.result_label = tk.Label(self.result_frame, bg=self.gui_background_color, text=str(self.format_number(self.number[0])), font=("Arial", self.font_size), fg=self.text_color)
		self.result_label.grid(row=1, column=0, sticky="w")
		self.set_result(self.number[0])

		self.button_frame = tk.Frame(self.gui, bg=self.gui_background_color, width=350, height=335)
		self.button_frame.grid_propagate(False)
		self.button_frame.grid(row=1, column=0)

		self.pixel = tk.PhotoImage(width=1, height=1)
		self.button_frame.update_idletasks()
		self.button_slet = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "⌫", lambda: self.button_press(1), text_size=30)
		self.button_clear = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "C", lambda: self.button_press(0), text_size=30)
		self.button_squared = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "x²", lambda: self.button_press(2))
		self.button_divider = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "÷", lambda: self.button_press(3))
		self.button_7 = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "7", lambda: self.button_press(4, 7))
		self.button_8 = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "8", lambda: self.button_press(5, 8))
		self.button_9 = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "9", lambda: self.button_press(6, 9))
		self.button_gange = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "×", lambda: self.button_press(7))
		self.button_4 = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "4", lambda: self.button_press(8, 4))
		self.button_5 = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "5", lambda: self.button_press(9, 5))
		self.button_6 = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "6", lambda: self.button_press(10, 6))
		self.button_minus = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "−", lambda: self.button_press(11))
		self.button_1 = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "1", lambda: self.button_press(12, 1))
		self.button_2 = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "2", lambda: self.button_press(13, 2))
		self.button_3 = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "3", lambda: self.button_press(14, 3))
		self.button_plus = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "+", lambda: self.button_press(15))
		self.button_invert = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "±", lambda: self.button_press(16))
		self.button_0 = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, "0", lambda: self.button_press(17, 0))
		self.button_komma = Button(self.button_frame, self.pixel, self.button_color, self.button_press_color, self.text_color, self.button_press_text_color, ",", lambda: self.button_press(18))
		self.button_equals = Button(self.button_frame, self.pixel, self.equals_button_color, self.equals_button_press_color,
		                            self.equals_button_text_color, self.equals_button_press_text_color, "=", lambda: self.button_press(19))

	# self.equals_frame = tk.Frame(self.gui, bg=self.gui_background_color, width=350, height=65)
	# self.equals_frame.grid_propagate(False)
	# self.equals_frame.grid(row=2, column=0)
	# self.equals = Button(self.equals_frame, self.pixel, self.equals_button_color, self.equals_button_press_color, self.equals_button_text_color,
	# 					 self.equals_button_press_text_color, "=", lambda: print("Test"), 350, 65, 80)

	def set_result(self, number):
		formatted_num = str(self.format_number(number))
		new_size = (30 - (len(formatted_num) - 15) * 2) if len(formatted_num) > 15 else 30
		self.font_size = new_size if new_size > 15 else 15
		self.result_label.configure(text=str(self.format_number(number)), font=("Arial", self.font_size))

	def set_action_text(self, action):
		self.action_text = action
		self.action_label.configure(text=self.action_text, fg=self.action_color)

	def format_number(self, number):
		try:
			if abs(number) < 1000000000:
				if number.is_integer():
					return f"{int(number):,}".replace(",", ".")

				integer, decimal = f"{number}".split(".")
				integer = f"{int(integer):,}".replace(",", ".")
				return f"{integer},{decimal}"
			return f"{number:.8e}"
		except OverflowError:
			self.action_color = "#ff0000"
			self.set_action_text("Tallet er blevet for stort.")
			raise OverflowError

	def button_press(self, number, numbered_button=None):
		if number == 0:
			self.comma = False
			self.action = 0
			self.number = [0.0, None]
			self.action_color = "#999999"
			self.set_result(0)
			self.set_action_text("")
		try:
			str_number = [str(self.number[0]), str(self.number[1])]
			len_number = [len(str_number[0]), len(str_number[1]) if self.number[1] is not None else 0]
			current_num = 0 if self.action == 0 else 1
			self.action_color = "#999999"
			match number:
				case 0:
					return
				case 1:
					self.comma = False
					if self.number[current_num] is None or len_number[current_num] < 2:
						self.number[current_num] = 0
					if len_number[current_num] > 1:
						self.number[current_num] = float(str_number[current_num][:-1] if str_number[current_num][:-1] != "-" else "0")
					self.set_result(self.number[current_num])
					if self.number[0].is_integer():
						self.number[0] = int(self.number[0])
					if self.number[1] is not None and self.number[1].is_integer():
						self.number[1] = int(self.number[1])
				case 2:
					self.comma = False
					if self.number[current_num] is None:
						self.number[current_num] = 0
					self.set_action_text(f"x²({self.format_number(self.number[current_num])})")
					self.number[current_num] **= 2
					self.set_result(self.number[current_num])
				case 4 | 5 | 6 | 8 | 9 | 10 | 12 | 13 | 14 | 17:
					if self.number[current_num] is None or self.number[current_num] == 0:
						self.number[current_num] = numbered_button
					else:
						self.number[current_num] = float(str_number[current_num] + str(numbered_button))
					self.set_result(self.number[current_num])
					if not self.comma:
						if self.number[0].is_integer():
							self.number[0] = int(self.number[0])
						if self.number[1] is not None and self.number[1].is_integer():
							self.number[1] = int(self.number[1])
				case 3 | 7 | 11 | 15:
					self.comma = False
					operators = {3: "÷", 7: "×", 11: "−", 15: "+"}
					operator = operators[number]
					if self.action == number:
						if self.number[1] is None:
							self.operator(self.number[0], operator)
							self.set_result(self.number[0])
						else:
							self.operator(self.number[1], operator)
							self.number[1] = None
							self.set_result(self.number[0])
						return
					elif self.action != 0:
						self.button_press(self.action)
					else:
						self.set_result(0)
					self.action = number
					self.set_action_text(f"{self.format_number(self.number[0])} {operator}")
				case 19:
					if self.action != 0:
						self.comma = False
						self.button_press(self.action)
						self.action = 0
				case 16:
					self.set_action_text(f"Negate({self.format_number(self.number[current_num])})")
					self.number[current_num] *= -1
					self.set_result(self.number[current_num])
				case 18:
					if "." in str_number[current_num]:
						return
					self.number[current_num] = str_number[current_num] + "."
					self.comma = True
				case _:
					self.set_action_text("How did you do this...")
		except Exception as error:
			if isinstance(error, OverflowError):
				return
			self.action_color = "#ff0000"
			self.set_action_text("Der er opstået en fejl.")
			print(f"{type(error).__name__}: {error} (at line {error.__traceback__.tb_lineno})")

	def operator(self, number, operator):
		self.set_action_text(f"{self.format_number(self.number[0])} {operator} {self.format_number(number)}")
		match operator:
			case "÷":
				self.number[0] /= number
			case "×":
				self.number[0] *= number
			case "−":
				self.number[0] -= number
			case "+":
				self.number[0] += number


class Button:
	instances = 0
	horizontal_buttons = 4

	def __init__(self, frame, pixel, background_color, focused_color, text_color, focused_text_color, text, command, button_width=None, button_height=None, text_size=None):
		row = Button.get_instances() // Button.horizontal_buttons
		column = Button.get_instances() - (row * Button.horizontal_buttons)
		if button_width is None:
			button_width = int(frame.winfo_width() / Button.horizontal_buttons - 3)  # Ikke ligefrem perfekt aligned hvis man ændrer horizontal_buttons for meget, men kunne ikke lige finde ud af hvorfor den ikke gad at perfekt align uden -3, selv hvis du satte horizontal_buttons til noget lige som fks 5
		if button_height is None:
			button_height = int(button_width * 0.75)
		if text_size is None:
			text_size = button_width // 2
		self.button = tk.Button(frame, text=text, image=pixel, font=("Arial", text_size),
		                        width=button_width, height=button_height, compound="center",
		                        bd=0, bg=background_color, activebackground=focused_color,
		                        anchor="center", relief="flat", fg=text_color,
		                        activeforeground=focused_text_color, command=command)
		self.button.grid(row=row, column=column)
		Button.instances += 1

	@staticmethod
	def get_instances():
		return Button.instances


if __name__ == "__main__":
	calculator = Calculator()
	calculator.gui.mainloop()