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

	'''
	def __init__(self, begin, label):
		'''

		'''
		self.label = label
		self.bTime = begin	# beginning time
		

class GUI(Frame, object):
	'''
	Main window of program. The time (00:00am to 12:00pm) appears on the left side. 
	Today and the next two days appear next to the time.
	A create button in the upper left corner allows for creating events.

	'''
	def __init__(self, rt):
		'''

		'''
		# this seems like it was required to get windows with data transfer
		# 	working properly - john
		super(GUI, self).\
			__init__(rt)

		self.rt = rt
		rt.title("Calendar")

		# Stores events between uses of the program
		self.cal = Calendar("saveFile.dat")

		self.labels = []
		# array for event spots (so they're clickable)
		self.eventSpots = []

		self.frame = Frame(height=100, bd=1)

		self.currentThreeDays = {}
		self.idx = 0
		self.eventLabelList = []

		self.create_widgets()


	def myfunction(self, event):
		'''

		'''
		canvas.configure(scrollregion=self.canvas.bbox("all"),width=200,height=200)

	def create_widgets(self):
		'''
		Creates initial layout - timescale, 3 days with slots and dates, exit warning

		'''
		self.create = Button(self.rt, text = "Create", width=8,command = lambda: self.onClick("", "", "", "", "", self.idx, 0)).grid(row=0,column=0)
		#an empty label for layout
		self.empty_label = Label(self.rt, text='', width =10).grid(row=2,column=0)

		self.day1 = Label(self.rt, width=10)
		self.day1['text'] = datetime.datetime.now().strftime("%Y-%m-%d")
		self.day1.grid(row=3,column=1)

		currentDay = datetime.datetime.now()
		nextDay = datetime.timedelta(days=1)
		nextDays = currentDay + nextDay

		self.day2 = Label(self.rt, width=10)
		self.day2['text'] = nextDays.strftime("%Y-%m-%d")
		self.day2.grid(row=3,column=2)

		dayThree = datetime.timedelta(days=2)
		twoDays = currentDay + dayThree

		self.day3 = Label(self.rt, width=10)
		self.day3['text'] = twoDays.strftime("%Y-%m-%d")
		self.day3.grid(row=3,column=3)

		self.currentThreeDays[self.day1.cget("text")] = self.day1
		self.currentThreeDays[self.day2.cget("text")] = self.day2
		self.currentThreeDays[self.day3.cget("text")] = self.day3

		#time scale
		self.timeScale = ['00:00 AM', '01:00 AM' , '02:00 AM', '03:00 AM', '04:00 AM', '05:00 AM',
						'06:00 AM', '07:00 AM', '08:00 AM', '09:00 AM', '10:00 AM', '11:00 AM',
						'12:00 PM', '01:00 PM', '02:00 PM', '03:00 PM', '04:00 PM', '05:00 PM',
						'06:00 PM', '07:00 PM', '08:00 PM', '09:00 PM', '10:00 PM', '11:00 PM', '12:00 PM']

		self.master.protocol("WM_DELETE_WINDOW", self.exit)

		self.createTimescale()

	
	def exit(self):
		'''
		When user clicks the upper left corner exit button on the main window,
		a popup appears warning the user to save changes before exiting.

		Either only the popup is closed and program remains open,
		or program closes.

		https://stackoverflow.com/questions/16242782/change-words-on-tkinter-messagebox-buttons

		CP
		'''
		win = Toplevel()
		win.title('warning')
		
		message = "You may lose any unsaved changes"
		Label(win, text=message).pack()

		Button(win, text='Go back to calendar', command=win.destroy).pack()
		Button(win, text='I already saved my changes!', command=self.deleteAll).pack()

	
	def deleteAll(self):
		'''
		
		'''
		self.rt.destroy()

	#### creates timescale slots where events can show up (presumably?)
	# john: "i modified this so the boxes are clickable. is this a layout design
	#		something you guys have settled on? it seems like we're going
	#		need to define start and end times for each time slot. "
	def createTimescale(self):
		'''

		'''
		row = 4
		for c in self.timeScale:
			Label(text=c, relief=RIDGE,width=15, height=2).grid(row=row,column=0, rowspan = 12)
			# creates timeslot slots
			
			dayOneTime = Label(bg= 'white', relief=GROOVE,width=20, height=2)
			dayOneTime.grid(row=row, column=1, rowspan = 12)
			dayOneEvent.append(dayOneTime)

			dayTwoTime = Label(bg= 'grey', relief=GROOVE,width=20, height=2)
			dayTwoTime.grid(row=row,column=2,  rowspan = 12)
			dayTwoEvent.append(dayTwoTime)

			dayThreeTime = Label(bg= 'white', relief=GROOVE,width=20, height=2)
			dayThreeTime.grid(row=row,column=3,  rowspan = 12)
			dayThreeEvent.append(dayThreeTime)
			#### declare timeslot to add to array (begintime, label)
			slot1 = TimeSlot(c, dayOneTime)
			slot2 = TimeSlot(c, dayTwoTime)
			slot3 = TimeSlot(c, dayThreeTime)

			timeSlots.append(slot1)
			timeSlots.append(slot2)
			timeSlots.append(slot3)

			row = row + 12 
			

	#### creates a new window that is a child to the GUI parent frame
	# john: "pretty much copied this from the example"
	def modifyDayBox(self,timeSlot,row,column):
		'''

		'''
		self.top = Toplevel()
		self.top.title("Modify Time Slot")
		self.top.geometry("300x150+30+30")
		self.top.transient(self)
		self.appc=AddEventPopUp(self.top, self.eventSpots, timeSlot,row,column)

	def onClick(self, event_name, start_time, end_time, date, description, idx, exist):
		'''

		'''
		self.top = Toplevel()
		self.top.title("title")
		#self.top.geometry("1200x720")
		self.top.transient(self)
		self.appc = CreateEvent(self, self.top, event_name, start_time, end_time, date, description, idx, exist)


#### class for the pop up when clicking on a time slot in the day-time breakdown
# john: "essentially designed from the example"	
class AddEventPopUp(object):
	'''

	'''
	def __init__(self, master, logicCal, timeSlot,row,column):
		self.master = master
		# create new window
		self.frame = Frame(self.master)

		self.logicCal = logicCal
		self.timeslot = timeSlot # This is not the correct time

		self.AddEvent(row,column)


	def on_closing(self):
		'''

		'''
		result = messagebox.askyesno("Save", "Save the event?")
		if result == True:
			print("worked")
			self.master.destroy()

		
	def close(self):
		self.frame.destroy()
		self.master.destroy()

	# user pressed add event
	def AddEvent(self,row,column):
		'''

		'''
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

		#TODO:  create fields for event info 
		#	add submit button
		#	send submission to calendar
		#	error check
		# 	detailed documentation, passed parameters, etc

	def SubmitAdd(self):
		'''

		'''
		print("submit add")
		self.event_name = self.v.get()
		print(self.event_name)

		rowInt = int(self.row)
		columnInt = int(self.column)

		if columnInt == 1:
			dayOneEvent[rowInt - 4].config(text=self.event_name)
		elif columnInt == 2:
			dayTwoEvent[rowInt - 4].config(text=self.event_name)
		else:
			dayThreeEvent[rowInt - 4].config(text=self.event_name)

		print("placed event")
		eventObject = event(rowInt, day, self.event_name)
		self.logicCal.addEvent(eventObject)
		self.logicCal.printCal()

	#user pressed mod event	(could work identical to add event except modify just replaces previous entry in event list)
	def ModEvent(self):
		'''

		'''
		print("modding event")
		#destroy old layout, retains window
		for widget in self.master.winfo_children():
			widget.destroy()
		#TODO: put in fields for modification
		#	add submit button
		#	send submission to calendar
		#	error check
		# 	detailed documentation, passed parameters, etc

class CreateEvent(object):
	'''

	'''
	def __init__(self, root, master, event_name, start_time, end_time, date, description, idx, exist):
		self.root = root
		self.master = master
		self.frame = Frame(self.master)
		self.event_name = event_name
		self.start_time = start_time
		self.end_time = end_time
		self.date = date
		#
		self.description = description
		# Current index for window
		self.idx = idx
		# 
		self.exist = exist
		self.pickDateOpened = False
		#
		self.count = 6
		# Creates layout of window
		self.widget()

	def widget(self):
		'''

		'''
		# Creating two list of options for drop down menus
		hourChoices = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', \
		'12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
		minuteChoices = ['00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55']
		
		# 'l' stands for label, 'e' stands for entry, 'b' stands for button
		# Creating Labels and Entries for event name and description
		self.l_name = Label(self.master, width = 17, text = "Event name: ")
		self.e_name = Entry(self.master)
		self.l_name.grid(row = 0, column = 0, pady = 20)
		self.e_name.grid(row = 0, column = 1, sticky= W, pady = 20)

		self.l_dscrp = Label(self.master, width = 17, text = "Event description: ")
		self.e_dscrp = Text(self.master, width = 30, height = 6)
		self.l_dscrp.grid(row = 1, column = 0, pady = 20)
		self.e_dscrp.grid(row = 1, column = 1, columnspan = 3, pady = 20, sticky=N+S+W+E)

		# Creating tk variable for drop down menus
		# tkvar stands for tk variable
		# h stands for hour, m stands for minute
		# _from and _to to distinguish start time choosing and end time choosing
		self.tkhvar_from = StringVar(self.master)
		self.tkmvar_from = StringVar(self.master)
		self.tkhvar_from.set('00')
		self.tkmvar_from.set('00')

		self.tkhvar_to = StringVar(self.master)
		self.tkmvar_to = StringVar(self.master)
		self.tkhvar_to.set('00')
		self.tkmvar_to.set('00')

		# Creating Labels, Entries, and drop down menus for choosing time slacks FROM
		self.l_dateFrom = Label(self.master, width = 17, text = "From: ")
		self.dropDown_hour_from = OptionMenu(self.master, self.tkhvar_from, *hourChoices)
		self.l_semicolon1 = Label(self.master, width = 2, text = ":")
		self.dropDown_minute_from = OptionMenu(self.master, self.tkmvar_from, *minuteChoices)
		self.dropDown_hour_from.config(width = 6)
		self.dropDown_minute_from.config(width = 6)
		
		# Adding datePicker button and arranging
		# the button calls the onDatePicker with argument 0, which means the caller is "From"
		self.l_pickDate = Label(self.master, text = "Select date:", width = 15)
		self.l_pickDate.grid(row = 2, column = 1)
		self.b_dateFrom = Button(self.master, text = "DatePicker", command = lambda: self.onDatePicker(0))
		self.b_dateFrom.grid(row = 2, column = 2, padx = 10, pady = 20, sticky = W)

		# Arranging grids
		self.l_dateFrom.grid(row = 3, column = 0, pady = 20)
		self.dropDown_hour_from.grid(row = 3, column = 1, pady = 20, sticky = W)
		self.l_semicolon1.grid(row = 3, column = 1)
		self.dropDown_minute_from.grid(row = 3, column = 1, pady = 20, sticky = E)

		# Creating Labels, Entries, and drop down menus for choosing time slacks TO
		self.l_dateTo = Label(self.master, width = 17, text = "to: ")
		self.dropDown_hour_to = OptionMenu(self.master, self.tkhvar_to, *hourChoices)
		self.l_semicolon2 = Label(self.master, width = 2, text = ":")
		self.dropDown_minute_to = OptionMenu(self.master, self.tkmvar_to, *minuteChoices)
		self.dropDown_hour_to.config(width = 6)
		self.dropDown_minute_to.config(width = 6)

		# Arranging grids
		self.l_dateTo.grid(row = 4, column = 0, pady = 20)
		self.dropDown_hour_to.grid(row = 4, column = 1, pady = 20, sticky = W)
		self.l_semicolon2.grid(row = 4, column = 1)
		self.dropDown_minute_to.grid(row = 4, column = 1, pady = 20, sticky = E)

		# Adding "Submit" and "Delete" buttons
		# submit will call onSubmit, it stores entered event and display it on the main window
		# delete will call clear, it clears all entries
		self.b_sub = Button(self.master, width = 8, text = "submit",command = self.onSubmit)
		self.b_clr = Button(self.master, width = 8, text = "clear", command = self.clear)
		self.b_sub.grid(row = 4, column = 2, pady = 20)
		self.b_clr.grid(row = 4, column = 3, pady = 20)
		
		# EXPLAIN THIS
		if self.exist != 0:
			self.b_rm = Button(self.master, width = 8, text = "Delete this event", \
				command = self.onRemove)
			self.b_rm.grid(row = 5, column = 2, columnspan = 2, sticky = W+E)

		# EXPLAIN THIS
		if self.event_name != "":
			self.e_name.insert(0, "{}".format(self.event_name))
			self.e_dscrp.insert(1.0, "{}".format(self.description))
			self.tkhvar_from.set("{}".format(self.start_time[0]+self.start_time[1]))
			self.tkmvar_from.set("{}".format(self.start_time[2]+self.start_time[3]))
			self.tkhvar_to.set("{}".format(self.end_time[0]+self.end_time[1]))
			self.tkmvar_to.set("{}".format(self.end_time[2]+self.end_time[3]))
			self.l_pickDate["text"] = self.date

		# Creating Error Message 
		self.l_n_error = Label(self.master, text = "Name is empty!", fg = "red")
		self.l_t_error = Label(self.master, text = "Time slack incorrect!", fg = "red")
	

	def clear(self):
		'''
		Resets all entries and drop down menus
		'''
		self.e_name.delete(0, END)
		self.e_dscrp.delete(1.0, END)
		self.l_pickDate['text'] = "Select date:"
		self.tkhvar_from.set('00')
		self.tkmvar_from.set('00')
		self.tkhvar_to.set('00')
		self.tkmvar_to.set('00')

	def cal_time_slack(self):
		'''

		'''
		return int(self.tkhvar_to.get()) * 100 + int(self.tkmvar_to.get())\
		 - int(self.tkhvar_from.get()) * 100 - int(self.tkmvar_from.get())

	# store the event, display it at the right spot
	def onSubmit(self):
		'''
		
		'''
		self.ready_to_submit = True
		time_slack = self.cal_time_slack()
		
		if not self.e_name.get():
			self.l_n_error.grid(row = 0, column = 2, columnspan = 2)
			self.ready_to_submit = False
		else:
			self.l_n_error["text"] = ""

		if time_slack <= 0:
			self.l_t_error.grid(row = 3, column = 2, columnspan = 2)
			self.ready_to_submit = False
		else:
			self.l_t_error["text"] = ""

		if self.l_pickDate.cget("text") == "Select date:":
			self.l_pickDate["fg"] = "red"
			self.ready_to_submit = False
		else:
			self.l_pickDate["fg"] = "black"

		if self.ready_to_submit:
			if self.exist == 1:
				self.root.eventLabelList[self.idx].destroy()
				del self.root.eventLabelList[self.idx]
			
			tempDate = self.l_pickDate.cget("text")
			
			if tempDate in self.root.currentThreeDays:
				colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
				row_num = int(self.root.currentThreeDays[tempDate].grid_info()['row']) + 1
				col_num = int(self.root.currentThreeDays[tempDate].grid_info()['column'])
				start_h = int(self.tkhvar_from.get())
				end_h = int(self.tkhvar_to.get())
				start_m = int(self.tkmvar_from.get())
				end_m = int(self.tkmvar_to.get())
				start_time = self.tkhvar_from.get() + self.tkmvar_from.get()
				end_time = self.tkhvar_to.get() + self.tkmvar_to.get()
				span = (end_h * 60 + end_m - start_h * 60 - start_m) * 12 / 60
				dscrp = self.e_dscrp.get("1.0", END)
				
				self.event = Label(self.root.rt, text = "{}".format(self.e_name.get()), bg = random.choice(colors))
				self.event.grid(row = int(row_num + start_h * 12 + start_m * 12 / 60) , \
					column = col_num, rowspan = int(span), sticky = N+S+W+E)
				self.event.bind("<1>", lambda event : self.root.onClick(self.event.cget("text"), \
					start_time, end_time, tempDate, dscrp, self.idx, 1))
				self.root.eventLabelList.append(self.event)
				print(self.idx, self.root.idx)
				
				if self.exist == 0:
					self.root.idx += 1
				self.master.destroy()

	# remove an event, will add prompt later
	def onRemove(self):
		'''
		Removes an event
		'''
		self.root.eventLabelList[self.idx].destroy()
		del self.root.eventLabelList[self.idx]
		self.master.destroy()

	# pop up the datePicker
	# if there's already a datePicker onpened, close it and pop up a new one
	def onDatePicker(self, fromOrTo):
		'''

		'''
		if self.pickDateOpened == True:
			self.datePicker.destroy()
		self.datePicker = Toplevel()
		if fromOrTo == 0:
			self.child = DatePicker(self.datePicker, self.l_pickDate)
		self.pickDateOpened = True

# DatePicker class is an open-sourced work that was done by Max-Planck-Institut fur Radioastronomie, Bonn, Germany, 2016.
# Our implementation did some modifications.  
class DatePicker:
	'''
	Based on open-sourced work that was done by Max-Planck-Institut fur Radioastronomie, Bonn, Germany, 2016.
	'''
	def __init__(self, parent, p_label):
		self.parent = parent
		self.cal = calendar.TextCalendar(calendar.SUNDAY)
		self.year = datetime.date.today().year
		self.month = datetime.date.today().month
		# EXPLAIN THIS
		self.wid = []
		self.day_selected = 1
		self.month_selected = self.month
		self.year_selected = self.year
		self.day_name = ''
		self.selectedDate = datetime.date.today()
		# EXPLAIN THIS
		self.p_label = p_label
		self.setup(self.year, self.month)

	def clear(self):
		'''

		'''
		for w in self.wid[:]:
			w.grid_forget()
			self.wid.remove(w)

	def go_prev(self):
		'''

		'''
		if self.month > 1:
			self.month -= 1
		else:
			self.month = 12
			self.year -= 1

		self.clear()
		self.setup(self.year, self.month)

	def go_next(self):
		'''

		'''
		if self.month < 12:
			self.month += 1
		else:
			self.month = 1
			self.year += 1
		 
		#self.selected = (self.month, self.year)
		self.clear()
		self.setup(self.year, self.month)

	def selection(self, day, name):
		'''

		'''
		self.day_selected = day
		self.month_selected = self.month
		self.year_selected = self.year

		#data
		self.selectedDate = datetime.date(self.year, self.month, day)
		self.day_name = self.selectedDate.strftime("%A")
		
		self.clear()
		self.setup(self.year, self.month)
		
	def setup(self, y, m):
		'''

		'''
		left = Button(self.parent, text='<', command=self.go_prev)
		self.wid.append(left)
		left.grid(row=0, column=1)
		
		header = Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
		self.wid.append(header)
		header.grid(row=0, column=2, columnspan=3)
		
		right = Button(self.parent, text='>', command=self.go_next)
		self.wid.append(right)
		right.grid(row=0, column=5)
		
		days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
		for num, name in enumerate(days):
			t = Label(self.parent, text=name[:3])
			self.wid.append(t)
			t.grid(row=1, column=num)

		for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
			for d, day in enumerate(week):
				if day:
					b = Button(self.parent, width=1, text=day, command=lambda day=day:self.selection(day, calendar.day_name[(day-1) % 7]))
					self.wid.append(b)
					b.grid(row=w, column=d)
					
		sel = Label(self.parent, height=2, text='{} {} {} {}'.format(
			self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
		self.wid.append(sel)
		sel.grid(row=8, column=0, columnspan=7)

		done = Button(self.parent, text = "Done Choosing", command=self.onDone)
		self.wid.append(done)
		done.grid(row=9, column=0, columnspan=7, pady = 10)

	def onDone(self):
		'''

		'''
		self.p_label['text'] = self.selectedDate
		self.parent.pickDateOpened = False
		self.parent.destroy()

#### main program area
# john: "i changed it to work from root to a master window (so it works easier on windows 10 - i'm selfish)"

master_window = Tk()
gui = GUI(master_window)
master_window.mainloop()
