import calendar
import datetime
import sys

if sys.version[0] == '2':
	from Tkinter import *
else:
	from tkinter import *

#from tkinter import *

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
		self.appc = Demo(self, self.top, self.t1)

class Demo(object):
	def __init__(self, root, master, t1):
		self.root = root
		self.master = master
		self.frame = Frame(self.master)
		self.t1 = t1
		self.pickDateOpened = False
		self.count = 6
		self.widget()

	def widget(self):
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
		
		# Arranging grids
		self.l_dateFrom.grid(row = 2, column = 0, pady = 20)
		self.dropDown_hour_from.grid(row = 2, column = 1, pady = 20, sticky = W)
		self.l_semicolon1.grid(row = 2, column = 1)
		self.dropDown_minute_from.grid(row = 2, column = 1, pady = 20, sticky = E)

		# Adding datePicker button and arranging
		# the button calls the onDatePicker with argument 0, which means the caller is "From"
		self.l_pickDate_from = Label(self.master, text = "Select date:", width = 15)
		self.l_pickDate_from.grid(row = 2, column = 2)
		self.b_dateFrom = Button(self.master, text = "DatePicker", command = lambda: self.onDatePicker(0))
		self.b_dateFrom.grid(row = 2, column = 3, pady = 20, sticky = W)

		# Creating Labels, Entries, and drop down menus for choosing time slacks TO
		self.l_dateTo = Label(self.master, width = 17, text = "to: ")
		self.l_dateTo.grid(row = 3, column = 0, pady = 20)
		self.dropDown_hour_to = OptionMenu(self.master, self.tkhvar_to, *hourChoices)
		self.l_semicolon2 = Label(self.master, width = 2, text = ":")
		self.dropDown_minute_to = OptionMenu(self.master, self.tkmvar_to, *minuteChoices)
		self.dropDown_hour_to.config(width = 6)
		self.dropDown_minute_to.config(width = 6)

		# Arraning grids
		self.l_dateTo.grid(row = 3, column = 0, pady = 20)
		self.dropDown_hour_to.grid(row = 3, column = 1, pady = 20, sticky = W)
		self.l_semicolon2.grid(row = 3, column = 1)
		self.dropDown_minute_to.grid(row = 3, column = 1, pady = 20, sticky = E)

		# Adding datePicker button and arranging
		# the button calls the onDatePicker with argument 1, which means the caller is "to"
		self.l_pickDate_to = Label(self.master, text = "Select date:", width = 15)
		self.l_pickDate_to.grid(row = 3, column = 2)
		self.b_dateTo = Button(self.master, text = "DatePicker", command = lambda: self.onDatePicker(1))
		self.b_dateTo.grid(row = 3, column = 3, pady = 20)

		# Adding "Submit" and "Delete" buttons
		# submit will call onSubmit, it stores entered event and display it on the main window
		# delete will call clear, it clears all entries
		self.b_sub = Button(self.master, text = "submit",command = self.onSubmit)
		self.b_del = Button(self.master, text = "delete", command = self.clear)
		self.b_sub.grid(row = 4, column = 2, pady = 20)
		self.b_del.grid(row = 4, column = 3, pady = 20)
	
	# Reset all the entries, drop down menus
	def clear(self):
		self.e_name.delete(0, END)
		self.e_dscrp.delete(1.0, END)
		self.l_pickDate_from['text'] = "Select date:"
		self.l_pickDate_to['text'] = "Select date:"
		self.tkhvar_from.set('00')
		self.tkmvar_from.set('00')
		self.tkhvar_from.set('00')
		self.tkmvar_from.set('00')

	# store the event, display it at the right spot
	def onSubmit(self):
		self.event = Button(self.root, height = 6, text = "event")
		self.event.grid(row = self.count * 6, column = 1, rowspan = 6)
		self.count += 1

	# pop up the datePicker
	# if there's already a datePicker onpened, close it and pop up a new one
	def onDatePicker(self, fromOrTo):
		if self.pickDateOpened == True:
			self.datePicker.destroy()
		self.datePicker = Toplevel()
		if fromOrTo == 0:
			self.child = DatePicker(self.datePicker, self.l_pickDate_from)
		else:
			self.child = DatePicker(self.datePicker, self.l_pickDate_to)
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
		sel.grid(row=8, column=0, columnspan=7)

		done = Button(self.parent, text = "Done Choosing", command=self.onDone)
		self.wid.append(done)
		done.grid(row=9, column=0, columnspan=7, pady = 10)

	def onDone(self):
		self.p_label['text'] = self.selectedDate
		self.parent.pickDateOpened = False
		self.parent.destroy()

root=Tk()
app=Application(root)
app.mainloop()