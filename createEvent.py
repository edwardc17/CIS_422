import sys
from calendarClasses import *
import datetime
import calendar
import random
if sys.version[0] == '2':
	from Tkinter import *
else:
	from tkinter import *

class CreateEvent(object):
	def __init__(self, canvas, root, master, event_name, start_time, end_time, date, description, idx, exist):
		self.canvas = canvas
		self.root = root
		self.master = master
		self.frame = Frame(self.master)
		self.event_name = event_name
		self.start_time = start_time
		self.end_time = end_time
		self.date = date
		self.description = description
		self.idx = idx
		self.exist = exist
		self.pickDateOpened = False
		self.count = 6
		self.widget()

	def widget(self):
		# Creating two list of options for drop down menus
		hourChoices = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', \
		'12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
		minuteChoices = ['00', '05', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55']
		
		# 'l' stands for label, 'e' stands for entry, 'b' stands for button
		# Creating Labels and Entries for event name and description
		self.l_name = Label(self.master, width = 17, text = "Event name: ")
		self.e_name = Entry(self.master)
		self.l_name.grid(row = 0, column = 0, pady = 20)
		self.e_name.grid(row = 0, column = 1, columnspan = 3, sticky= W, pady = 20)

		self.l_dscrp = Label(self.master, width = 17, text = "Event description: ")
		self.e_dscrp = Text(self.master, width = 30, height = 6)
		self.l_dscrp.grid(row = 1, column = 0, pady = 20)
		self.e_dscrp.grid(row = 1, column = 1, columnspan = 3, pady = 20, sticky=W)

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
		self.l_dateFrom = Label(self.master, width = 17, text = "From: ")
		self.dropDown_hour_from = OptionMenu(self.master, self.tkhvar_from, *hourChoices)
		self.l_semicolon1 = Label(self.master, width = 2, text = ":")
		self.dropDown_minute_from = OptionMenu(self.master, self.tkmvar_from, *minuteChoices)
		self.dropDown_hour_from.config(width = 6)
		self.dropDown_minute_from.config(width = 6)
		
		# Adding datePicker button and arranging
		# the button calls the onDatePicker with argument 0, which means the caller is "From"
		self.l_selectDate = Label(self.master, text = "Select date:", width = 15)
		self.l_selectDate.grid(row = 2, column = 0)
		self.l_pickDate = Label(self.master, text = datetime.datetime.now().strftime("%Y-%m-%d"), width = 15)
		self.l_pickDate.grid(row = 2, column = 1, columnspan = 3)
		self.b_dateFrom = Button(self.master, width = 8, text = "DatePicker", command = lambda: self.onDatePicker(0))
		self.b_dateFrom.grid(row = 2, column = 4, padx = 10, pady = 20, sticky = W)

		# Arranging grids
		self.l_dateFrom.grid(row = 3, column = 0, pady = 20)
		self.dropDown_hour_from.grid(row = 3, column = 1, pady = 20, sticky = E)
		self.l_semicolon1.grid(row = 3, column = 2, sticky = N+S+W+E)
		self.dropDown_minute_from.grid(row = 3, column = 3, pady = 20, sticky = W)

		# Creating Labels, Entries, and drop down menus for choosing time slacks TO
		self.l_dateTo = Label(self.master, width = 17, text = "to: ")
		self.dropDown_hour_to = OptionMenu(self.master, self.tkhvar_to, *hourChoices)
		self.l_semicolon2 = Label(self.master, width = 2, text = ":")
		self.dropDown_minute_to = OptionMenu(self.master, self.tkmvar_to, *minuteChoices)
		self.dropDown_hour_to.config(width = 6)
		self.dropDown_minute_to.config(width = 6)

		# Arraning grids
		self.l_dateTo.grid(row = 4, column = 0, pady = 20)
		self.dropDown_hour_to.grid(row = 4, column = 1, pady = 20, sticky = E)
		self.l_semicolon2.grid(row = 4, column = 2, sticky = N+S+W+E)
		self.dropDown_minute_to.grid(row = 4, column = 3, pady = 20, sticky = W)

		# Adding "Submit" and "Delete" buttons
		# submit will call onSubmit, it stores entered event and display it on the main window
		# delete will call clear, it clears all entries
		self.b_sub = Button(self.master, width = 8, text = "submit",command = self.onSubmit)
		self.b_clr = Button(self.master, width = 8, text = "clear", command = self.clear)
		self.b_sub.grid(row = 4, column = 4, padx = 10)
		self.b_clr.grid(row = 4, column = 5, padx = 10)
		if self.exist != 0:
			self.b_rm = Button(self.master, width = 15, text = "Delete this event", \
				command = self.onRemove)
			self.b_rm.grid(row = 5, column = 4, columnspan = 2, pady = 20)

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
	
	# Reset all the entries, drop down menus
	def clear(self):
		self.e_name.delete(0, END)
		self.e_dscrp.delete(1.0, END)
		self.l_pickDate['text'] = datetime.datetime.now().strftime("%Y-%m-%d")
		self.tkhvar_from.set('12')
		self.tkmvar_from.set('00')
		self.tkhvar_to.set('13')
		self.tkmvar_to.set('00')

	def check_empty(self, event_name):
		for i in event_name:
			if i != ' ':
				return False
		return True


	def cal_time_slack(self):
		return int(self.tkhvar_to.get()) * 100 + int(self.tkmvar_to.get())\
		 - int(self.tkhvar_from.get()) * 100 - int(self.tkmvar_from.get())

	# store the event, display it at the right spot
	def onSubmit(self):
		#self.event = Button(self.root, height = 6, text = "event")
		self.ready_to_submit = True
		time_slack = self.cal_time_slack()
		if not self.e_name.get() or self.check_empty(self.e_name.get()):
			self.l_n_error["text"] = "Name is empty!"
			self.l_n_error.grid(row = 0, column = 3, columnspan = 2)
			self.ready_to_submit = False
		else:
			self.l_n_error["text"] = ""

		if time_slack <= 0:
			self.l_t_error["text"] = "Time slack incorrect!"
			self.l_t_error.grid(row = 3, column = 4, columnspan = 2)
			self.ready_to_submit = False
		else:
			self.l_t_error["text"] = ""

		if self.ready_to_submit:
			if self.exist == 1:
				self.root.eventLabelList[self.idx].destroy()
				del self.root.eventLabelList[self.idx]
			tempDate = self.l_pickDate.cget("text")
			if tempDate in self.root.currentThreeDays:
				colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
				col_num = int(self.root.currentThreeDays[tempDate].grid_info()['column'])
				start_h = int(self.tkhvar_from.get())
				end_h = int(self.tkhvar_to.get())
				start_m = int(self.tkmvar_from.get())
				end_m = int(self.tkmvar_to.get())
				start_time = self.tkhvar_from.get() + self.tkmvar_from.get()
				end_time = self.tkhvar_to.get() + self.tkmvar_to.get()
				span = (end_h * 60 + end_m - start_h * 60 - start_m) * 12 / 60
				dscrp = self.e_dscrp.get("1.0", END)
				self.event = Label(self.canvas, text = "{}".format(self.e_name.get()), bg = random.choice(colors))
				self.event.grid(row = int(start_h * 12 + start_m * 12 / 60) , \
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
		print(self.idx)
		self.root.eventLabelList[self.idx].destroy()
		del self.root.eventLabelList[self.idx]
		self.root.idx -= 1
		self.master.destroy()

	# pop up the datePicker
	# if there's already a datePicker onpened, close it and pop up a new one
	def onDatePicker(self, fromOrTo):
		if self.pickDateOpened == True:
			self.datePicker.destroy()
		self.datePicker = Toplevel()
		if fromOrTo == 0:
			self.child = DatePicker(self.datePicker, self.l_pickDate)
		self.pickDateOpened = True

# DatePicker class is an open-sourced work that was done by Max-Planck-Institut für Radioastronomie, Bonn, Germany, 2016.
# Our implementation did some modifications.  
class DatePicker:
	def __init__(self, parent, p_label):
		self.parent = parent
		self.cal = calendar.TextCalendar(calendar.SUNDAY)
		self.year = datetime.date.today().year
		self.month = datetime.date.today().month
		self.wid = []
		self.day_selected = 1
		self.month_selected = self.month
		self.year_selected = self.year
		self.day_name = ''
		self.selectedDate = datetime.date.today()
		self.p_label = p_label
		self.setup(self.year, self.month)

	def clear(self):
		for w in self.wid[:]:
			w.grid_forget()
			#w.destroy()
			self.wid.remove(w)

	def go_prev(self):
		if self.month > 1:
			self.month -= 1
		else:
			self.month = 12
			self.year -= 1
		#self.selected = (self.month, self.year)
		self.clear()
		self.setup(self.year, self.month)

	def go_next(self):
		if self.month < 12:
			self.month += 1
		else:
			self.month = 1
			self.year += 1
		 
		#self.selected = (self.month, self.year)
		self.clear()
		self.setup(self.year, self.month)

	def selection(self, day, name):
		self.day_selected = day
		self.month_selected = self.month
		self.year_selected = self.year


		#data
		self.selectedDate = datetime.date(self.year, self.month, day)
		self.day_name = self.selectedDate.strftime("%A")
		
		self.clear()
		self.setup(self.year, self.month)
		
	def setup(self, y, m):
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
		sel['text'] = self.selectedDate
		sel.grid(row=8, column=0, columnspan=7)

		done = Button(self.parent, text = "Done Choosing", command=self.onDone)
		self.wid.append(done)
		done.grid(row=9, column=0, columnspan=7, pady = 10)

	def onDone(self):
		self.p_label['text'] = self.selectedDate
		self.p_label['fg'] = "black"
		self.parent.pickDateOpened = False
		self.parent.destroy()