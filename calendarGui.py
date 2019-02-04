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

def onClick(event, guiObj, timeSlot):
	'''

	'''
	print ("you clicked on", guiObj, "and timeslot ", timeSlot)
	row    = event.widget.grid_info()['row']
	column = event.widget.grid_info()['column']
	#this could be helpful for store and write information
	print ("row =", row, "column = ", column)
	guiObj.modifyDayBox(timeSlot,row,column)

#### timeslot with associated labels and times (clickable spots)
# TODO: define daytime variables (could just need start -and date- and make ending 1 hour later)
class TimeSlot:
	'''
	GC
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
		#super(GUI, self).\
		#	__init__(rt)

		Frame.__init__(self, rt)
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
			

	#### creates a new window that is a child to the GUI parent frame
	# john: "pretty much copied this from the example"
	def modifyDayBox(self,timeSlot,row,column):
		'''
		
		JN - find source
		'''
		self.top = Toplevel()
		self.top.title("Modify Time Slot")
		self.top.geometry("300x150+30+30")
		self.top.transient(self)
		self.appc=AddEventPopUp(self.top, self.eventSpots, timeSlot,row,column)

	# THIS IS OLD?
	def onClick(self, event_name, start_time, end_time, date, description, idx, exist):

		self.top = Toplevel()
		if exist == 0:
			self.top.title("Adding an Event")
		else:
			self.top.title("Editing Or Removing an Event")

		self.appc = CreateEvent(self.scrollFrame.viewPort, self, self.top, event_name, start_time, end_time, date, description, idx, exist)

# ARE WE STILL USING THIS?
#### class for the pop up when clicking on a time slot in the day-time breakdown
# john: "essentially designed from the example"	
class AddEventPopUp(object):
	def __init__(self, master, eventsList, timeSlot,row,column):
		self.master = master
		# create new window
		self.frame = Frame(self.master)
		self.eventsList = eventsList
		self.timeslot = timeSlot # This is not the correct time?

		self.AddEvent(row,column)

	def on_closing(self):
		'''

		'''
		result = messagebox.askyesno("Save", "Save the event?")
		if result == True:
			print("worked")
			self.master.destroy()
		
	def close(self):
		'''

		'''
		self.frame.destroy()
		self.master.destroy()

#### main program area
# john: "i changed it to work from root to a master window (so it works easier on windows 10 - i'm selfish)"
'''
master_window = Tk()
gui = GUI(master_window)
gui.pack(side="top", fill="both", expand=True)
master_window.mainloop()
'''