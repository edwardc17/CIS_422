'''
All code produced by the team - specifically Jiazhen Cao.
'''

import sys
from calendarGui import *
from calendarClasses import *
import datetime
import calendar
import random
if sys.version[0] == '2':
    from Tkinter import *
else:
    from tkinter import *

class UpdateCalendar():
	'''
	Creates and updates layout of 5 days.

	JC
	'''
	def __init__(self, dayPtr):
		self.dayPtr = dayPtr

	def createFiveDays(self, currentDay, mainFrame, frame):
		'''
		Creates template for 5 days on main window. 
		One column per day with the date at the top.
		'''
		for i in range(5):
			# Get correct day based on current day and number of days in the future.
			dateDelta = datetime.timedelta(days=i)
			tempDate = currentDay + dateDelta
			# Date label
			l_date = Label(mainFrame, width = 20, text = "{}".format(tempDate.strftime("%Y-%m-%d")))
			l_date.grid(row = 1, column = i + 1)
			# Store date label
			frame.currentDays[l_date.cget("text")] = l_date	

	def updateFiveDays(self, frame, plusOrMinus, currentCoef):
		'''
		
		'''
		for i in range(5):
			oldDateDelta = datetime.timedelta(days = i + self.dayPtr)
			newDateDelta = datetime.timedelta(days = i + (self.dayPtr + plusOrMinus * 5) * currentCoef)
			oldTempDate = (currentDay + oldDateDelta).strftime("%Y-%m-%d")
			newTempDate = (currentDay + newDateDelta).strftime("%Y-%m-%d")
			frame.currentDays[newTempDate] = frame.currentDays.pop(oldTempDate)
			frame.currentDays[newTempDate]["text"] = newTempDate
		for dayKey in frame.eventLabels:
			frame.eventLabels[dayKey].destroy()
			#frame.eventLabels.pop(dayKey)
		frame.loadLabels()
		self.dayPtr = (self.dayPtr + 5 * plusOrMinus) * currentCoef

	def initCalendar(self, frame):
		frame.loadLabels()

if __name__ == "__main__":
	'''
	Runs the program.

	JC
	'''
	root=Tk()
	root.resizable(width=False, height=False)
	# Layout of top of main window - main buttons and day labels
	f1 = Frame()
	# Layout of rest of window - day columns with events, hour labels
	f2 = GUI(root)
	dayPtr = 0
	update = UpdateCalendar(dayPtr)
	currentDay = datetime.datetime.now()

	# Inital layout of five days
	update.createFiveDays(currentDay, f1, f2)

	# Create main window buttons
	eventObj = EventObj("", "", "", "", "", "", f2.idx)
	createButton = Button(f1, text = "Create", width=13,\
		command = lambda: f2.onClick(eventObj, "", f2.idx, 0)).grid(row = 0,column=0, padx = 1, pady = 20)
	
	previousButton = Button(f1, text = "Previous Five Days", command = lambda : update.updateFiveDays(f2, -1, 1))
	previousButton.grid(row = 0, column = 1, columnspan = 2)

	currentButton = Button(f1, text = "current Five Days", command = lambda : update.updateFiveDays(f2, -1, 0))
	currentButton.grid(row = 0, column = 3)

	nextButton = Button(f1, text = "Next Five Days", command = lambda : update.updateFiveDays(f2, 1, 1))
	nextButton.grid(row = 0, column = 4, columnspan = 2)

	time_region = Label(f1, text = "GMT-08")
	time_region.grid(row = 1, column = 0)

	# Load events from last use of program
	update.initCalendar(f2)

	# Create grids for each frame
	f1.grid(row = 0, column = 0, padx = 10, sticky=W)
	f2.grid(row = 1, column = 0, sticky = N+S+W+E)

	root.mainloop()
