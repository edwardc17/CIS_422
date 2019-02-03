#from Tkinter import *
import sys
from calendarClasses import *
from createEvent import *
import datetime
import calendar
import random
#import tkinter
#import tkinter.messagebox
##import tkinter.messagebox
#from Tkinter import messagebox
#import tkMessageBox as messagebox
# these options work for python3
#from tkinter import *
#from tkinter import messagebox

if sys.version[0] == '2':
	from Tkinter import *
else:
	from tkinter import *

# global variable to see if save button was pressed
credit = 0
# global dict for timeslots, key: day
#timeSlots = {}
timeSlots = []
dayOneEvent = []
dayTwoEvent = []
dayThreeEvent = []
#### click recorder for clicking on labels for time ###
# this was also required in order to wait for clicking
# 	in a box before creating additional windows - john

def onClick(event, guiObj, timeSlot):
	print ("you clicked on", guiObj, "and timeslot ", timeSlot)
	row    = event.widget.grid_info()['row']
	column = event.widget.grid_info()['column']
	#this could be helpful for store and write information
	print ("row =", row, "column = ", column)
	guiObj.modifyDayBox(timeSlot,row,column)

#### timeslot with associated labels and times (clickable spots)
# TODO: define daytime variables (could just need start -and date- and make ending 1 hour later)
class TimeSlot:
	def __init__(self, begin, label):
		self.label = label
		self.bTime = begin	# beginning time
		

