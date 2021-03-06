'''
Author(s): Jiazhen Cao(JC), Anna Saltveit(AS), John Nemeth(JN)
Update date:  Feburary 5, 2019

DatePicker class is an open-sourced work 
that was done by Max-Planck-Institut fur Radioastronomie, Bonn, Germany, 2016.

All other code is made by the team - individual work marked in methods and classes.
'''

import sys
from calendarClasses import *
from tkinter.colorchooser import *
import datetime
import calendar
if sys.version[0] == '2':
	from Tkinter import *
else:
	from tkinter import *

class CreateEvent(object):
	'''
	Create event popup window.

	AS - binding functions to labels
	JC - everything else
	'''
	def __init__(self, canvas, root, master, eventObject, date, idx, exist):
		# Scroll frame
		self.canvas = canvas
		# Calendar GUI
		self.root = root
		# Top level
		self.master = master
		# Window
		self.frame = Frame(self.master)
		self.eventObj = eventObject					# reference event object
		self.event_name = eventObject.name 			# reference event name
		self.start_time = eventObject.start_time 	# reference event start_time
		self.end_time = eventObject.end_time 		# reference event end_time
		self.category = eventObject.category 		# reference event category
		self.color = eventObject.color 				# reference event color
		self.description = eventObject.desc 		# reference event description
		self.date = date 							# reference event date
		# Index for placement
		self.idx = idx
		# To check whether user is accessing "Create" button (0) or event label (>0)
		self.exist = exist
		# Whether a date picker window is open
		self.pickDateOpened = False
		# Create layout of popup window
		self.widget()

	def widget(self):
		'''
		Creates layout - buttons, labels, dropdown menus for popup window.
		'''
		# Creating two list of options for drop down menus
		hourChoices = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', \
		'12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
		minuteChoices = ['00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55']
		
		# 'l' stands for label, 'e' stands for entry, 'b' stands for button
		# Creating Label and Entry for event name
		self.l_name = Label(self.master, width = 17, text = "Event name: ")
		self.e_name = Entry(self.master)
		self.l_name.grid(row = 0, column = 0, pady = 20)
		self.e_name.grid(row = 0, column = 1, columnspan = 3, pady = 20, sticky = W)
		# Creating Label and Entry for event category
		self.l_category = Label(self.master, width = 17, text = "Event category: ")
		self.e_category = Entry(self.master)
		self.l_category.grid(row = 1, column = 0, pady = 20)
		self.e_category.grid(row = 1, column = 1, columnspan = 3, pady = 20, sticky =W)
		# Creating button for choosing event color
		self.b_color = Button(self.master, width = 9, text = "Event Color", bg = "#33A1C9", \
			command = self.setColor)
		self.b_color.grid(row = 1, column = 4, pady = 20)
		# Creating Label and Entry for event description
		self.l_desc = Label(self.master, width = 17, text = "Event description: ")
		self.e_desc = Text(self.master, width = 30, height = 6)
		self.l_desc.grid(row = 2, column = 0, pady = 20)
		self.e_desc.grid(row = 2, column = 1, columnspan = 3, pady = 20, sticky = W)
		
		# Creating tk variable for drop down menus
		# tkvar stands for tk variable
		# h stands for hour, m stands for minute
		# _from and _to to distinguish start time choosing and end time choosing
		self.tkhvar_from = StringVar(self.master)
		self.tkmvar_from = StringVar(self.master)
		self.tkhvar_from.set('12')
		self.tkmvar_from.set('00')

		self.tkhvar_to = StringVar(self.master)
		self.tkmvar_to = StringVar(self.master)
		self.tkhvar_to.set('13')
		self.tkmvar_to.set('00')

		# Creating Labels, Entries, and drop down menus for choosing time slacks FROM
		# 'l' stands for label
		self.l_dateFrom = Label(self.master, width = 17, text = "From: ")
		self.dropDown_hour_from = OptionMenu(self.master, self.tkhvar_from, *hourChoices)
		self.l_semicolon1 = Label(self.master, width = 2, text = ":")
		self.dropDown_minute_from = OptionMenu(self.master, self.tkmvar_from, *minuteChoices)
		self.dropDown_hour_from.config(width = 6)
		self.dropDown_minute_from.config(width = 6)
		
		# Adding datePicker button and labels for instruction, and arranging
		# the button calls the onDatePicker with argument 0, which means the caller is "From"
		# 'l' stands for label, 'b' stands for button
		self.l_selectDate = Label(self.master, text = "Select date:", width = 15)
		self.l_selectDate.grid(row = 3, column = 0)
		self.l_pickDate = Label(self.master, text = datetime.datetime.now()\
			.strftime("%Y-%m-%d"), width = 15)
		self.l_pickDate.grid(row = 3, column = 1, columnspan = 3)
		self.b_dateFrom = Button(self.master, width = 8, text = "DatePicker", \
			command = lambda: self.onDatePicker())
		self.b_dateFrom.grid(row = 3, column = 4, padx = 10, pady = 20, sticky = W)

		# Arranging widgets
		# 'l' stands for label
		self.l_dateFrom.grid(row = 4, column = 0, pady = 20)
		self.dropDown_hour_from.grid(row = 4, column = 1, pady = 20, sticky = E)
		self.l_semicolon1.grid(row = 4, column = 2, sticky = N+S+W+E)
		self.dropDown_minute_from.grid(row = 4, column = 3, pady = 20, sticky = W)

		# Creating Labels, Entries, and drop down menus for choosing time slacks TO
		# 'l' stands for label
		self.l_dateTo = Label(self.master, width = 17, text = "to: ")
		self.dropDown_hour_to = OptionMenu(self.master, self.tkhvar_to, *hourChoices)
		self.l_semicolon2 = Label(self.master, width = 2, text = ":")
		self.dropDown_minute_to = OptionMenu(self.master, self.tkmvar_to, *minuteChoices)
		self.dropDown_hour_to.config(width = 6)
		self.dropDown_minute_to.config(width = 6)

		# Arraning widgets
		# 'l' stands for label
		self.l_dateTo.grid(row = 5, column = 0, pady = 20)
		self.dropDown_hour_to.grid(row = 5, column = 1, pady = 20, sticky = E)
		self.l_semicolon2.grid(row = 5, column = 2, sticky = N+S+W+E)
		self.dropDown_minute_to.grid(row = 5, column = 3, pady = 20, sticky = W)

		# Adding "Submit" and "Delete" buttons
		# Submit will call onSubmit, it stores entered event and displays it on the main window
		# Delete will call clear, it clears all entries
		# 'b' stands for button
		self.b_sub = Button(self.master, width = 8, text = "submit",command = self.onSubmit) # Submit button
		self.b_clr = Button(self.master, width = 8, text = "clear", command = self.clear) # Clear button
		self.b_sub.grid(row = 5, column = 4, padx = 10)
		self.b_clr.grid(row = 5, column = 5, padx = 10)
		if self.exist != 0:
			# User didn't click "create event" button
			self.b_rm = Button(self.master, width = 15, text = "Delete this event", \
				command = self.onRemove) # Remove button
			self.b_rm.grid(row = 6, column = 4, columnspan = 2, pady = 20)

		if self.event_name != "":
			# Set labels to their given values
			# 'e' stands for entry, 'b' stands for button
			self.e_name.insert(0, "{}".format(self.event_name))
			self.e_category.insert(0, "{}".format(self.category))
			self.b_color["bg"] = self.color
			self.e_desc.insert(1.0, "{}".format(self.description))
			# tk hour from variable
			self.tkhvar_from.set("{}".format(self.start_time[0]+self.start_time[1]))
			# tk minute from variable
			self.tkmvar_from.set("{}".format(self.start_time[2]+self.start_time[3]))
			# tk hour to variable
			self.tkhvar_to.set("{}".format(self.end_time[0]+self.end_time[1]))
			# tk minute to variable
			self.tkmvar_to.set("{}".format(self.end_time[2]+self.end_time[3]))
			self.l_pickDate["text"] = self.date

		# Creating Error Message 
		# 'l' stands for label
		self.l_name_error = Label(self.master, text = "Name is empty!", fg = "red") # Name error label
		self.l_time_error = Label(self.master, text = "Time slack incorrect!", fg = "red") # Time error label
	
	def clear(self):
		'''
		Resets all entries and drop down menus.
		'''
		# 'l' stands for label, 'b' stands for button, 'e' stands for event
		self.e_name.delete(0, END)
		self.e_category.delete(0, END)
		self.e_desc.delete(1.0, END)
		self.b_color["text"] = "Event Color"
		self.b_color["bg"] = "#33A1C9"
		self.l_pickDate['text'] = datetime.datetime.now().strftime("%Y-%m-%d")
		# Reset start and end time menu defaults
		self.tkhvar_from.set('12')
		self.tkmvar_from.set('00')
		self.tkhvar_to.set('13')
		self.tkmvar_to.set('00')

	def setColor(self):
		'''
		Sets event color chosen by user.
		'''
		color = askcolor()[1] # Get color choice from user
		self.b_color["bg"] = color # Set the color

	def check_empty(self, event_name):
		'''
		Checks if fields in event are empty.
		'''
		for i in event_name:
			if i != ' ':
				return False
		return True

	def cal_time_slice(self):
		'''
		Check if the start time is after the end time.
		'''
		return int(self.tkhvar_to.get()) * 100 + int(self.tkmvar_to.get())\
		 - int(self.tkhvar_from.get()) * 100 - int(self.tkmvar_from.get())

	def checkTimeConflict(self):
		'''
		Compares starting and ending times of every event in a day
		to check for overlapping.
		'''
		# 'h' stands for hour, 'm' stands for minute, 'e' stands for event
		date = self.l_pickDate["text"]
		if date in self.root.cal.events: 						# check if the day exist in dict
			eventList = self.root.cal.events[date] 				# assign the events to a list
			# Current event's times
			start_h = int(self.tkhvar_from.get())
			end_h = int(self.tkhvar_to.get())
			start_m = int(self.tkmvar_from.get())
			end_m = int(self.tkmvar_to.get())
			start_time = start_h * 100 + start_m
			end_time = end_h * 100 + end_m
			for event in eventList: 							# iterating the event list
				# Other event to compare
				e_start_time = int(event.start_time)
				e_end_time = int(event.end_time)
				if event == self.eventObj: 						# if event exist, upon just editing, continue
					continue 									# don't need check if time doesn't change
				# There's a conflict
				if e_start_time <= start_time < e_end_time or \
					e_start_time < end_time <= e_end_time:
					# Create popup window
					window = Toplevel()
					# Warning text
					window.title('Time Conflicts')
					message1 = "Time conflicts with existing events."
					message2 = "Please change the time slice."
					Label(window, text=message1).pack()
					Label(window, text=message2).pack()
					# Destroys current popup window, returns to main window
					Button(window, text='OK', command=window.destroy).pack()
					return False
		
		return True


	def onSubmit(self):
		'''
		Store event and display it at the correct spot.
		'''
		# Assign a boolean to check if a event is eligble for submit and save
		self.ready_to_submit = True
		# assign the time slice to time_slice
		time_slice = self.cal_time_slice()
		# No name given for event
		if not self.e_name.get() or self.check_empty(self.e_name.get()):
			self.l_name_error["text"] = "Name is empty!"
			self.l_name_error.grid(row = 0, column = 3, columnspan = 2)
			self.ready_to_submit = False
		else:
			self.l_name_error["text"] = ""
		
		# Start time is after end time
		if time_slice <= 0:
			self.l_time_error["text"] = "Time slack incorrect!"
			self.l_time_error.grid(row = 3, column = 4, columnspan = 2)
			self.ready_to_submit = False
		else:
			self.l_time_error["text"] = ""

		# Check if there's time confliction
		if self.checkTimeConflict() == False:
			self.ready_to_submit = False

		# New event being created
		if self.exist == 0:
			# There's a conflict
			if self.checkTimeConflict() == False:
				self.ready_to_submit = False

		# All fields are correct input, able to create event
		if self.ready_to_submit:
			# Popup created by clicking on event label
			if self.exist == 1:
				# Delete current event label
				# Delete the object that stored in the calendar class and save
				self.root.eventLabels[self.idx].destroy()
				self.root.eventLabels.pop(self.idx, None)
				self.root.cal.removeEvent(self.eventObj, self.date)
			tempDate = self.l_pickDate.cget("text")
			# Collect all data given into variables
			# 'h' stands for hour, 'm' stands for minute
			start_h = int(self.tkhvar_from.get()) 							# get start hour in int 
			end_h = int(self.tkhvar_to.get()) 								# get end hour in int
			start_m = int(self.tkmvar_from.get()) 							# get start minute in int
			end_m = int(self.tkmvar_to.get()) 								# get end hour in int
			start_time = self.tkhvar_from.get() + self.tkmvar_from.get() 	# concat start_h and start_m
			end_time = self.tkhvar_to.get() + self.tkmvar_to.get() 			# concat end_h and end_m
			name = self.e_name.get() 										# assign name entry text to name
			category = self.e_category.get() 								# assign category
			color = self.b_color["bg"] 										# assign color
			desc = self.e_desc.get("1.0", END) 								# assign description
			# Create event for saving
			eventObj = EventObj(start_time, end_time, name, desc, category, color, self.idx)
			# Chosen date is currently shown on main screen
			if tempDate in self.root.currentDays:
				# Add event label to that day
				self.createLabels(start_h, end_h, start_m, end_m, tempDate, name, eventObj)	
			# Add event to Calendar for saving
			self.root.cal.addEvent(eventObj, tempDate)
			# Destroy popup window
			self.master.destroy()

	def createLabels(self, start_h, end_h, start_m, end_m, tempDate, name, eventObj):
		'''
		Create an event label for a day currently shown on main window
		AS - event label borders
		JN - binds labels
		'''
		col_num = int(self.root.currentDays[tempDate].grid_info()['column']) # Column number
		# How much time/space the label should use.
		span = (end_h * 60 + end_m - start_h * 60 - start_m) * 12 / 60 
		# Event label with text and color
		self.event = Label(self.canvas, text = "{}".format(name), \
			bg = eventObj.color, borderwidth=2, relief="solid")
		# Place it in day on main window
		self.event.grid(row = int(start_h * 12 + start_m * 12 / 60) , \
			column = col_num, rowspan = int(span), sticky = N+S+W+E)
		self.event.bind("<1>", lambda event : self.root.onClick(eventObj, \
			tempDate, self.idx, 1))
		# Save label in eventLabels by index
		self.root.eventLabels[self.idx] = self.event
		# Event made from "Create" button
		if self.exist == 0:
			# Increase index for placing in list next time
			self.root.idx += 1

	def onRemove(self):
		'''
		Removes an event from window. Prompt will be added later.
		'''
		# Remove event from saved file
		self.root.cal.removeEvent(self.eventObj, self.date)
		# Destroy event label
		self.root.eventLabels[self.idx].destroy()
		# Remove index from list and decrease index
		self.root.eventLabels.pop(self.idx, None)
		self.root.idx -= 1
		self.master.destroy()

	def onDatePicker(self):
		'''
		Open datePicker popup window. 
		If there's already a datePicker onpened, close it and pop up a new one.
		'''
		# Destroy currently open date picker window
		if self.pickDateOpened == True:
			self.datePicker.destroy()
		self.datePicker = Toplevel()
		# DatePicker is open
		self.child = DatePicker(self.datePicker, self.l_pickDate)
		self.pickDateOpened = True


