import pickle
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

class event:
	def __init__(self, time, date, text):
		self.time = time
		self.date = date
		self.text = text

	def printEvent(self):
		print("date: " + self.date + " time: " + self.time + " text: " + self.text)

class calendar:
	def __init__(self, filename):
		self.events = [] # Data for saving
		self.file = filename

	
	def loadFile(self):
		# Manipulation of data happens outside of function
		with open(self.file, 'rb') as file:
			obj = pickle.load(file)
			return obj

	def saveFile(self):
		# Any new additions must be appended to the whole data collection.
		# Problematic if data collection becomes very large,
		# but would be working with the collection anyway.
		with open(self.file, 'wb') as file:
			pickle.dump(self.events, file, protocol=2)

	def addEvent(self, event):
		# create event here or just pass it?
		self.events.append(event)
		self.saveFile() 
		#loadFile() # Need to load for GUI? but not here?

	def removeEvent(self, event):
		self.events.remove(event)
		self.saveFile()
		#loadFile() # Need to load for GUI? but not here?

	def printCal():
		for i in self.events:
			i.printEvent()

root = Tk()
gui = GUI(root)
root.mainloop()