class GUI(Frame, object):
	def __init__(self, rt):
		# this seems like it was required to get windows with data transfer
		# 	working properly - john
		super(GUI, self).\
			__init__(rt)

		self.rt = rt
		rt.title("Calendar")
		self.cal = Calendar("saveFile.dat")
		#self.events = self.cal.loadFile()
		self.labels = []
		# array for event spots (so they're clickable)
		self.eventSpots = []

		self.frame = Frame(height=100, bd=1)
		self.currentThreeDays = {}
		self.idx = 0
		self.eventLabelList = []
		#self.frame.pack(fill='x', padx=0, pady=0)
		self.create_widgets()

	def create_widgets(self):
		self.create = Button(self.rt, text = "Create", width=8,command = lambda: self.onClick("", "", "", "", "", self.idx, 0)).grid(row=0,column=0)
		#self.create.pack()

		#self.edit = Button(rt, text = "Edit", width=8,command = self.editEvent).grid(row=1,column=0)
		#self.edit.pack()

		#an empty label for layout
		self.empty_label = Label(self.rt, text='', width =10).grid(row=2,column=0)

		#currentDay = datetime.datetime.now().day
		#currentMonth = datetime.datetime.now().month
		#time1 = datetime.datetime.now().day
		#time1.strftime('%m/%d/%Y')
		##dates = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		#print(strftime("%B %d %Y, %X %Z",mktime(20,0,0,12,31,98)))
		#print(time1)
		self.day1 = Label(self.rt, width=10)
		self.day1['text'] = datetime.datetime.now().strftime("%Y-%m-%d")
		##print(self.day1['text'])
		self.day1.grid(row=3,column=1)

		currentDay = datetime.datetime.now()
		nextDay = datetime.timedelta(days=1)
		nextDays = currentDay + nextDay
		##print(nextDays)

		self.day2 = Label(self.rt, width=10)
		self.day2['text'] = nextDays.strftime("%Y-%m-%d")
		##print(self.day2['text'])
		self.day2.grid(row=3,column=2)


		dayThree = datetime.timedelta(days=2)
		twoDays = currentDay + dayThree


		self.day3 = Label(self.rt, width=10)
		self.day3['text'] = twoDays.strftime("%Y-%m-%d")
		##print(self.day3['text'])
		self.day3.grid(row=3,column=3)
		self.currentThreeDays[self.day1.cget("text")] = self.day1
		self.currentThreeDays[self.day2.cget("text")] = self.day2
		self.currentThreeDays[self.day3.cget("text")] = self.day3



		#time scale
		self.timeScale = ['00:00 AM', '01:00 AM' , '02:00 AM', '03:00 AM', '04:00 AM', '05:00 AM',
						'06:00 AM', '07:00 AM', '08:00 AM', '09:00 AM', '10:00 AM', '11:00 AM',
						'12:00 PM', '01:00 PM', '02:00 PM', '03:00 PM', '04:00 PM', '05:00 PM',
						'06:00 PM', '07:00 PM', '08:00 PM', '09:00 PM', '10:00 PM', '11:00 PM', '12:00 PM']


		#self.testEvent = Label(self.rt, text="event").grid(row=0, column=4)
		#this button closes the calendar 
		#self.close_button = Button(rt, text = "Close", command = rt.quit)

		#self.save_button = Button(rt, text="Save", command = self.addCredit()).grid(row=29, column=2)

		self.master.protocol("WM_DELETE_WINDOW", self.exit)
		#self.close_button = Button(rt, text = "Close", command = self.exit())
		#self.close_button.grid(row=29 ,column =4)

		self.createTimescale()
		#self.dayOneEvent[0].config(text='test')

	def clickEvent(self):
		self.widget.config(background = "green")

	'''
	#this was for a save button so when the save button was clicked it would go to addCredit function and
	#add 10 to the global variiable 'credit'. When you pressed exit it would go to a check function
	# that if credit was < 10 then save was not pressed so would display a warning and if > 10 then exit
	#
	def addCredit(self, credit):
		#found on stackoverflow https://stackoverflow.com/questions/22506298/checking-if-a-button-has-been-pressed-in-python
		#to see if a button has been pressed
		##edited though
		credit = credit + 10
		###print(credit)

	def check(self, credit):
		if credit < 10:
			self.exit()
	'''
	
	def exit(self):
		#maybe if credit is 0 then exit and if not show warning
		#global root
		##print(credit)
		#if credit < 10:
			#print("less than 10 in exit")

		#self.rt = rt
		#self.withdraw()
		#messagebox.showinfo("Warning", "Are you sure you want to leave without saving?")

		#else:
			#messagebox.showinfo("You saved you calendar", "Have a nice day!")

		#rt.quit()
		#root.quit()
		
		#if credit < 10:
		#https://stackoverflow.com/questions/16242782/change-words-on-tkinter-messagebox-buttons
		win = Toplevel()
		win.title('warning')
		message = "You may lose any unsaved changes"
		Label(win, text=message).pack()
		Button(win, text='Go back to calendar', command=win.destroy).pack()
		
		Button(win, text='I already saved my changes!', command=exit).pack()
		
	# getting ridof these
	'''
	def createEvent(self):
		e = event("1pm", "2/1/19", "waffle")
		new = self.cal.addEvent(e)
		self.events = new
		# how to load new data?
		label=Label(self.rt,text=e.getEvent())

		self.labels.append(label)
	'''
	def editEvent(self):
		events = self.cal.getEvents()
		for i in range(0, len(events)):
			events[i].editEventTime("2:30pm")
			self.labels[i]['text'] = events[i].getEvent()
		self.cal.saveFile()
		self.cal.loadFile()


	#### creates timescale slots where events can show up (presumably?)
	# john: "i modified this so the boxes are clickable. is this a layout design
	#		something you guys have settled on? it seems like we're going
	#		need to define start and end times for each time slot. "
	def createTimescale(self):
		r = 4
		for c in self.timeScale:
			Label(text=c, relief=RIDGE,width=15, height=1).grid(row=r,column=0, rowspan = 12)
			# creates timeslot slots
			
			dayOneTime = Label(bg= 'white', relief=GROOVE,width=20, height=1)
			#dayOneTime.bind("<1>", lambda event, obj=self: onClick(event, obj, dayOneTime))
			dayOneTime.grid(row=r, column=1, rowspan = 12)
			dayOneEvent.append(dayOneTime)

			dayTwoTime = Label(bg= 'grey', relief=GROOVE,width=20, height=1)
			#dayTwoTime.bind("<1>", lambda event, obj=self: onClick(event, obj, dayTwoTime))
			dayTwoTime.grid(row=r,column=2,  rowspan = 12)
			dayTwoEvent.append(dayTwoTime)

			dayThreeTime = Label(bg= 'white', relief=GROOVE,width=20, height=1)
			#dayThreeTime.bind("<1>", lambda event, obj=self: onClick(event, obj, dayThreeTime))
			dayThreeTime.grid(row=r,column=3,  rowspan = 12)
			dayThreeEvent.append(dayThreeTime)
			#### declare timeslot to add to array (begintime, label)
			# (need to input actual date?) yep
			slot1 = TimeSlot(c, dayOneTime)
			slot2 = TimeSlot(c, dayTwoTime)
			slot3 = TimeSlot(c, dayThreeTime)
			#if dayOneTime in timeSlots:
				#timeSlots[dayOneTime].append(slot1)
			timeSlots.append(slot1)
			timeSlots.append(slot2)
			timeSlots.append(slot3)

			r = r + 12 
			

	#### creates a new window that is a child to the GUI parent frame
	# john: "pretty much copied this from the example"
	def modifyDayBox(self,timeSlot,row,column):
		self.top = Toplevel()
		self.top.title("Modify Time Slot")
		self.top.geometry("300x150+30+30")
		self.top.transient(self)
		self.appc=AddEventPopUp(self.top, self.eventSpots, timeSlot,row,column)

	def onClick(self, event_name, start_time, end_time, date, description, idx, exist):
		self.top = Toplevel()
		self.top.title("title")
		self.top.geometry("1200x720")
		self.top.transient(self)
		self.appc = CreateEvent(self, self.top, event_name, start_time, end_time, date, description, idx, exist)


