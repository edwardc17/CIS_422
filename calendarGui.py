#from Tkinter import *
import sys
from calendarClasses import *
from createEvent import *
from scrollFrame import *
import datetime
import calendar
import random
import gc
import pickle #test part for pickle save load data

if sys.version[0] == '2':
	from Tkinter import *
else:
	from tkinter import *

timeSlots = []
dayOneEvent = []
dayTwoEvent = []
dayThreeEvent = []
calendarData = {}	#test part for pickle save load data

#### timeslot class used for time labels
class TimeSlot:
	'''
	JN, GC
	'''
	def __init__(self, begin, label):
		self.label = label
		self.bTime = begin	# beginning time
		

class GUI(Frame):
	'''
	Main window.

	JC, GC
	'''
	def __init__(self, rt):
		# this seems like it was required to get windows with data transfer
		# 	working properly - john
		super(GUI, self).\
			__init__(rt)

		#Frame.__init__(self, rt)
		self.scrollFrame = ScrollFrame(self)
		self.rt = rt
		rt.title("Calendar")
		# For storing events
		self.cal = Calendar("saveFile.dat")
		self.labels = []
		self.currentDays = {}
		# EXPLAIN THIS
		self.idx = 0
		self.eventLabels = {}
		self.create_widgets()
		# For scroll bar
		self.scrollFrame.pack(side="top", fill="both", expand=True)
		self.load_data()	#test part for pickle
		print(self.winfo_width())


	def load_data(self):	#test part for pickle
		with open('calendar.pickle','rb') as f:
			calendar = pickle.load(f)
		calendarData = calendar
		for date,event_dic in calendarData.items():   
			if date == '2019-02-03':
				for event,eventItem in event_dic.items():
					print(eventItem[0])

	def create_widgets(self):
		'''
		Creates initial layout of main window with time scale labels
		and a popup window upon clicking the upper left corner exit button.

		GC? JC?
		'''
		#Time scale label text
		self.timeScale = ['00:00 AM', '01:00 AM' , '02:00 AM', '03:00 AM', '04:00 AM', '05:00 AM',
						'06:00 AM', '07:00 AM', '08:00 AM', '09:00 AM', '10:00 AM', '11:00 AM',
						'12:00 PM', '01:00 PM', '02:00 PM', '03:00 PM', '04:00 PM', '05:00 PM',
						'06:00 PM', '07:00 PM', '08:00 PM', '09:00 PM', '10:00 PM', '11:00 PM']
		# Handles upper left corner red x button
		self.master.protocol("WM_DELETE_WINDOW", self.exit)
		self.createTimescale()

	def exit(self):
		'''
		Popup window asking user whether to exit calendar program or continue using.

		Based on: https://stackoverflow.com/questions/16242782/change-words-on-tkinter-messagebox-buttons
		
		CP
		'''
		window = Toplevel()

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

		JC, CP
		'''
		gc.collect()
		self.scrollFrame.viewPort.destroy()
		self.rt.destroy()


	def createTimescale(self):
		'''
		Creates timescale slots in each of three dates for events to appear.
		Each label has 12 parts horizontally to allow for choosing at 5 minute intervals.

		GC, JN
		'''
		row = 0
		for time in self.timeScale:
			# Timeslot label
			Label(self.scrollFrame.viewPort, text=time, relief=RIDGE,width=15, height=2).grid(row=row,column=0, rowspan = 12)
			
			# creates empty timeslot slots
			dayOneTime = Label(self.scrollFrame.viewPort, bg= 'white', relief=GROOVE,width=20, height=2)
			dayOneTime.grid(row=row, column=1, rowspan = 12)
			dayOneEvent.append(dayOneTime)

			dayTwoTime = Label(self.scrollFrame.viewPort, bg= 'grey', relief=GROOVE,width=20, height=2)
			dayTwoTime.grid(row=row,column=2,  rowspan = 12)
			dayTwoEvent.append(dayTwoTime)

			dayThreeTime = Label(self.scrollFrame.viewPort, bg= 'white', relief=GROOVE,width=20, height=2)
			dayThreeTime.grid(row=row,column=3,  rowspan = 12)
			dayThreeEvent.append(dayThreeTime)

			dayFourTime = Label(self.scrollFrame.viewPort, bg= 'grey', relief=GROOVE,width=20, height=2)
			dayFourTime.grid(row=row,column=4,  rowspan = 12)

			dayFiveTime = Label(self.scrollFrame.viewPort, bg= 'white', relief=GROOVE,width=20, height=2)
			dayFiveTime.grid(row=row,column=5,  rowspan = 12)
			
			#### declare timeslot to add to array (begintime, label)
			slot1 = TimeSlot(time, dayOneTime)
			slot2 = TimeSlot(time, dayTwoTime)
			slot3 = TimeSlot(time, dayThreeTime)

			timeSlots.append(slot1)
			timeSlots.append(slot2)
			timeSlots.append(slot3)

			row = row + 12 
			

	# when clicking on event display
	def onClick(self, event_name, start_time, end_time, date, description, idx, exist):

		self.top = Toplevel()
		if exist == 0:
			self.top.title("Adding an Event")
		else:
			self.top.title("Editing Or Removing an Event")

		self.appc = CreateEvent(self.scrollFrame.viewPort, self, self.top, event_name, start_time, end_time, date, description, idx, exist)
