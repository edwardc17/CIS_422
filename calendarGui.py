from tkinter import *
from calendarClasses import *

class GUI(object):
	def __init__(self, rt):
		self.rt = rt
		rt.title("Calendar")
		self.cal = calendar("saveFile.dat")
		#self.events = self.cal.loadFile()
		self.labels = []

		self.frame = Frame(height=100, bd=1)
		#self.frame.pack(fill='x', padx=0, pady=0)

		#self.label = Label(rt, text = "Testing GUI!")
		#self.label.pack()

		self.create = Button(rt, text = "Create", width=8,command = self.createEvent).grid(row=0,column=0)
		#self.create.pack()

		self.edit = Button(rt, text = "Edit", width=8,command = self.editEvent).grid(row=1,column=0)
		#self.edit.pack()

		#an empty label for layout
		self.empty_label = Label(text='', width =10).grid(row=2,column=0)

		#show three day
		self.day1 = Label(text='Day 1', width=10).grid(row=3,column=1)
		self.day2 = Label(text='Day 2', width=10).grid(row=3,column=2)
		self.day3 = Label(text='Day 3', width=10).grid(row=3,column=3)

		#time scale
		self.timeScale = ['00:00 AM', '01:00 AM' , '02:00 AM', '03:00 AM', '04:00 AM', '05:00 AM',
						'06:00 AM', '07:00 AM', '08:00 AM', '09:00 AM', '10:00 AM', '11:00 AM',
						'12:00 PM', '01:00 PM', '02:00 PM', '03:00 PM', '04:00 PM', '05:00 PM',
						'06:00 PM', '0:7:00 PM', '08:00 PM', '09:00 PM', '10:00 PM', '11:00 PM', '12:00 PM']



		self.close_button = Button(rt, text = "Close", command = rt.quit)
		#self.close_button.pack()
		self.createTimescale()
		#self.scrollbar = Scrollbar(rt).grid(sticky='ns')

	def createEvent(self):
		e = event("1pm", "2/1/19", "waffle")
		new = self.cal.addEvent(e)
		self.events = new
		# how to load new data?
		label=Label(self.rt,text=e.getEvent())
		#label.pack()
		self.labels.append(label)
	
	def editEvent(self):
		events = self.cal.getEvents()
		for i in range(0, len(events)):
			events[i].editEventTime("2:30pm")
			self.labels[i]['text'] = events[i].getEvent()
		self.cal.saveFile()
		self.cal.loadFile()

	def createTimescale(self):
		r = 4
		for c in self.timeScale:
			Label(text=c, relief=RIDGE,width=15, height=2).grid(row=r,column=0)
			Label(bg= 'white', relief=GROOVE,width=20, height=2).grid(row=r,column=1)
			Label(bg= 'white', relief=GROOVE,width=20, height=2).grid(row=r,column=2)
			Label(bg= 'white', relief=GROOVE,width=20, height=2).grid(row=r,column=3)
			r = r + 1




root = Tk()
gui = GUI(root)

root.mainloop()