#### class for the pop up when clicking on a time slot in the day-time breakdown
# john: "essentially designed from the example"	
class AddEventPopUp(object):
	def __init__(self, master, eventsList, timeSlot,row,column):
		self.master = master
		# create new window
		self.frame = Frame(self.master)
		self.eventsList = eventsList
		self.timeslot = timeSlot # This is not the correct time

		self.AddEvent(row,column)
		#self.vText = ''

	def on_closing(self):
		#maybe if credit is 0 then exit and if not show warning
		#global root
		##print(credit)
		#if credit < 10:
			#print("less than 10 in exit")

		#self.rt = rt
		#self.withdraw()
		#messagebox.showinfo("Warning", "Are you sure you want to leave without saving?")

		#else:
			#messagebox.showinfo("You saved you calendar", "Have a nice day!")

		#rt.quit()
		#root.quit()
		
		#if credit < 10:
		#https://stackoverflow.com/questions/16242782/change-words-on-tkinter-messagebox-buttons
		'''
		win = Toplevel()
		win.title('warning')
		message = "You may lose any unsaved changes"
		Label(win, text=message).pack()
		Button(win, text='Stay', command=win.destroy).pack()
		'''
		#if tkinter.messagebox.askyesno("Print", "Print this report?"):
		result = messagebox.askyesno("Save", "Save the event?")
		if result == True:
			print("worked")
			self.master.destroy()
			##result.destroy()
			#result.print()
		
		#win = Toplevel()
		#Button(win, text='Exit Application',command=on_closing)
		#tk.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application',icon = 'warning')
		#messagebox.showinfo("Warning", "Are you sure you want to leave without saving?")
		#if MsgBox == 'yes':
			#win.destroy()
		#else:
			#tk.messagebox.showinfo('Return','You will now return to the application screen')
		
	def close(self):
		self.frame.destroy()
		self.master.destroy()

	# user pressed add event
	def AddEvent(self,row,column):
		print("adding event")
		print(row,column)
		self.row = row
		self.column = column
		self.lname = Label(self.master, width = 30, text = "Event name: ")
		self.v = StringVar()
		self.v.set('default')
		self.ename = Entry(self.master, textvariable = self.v)
		self.event_name = self.v.get()
		self.ldscrp = Label(self.master, text = "Event description: ")
		self.edscrp = Text(self.master, width = 30, height = 6)

		self.lname.grid(row = 1, column = 1, pady = 20)
		self.ename.grid(row = 1, column = 2, sticky=W, pady = 20)
		self.ldscrp.grid(row = 2, column = 1, pady = 20)
		self.edscrp.grid(row = 2, column = 2, sticky=W, pady = 20)

		self.subButton = Button(self.master, text = "submit",command = self.SubmitAdd)
		self.subButton.grid(row=3, column=2, pady = 20)

		self.master.protocol("WM_DELETE_WINDOW", self.on_closing)


		# event doesn't appear - don't know how to send it back
		# need time/date
		#text = self.text.get('1.0', 'end-1c')
		#print(self.vtext)
		#newEvent = event(self.timeslot, self.timeslot, text)
		#self.master.destroy()
		#print(self.timeslot) # wonky time
		#print(text)
		#self.eventsList.append(newEvent)
		#print(self.eventsList)
		#self.master.destroy()
		#TODO:  create fields for event info 
		#	add submit button
		#	send submission to calendar
		#	error check
		# 	detailed documentation, passed parameters, etc
	def add(self):
		eventName = self.ename.get()
		eventDesc = self.edscrp.get("1.0", "end-1c")
		print(eventDesc)
		#event = event(row, )
		self.eventsList.append(event("5", "today", eventName, eventDesc)) # doesn't fill original eventSpots
		self.timeslot["text"] = eventName # accesses last label in day's list
		print(self.eventsList)
		self.master.destroy()

	def SubmitAdd(self):

		self.event_name = self.v.get()
		print(self.event_name)
		#print(type(self.row),type(self.column))
		rowInt = int(self.row)
		columnInt = int(self.column)
		if columnInt == 1:
			dayOneEvent[rowInt - 4].config(text=self.event_name)
		elif columnInt == 2:
			dayTwoEvent[rowInt - 4].config(text=self.event_name)
		else:
			dayThreeEvent[rowInt - 4].config(text=self.event_name)

		eventObject = event(rowInt, day, self.event_name)

		'''
		
		print(type(self.timeslot))
		for slot in self.timeslot:
			if self.timeslot is slot.label:
				print("found it")
				slots.label['text'] = self.ename.get()
		'''

	#user pressed mod event	(could work identical to add event except modify just replaces previous entry in event list)
	def ModEvent(self):
		print("modding event")
		#destroy old layout, retains window
		for widget in self.master.winfo_children():
			widget.destroy()
		#TODO: put in fields for modification
		#	add submit button
		#	send submission to calendar
		#	error check
		# 	detailed documentation, passed parameters, etc

#from tkinter import *

'''
class Application(Frame, object):
	def __init__(self,  master):
		super(Application, self).\
			__init__(master)
		self.rt = master
		#self.buttonList = []
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		self.t1=Text(self,width=10,height=2)
		self.t1.grid(row=1,column=1)
		self.b1=Button(self,text="create",command=self.onClick)
		self.b1.grid(row=2,column=1)

	def onClick(self):
		self.top = Toplevel()
		self.top.title("title")
		self.top.geometry("1200x720")
		self.top.transient(self)
		self.appc = CreateEvent(self, self.top, self.t1)
'''

#### main program area
# john: "i changed it to work from root to a master window (so it works easier on windows 10 - i'm selfish)"
master_window = Tk()
gui = GUI(master_window)
master_window.mainloop()
