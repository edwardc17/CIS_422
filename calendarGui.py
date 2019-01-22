from tkinter import Tk, Label, Button

class GUI:
	def __init__(self, rt):
		self.rt = rt
		rt.title("Calendar")

		self.label = Label(rt, text = "Testing GUI!")
		self.label.pack()

		self.greetings = Button(rt, text = "Greet", command = self.greet)
		self.greetings.pack()

		self.close_button = Button(rt, text = "Close", command = rt.quit)
		self.close_button.pack()

	def greet(self):
		print("Greetings!")


root = Tk()
gui = GUI(root)
root.mainloop()