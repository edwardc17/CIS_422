#from Tkinter import *
import sys
from calendarClasses import *
from createEvent import *
from scrollFrame import *
import datetime
import calendar
import random
import gc

if sys.version[0] == '2':
	from Tkinter import *
else:
	from tkinter import *

class GUI(Frame):
	'''
	Main window.

	JC, JN, GC
	'''
	def __init__(self, rt):
		super(GUI, self).\
			__init__(rt)

		Frame.__init__(self, rt)
		# Allows a scrollbar to see all 24 hours
		self.scrollFrame = ScrollFrame(self)
		self.rt = rt
		rt.title("Calendar")
		# For storing events
		self.cal = Calendar("saveFile.dat")
		self.cal.events = self.cal.loadFile()
		self.labels = []
		# Stores 5 days currently shown
		self.currentDays = {}
		# Current index
		self.idx = 0
		# Stores all even
		self.eventLabels = {}
		# Creates initial layout
		self.create_widgets()
		# For scroll bar
		self.scrollFrame.pack(side="top", fill="both", expand=True)

	def create_widgets(self):
		'''
		Creates initial layout of main window with time scale labels
		and a popup window upon clicking the upper left corner exit button.

		GC, JC
		'''
		#Time scale label text
		self.timeScale = ['00:00 AM', '01:00 AM' , '02:00 AM', '03:00 AM', '04:00 AM', '05:00 AM',
						'06:00 AM', '07:00 AM', '08:00 AM', '09:00 AM', '10:00 AM', '11:00 AM',
						'12:00 PM', '01:00 PM', '02:00 PM', '03:00 PM', '04:00 PM', '05:00 PM',
						'06:00 PM', '07:00 PM', '08:00 PM', '09:00 PM', '10:00 PM', '11:00 PM']
		# Handles upper left corner red x button
		self.master.protocol("WM_DELETE_WINDOW", self.exit)
		# Create layout with timescale labels
		self.createTimescale()

	def exit(self):
		'''
		Popup window asks user whether to exit calendar program or continue using it.

		Based on: https://stackoverflow.com/questions/16242782/change-words-on-tkinter-messagebox-buttons
		
		CP
		'''
		# Accesses popup window to manipulate it
		window = Toplevel()

		# Inital title and text
		window.title('warning')
		message = "You may lose any unsaved changes"
		Label(window, text=message).pack()
		# Destroys current popup window, returns to main window
		Button(window, text='Go back to calendar', command=window.destroy).pack()
		# destroys current popup window and main window, exits program
		Button(window, text='I already saved my changes!', command=self.deleteAll).pack()

	def deleteAll(self):
		'''
		Destroy everything in main window and close program.

		CP, JC
		'''
		gc.collect() # Python's garbage collector
		self.scrollFrame.viewPort.destroy() # Destroy frame placed on top of main frame
		self.rt.destroy() # Destroy everything else


	def createTimescale(self):
		'''
		Creates timescale slots in each of three dates for events to appear.
		Each label has 12 parts horizontally to allow for choosing at 5 minute intervals.

		GC, JN
		'''
		row = 0
		for time in self.timeScale:
			# Timeslot label - rowspan divides each label into 12 parts, 
			# so that time can be partitioned down to 5 minutes
			Label(self.scrollFrame.viewPort, text=time, relief=RIDGE,width=15, height=2)\
			.grid(row=row,column=0, rowspan = 12)
			
			# Creates empty timeslot slots for each day/column
			dayOneTime = Label(self.scrollFrame.viewPort, bg= 'white', relief=GROOVE,width=20, height=2)
			dayOneTime.grid(row=row, column=1, rowspan = 12)

			dayTwoTime = Label(self.scrollFrame.viewPort, bg= 'grey', relief=GROOVE,width=20, height=2)
			dayTwoTime.grid(row=row,column=2,  rowspan = 12)

			dayThreeTime = Label(self.scrollFrame.viewPort, bg= 'white', relief=GROOVE,width=20, height=2)
			dayThreeTime.grid(row=row,column=3,  rowspan = 12)

			dayFourTime = Label(self.scrollFrame.viewPort, bg= 'grey', relief=GROOVE,width=20, height=2)
			dayFourTime.grid(row=row,column=4,  rowspan = 12)

			dayFiveTime = Label(self.scrollFrame.viewPort, bg= 'white', relief=GROOVE,width=20, height=2)
			dayFiveTime.grid(row=row,column=5,  rowspan = 12)
			
			# Row is adjusted for the 12 partitions given to each label.
			row = row + 12 
			
	def loadLabels(self):
		'''
		Load Labels that in current 5 days from saveFile.dat
		
		JC
		'''
		i = 0
		for day in self.currentDays:
			if day in self.cal.events:
				for e in self.cal.events[day]:
					initLabel = InitLabel(self, self.scrollFrame.viewPort, day, e, i)
					i += 1
		self.idx = i

	def onClick(self, event, date, idx, exist):
		'''
		Handles user clicking on events or "Create" button.
		
		JC
		'''
		self.top = Toplevel() # To provide main window access to "CreateEvent" class
		if exist == 0:
			# User clicked "Create" button in upper left corner of main window
			self.top.title("Adding an Event")
		else:
			# User clicked on a previously created event in calendar
			self.top.title("Editing Or Removing an Event")
		# Open popup window to add or create event
		self.appc = CreateEvent(self.scrollFrame.viewPort, self, self.top, \
			event, date, idx, exist)

class InitLabel(object):
	def __init__(self, root, canvas, day, eventObject, i):
		self.root = root
		self.canvas = canvas
		self.day = day
		self.e = eventObject
		self.i = i
		self.createLabel()

	def createLabel(self):
		col_num = int(self.root.currentDays[self.day].grid_info()['column'])
		start_h = int(self.e.start_time[0] + self.e.start_time[1])
		start_m = int(self.e.start_time[2] + self.e.start_time[3])
		end_h = int(self.e.end_time[0] + self.e.end_time[1])
		end_m = int(self.e.end_time[2] + self.e.end_time[3])
		span = (end_h * 60 + end_m - start_h * 60 - start_m) * 12 / 60
		self.l_event = Label(self.canvas, text = "{}".format(self.e.name), \
			bg = self.e.color)
		self.l_event.grid(row = int(start_h * 12 + start_m * 12 / 60) , \
			column = col_num, rowspan = int(span), sticky = N+S+W+E)
		self.root.eventLabels[self.i] = self.l_event
		self.root.eventLabels[self.i].bind("<1>", \
			lambda event : self.root.onClick(self.e, self.day, self.i, 1))