class DatePicker:
	'''
	DatePicker class is an open-sourced work 
	that was done by Max-Planck-Institut fur Radioastronomie, Bonn, Germany, 2016.
	Our implementation did some modifications. WHICH MODIFICATIONS
	'''
	def __init__(self, parent, p_label):
		self.parent = parent								# reference parent
		self.cal = calendar.TextCalendar(calendar.SUNDAY) 	# reference cal
		self.year = datetime.date.today().year 				# reference year
		self.month = datetime.date.today().month 			# reference month
		self.wid = [] 										# reference a empty widget list
		self.day_selected = 1								# reference initial day_selected to 1
		self.month_selected = self.month 					# reference month_selected
		self.year_selected = self.year 						# reference year_selected
		self.day_name = '' 									# reference day_name to emptry str
		self.selectedDate = datetime.date.today() 			# reference selectedDate to the current day
		self.p_label = p_label 								# reference p_label to l_pickDate from the parent
		self.setup(self.year, self.month)					# call the setup()

	def clear(self):
		'''
		clear function that remove all the widgets
		'''
		for w in self.wid[:]:
			w.grid_forget()
			self.wid.remove(w)

	def go_prev(self):
		'''
		Update the month and year to previous upon < button clicked
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
		Update the month and year to next upon > button clicked
		'''
		if self.month < 12:
			self.month += 1
		else:
			# Reset to January
			self.month = 1
			self.year += 1
		 
		self.clear()
		self.setup(self.year, self.month)

	def selection(self, day, name):
		'''
		Stores selected day, month, year.
		'''
		self.day_selected = day
		self.month_selected = self.month
		self.year_selected = self.year

		# selectDate get the Date selected in numerical format
		# day_name get the selected date in word
		self.selectedDate = datetime.date(self.year, self.month, day)
		self.day_name = self.selectedDate.strftime("%A")
		
		self.clear()
		self.setup(self.year, self.month)
		
	def setup(self, y, m):
		'''
		set up the DatePicker Layout
		'''
		# create a < button for previous month
		left = Button(self.parent, text='<', command=self.go_prev)
		self.wid.append(left)
		left.grid(row=0, column=1)
		
		# create middle for displaying the month
		header = Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
		self.wid.append(header)
		header.grid(row=0, column=2, columnspan=3)
		
		# create a > button for next month
		right = Button(self.parent, text='>', command=self.go_next)
		self.wid.append(right)
		right.grid(row=0, column=5)
		
		# create labels displaying days
		days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
		for num, name in enumerate(days):
			t = Label(self.parent, text=name[:3])
			self.wid.append(t)
			t.grid(row=1, column=num)
		
		# create buttons for day selecting and set up their layout
		for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
			for d, day in enumerate(week):
				if day:
					b = Button(self.parent, width=1, text=day, command =lambda day = \
						day:self.selection(day, calendar.day_name[(day-1) % 7]))
					self.wid.append(b)
					b.grid(row=w, column=d)
		
		# create a label at the very buttom that display the chosen date
		sel = Label(self.parent, height=2, text='{} {} {} {}'.format(
			self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
		self.wid.append(sel)
		sel['text'] = self.selectedDate
		sel.grid(row=8, column=0, columnspan=7)

		# create a button that calls onDonw function
		done = Button(self.parent, text = "Done Choosing", command=self.onDone)
		self.wid.append(done)
		done.grid(row=9, column=0, columnspan=7, pady = 10)

	def onDone(self):
		'''
		The function change the text of the label 'l_pickDate' on the event window.
		'''
		self.p_label['text'] = self.selectedDate
		self.p_label['fg'] = "black"
		# set pickDateOpened to False and destroy the child datePicker window.
		self.parent.pickDateOpened = False
		self.parent.destroy()