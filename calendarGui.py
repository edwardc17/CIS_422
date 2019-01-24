from Tkinter import Tk, Label, Button, Frame
from calendarClasses import *

class GUI:
	def __init__(self, rt):
		self.rt = rt
		rt.title("Calendar")
		self.cal = calendar("saveFile.dat")
		#self.events = self.cal.loadFile()
		self.labels = []

		self.frame = Frame(height=2, bd=1)
		self.frame.pack(fill='x', padx=5, pady=5)

		self.label = Label(rt, text = "Testing GUI!")
		self.label.pack()

		self.create = Button(rt, text = "Create", command = self.createEvent)
		self.create.pack()

		self.edit = Button(rt, text = "Edit", command = self.editEvent)
		self.edit.pack()

		self.close_button = Button(rt, text = "Close", command = rt.quit)
		self.close_button.pack()

	def createEvent(self):
		e = event("1pm", "2/1/19", "waffle")
		new = self.cal.addEvent(e)
		self.events = new
		# how to load new data?
		label=Label(self.rt,text=e.getEvent())
		label.pack()
		self.labels.append(label)
	
	def editEvent(self):
		events = self.cal.getEvents()
		for i in range(0, len(events)):
			events[i].editEventTime("2:30pm")
			self.labels[i]['text'] = events[i].getEvent()
		self.cal.saveFile()
		self.cal.loadFile()


root = Tk()
gui = GUI(root)
root.mainloop()