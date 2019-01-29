from tkinter import *
from calendarClasses import *
import datetime

#### click recorder for clicking on labels for time ###
# this was also required in order to wait for clicking
# 	in a box before creating additional windows - john
def onClick(event, guiObj, timeSlot):
	print ("you clicked on", guiObj, "and timeslot ", timeSlot)
	guiObj.modifyDayBox(timeSlot)

def time2():
		#look at createEvent
		dates = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		print(dates)
		#time1 = datetime.datetime.now()
		#label=Label(self.rt,text=time1)

class GUI(Frame, object):
	def __init__(self, rt):
		# this seems like it was required to get windows with data transfer
		# 	working properly - john
		super(GUI, self).\
			__init__(rt)

		self.rt = rt
		rt.title("Calendar")
		self.cal = calendar("saveFile.dat")
		#self.events = self.cal.loadFile()
		self.labels = []
		# array for event spots (so they're clickable)
		self.eventSpots = []

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

		#currentDay = datetime.datetime.now().day
		#currentMonth = datetime.datetime.now().month
		#time1 = datetime.datetime.now().day
		#time1.strftime('%m/%d/%Y')
		##dates = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
		#print(strftime("%B %d %Y, %X %Z",mktime(20,0,0,12,31,98)))
		#print(time1)
		self.day1 = Label(width=10)
		self.day1['text'] = datetime.datetime.now().strftime("%m-%d-%Y")
		print(self.day1['text'])
		self.day1.grid(row=3,column=1)

		currentDay = datetime.datetime.now()
		nextDay = datetime.timedelta(days=1)
		nextDays = currentDay + nextDay
		print(nextDays)

		self.day2 = Label(width=10)
		self.day2['text'] = nextDays.strftime("%m-%d-%Y")
		print(self.day2['text'])
		self.day2.grid(row=3,column=2)


		dayThree = datetime.timedelta(days=2)
		twoDays = currentDay + dayThree


		self.day3 = Label(width=10)
		self.day3['text'] = twoDays.strftime("%m-%d-%Y")
		print(self.day3['text'])
		self.day3.grid(row=3,column=3)

		#time scale
		self.timeScale = ['00:00 AM', '01:00 AM' , '02:00 AM', '03:00 AM', '04:00 AM', '05:00 AM',
						'06:00 AM', '07:00 AM', '08:00 AM', '09:00 AM', '10:00 AM', '11:00 AM',
						'12:00 PM', '01:00 PM', '02:00 PM', '03:00 PM', '04:00 PM', '05:00 PM',
						'06:00 PM', '07:00 PM', '08:00 PM', '09:00 PM', '10:00 PM', '11:00 PM', '12:00 PM']



		self.close_button = Button(rt, text = "Close", command = rt.quit)
		self.close_button.grid(row=29 ,column =4)
		self.createTimescale()

	def clickEvent(self):
		self.widget.config(background = "green")


	def createEvent(self):
		e = event("1pm", "2/1/19", "waffle")
		new = self.cal.addEvent(e)
		self.events = new
		# how to load new data?
		label=Label(self.rt,text=e.getEvent())

		self.labels.append(label)
	
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
			Label(text=c, relief=RIDGE,width=15, height=1).grid(row=r,column=0)
			# creates timeslot slots
			dayOneTime = Label(bg= 'white', relief=GROOVE,width=20, height=1)
			dayOneTime.bind("<1>", lambda event, obj=self: onClick(event, obj, dayOneTime))
			dayOneTime.grid(row=r, column=1)
			dayTwoTime = Label(bg= 'white', relief=GROOVE,width=20, height=1)
			dayTwoTime.bind("<1>", lambda event, obj=self: onClick(event, obj, dayTwoTime))
			dayTwoTime.grid(row=r,column=2)
			dayThreeTime = Label(bg= 'white', relief=GROOVE,width=20, height=1)
			dayThreeTime.bind("<1>", lambda event, obj=self: onClick(event, obj, dayThreeTime))
			dayThreeTime.grid(row=r,column=3)
			r = r + 1

	#### creates a new window that is a child to the GUI parent frame
	# john: "pretty much copied this from the example"
	def modifyDayBox(self, timeSlot):
		self.top = Toplevel()
		self.top.title("Modify Time Slot")
		self.top.geometry("300x150+30+30")
		self.top.transient(self)
		self.appc=ModTimePopUp(self.top, self.eventSpots, timeSlot)

#### class for the pop up when clicking on a time slot in the day-time breakdown
# john: "essentially designed from the example"	
class ModTimePopUp(object):
	def __init__(self, master, eventsList, timeSlot):
		self.master = master
		# create new window
		self.frame = Frame(self.master)
		self.eventsList = eventsList
		self.timeslot = timeSlot # This is not the correct time
		self.widget()

	# define widgets for first window (buttons)
	def widget(self):
		self.b1=Button(self.master, text="Add Event", command=self.AddEvent).grid(row=0, column=0)
		self.b2=Button(self.master, text="Modify Existing Event", command=self.ModEvent).grid(row=1, column=0)

	# user pressed add event
	def AddEvent(self):
		print("adding event")
		#destroy old layout, retains window
		for widget in self.master.winfo_children():
			widget.destroy()
		#self.t1 = Text(self.frame)
		tLabel = Label(self.master, text='Details')
		tLabel.pack()
		self.text = Text(self.master)
		self.text.pack()
		self.submitButton = Button(self.master, text='Submit', command=self.add)
		self.submitButton.pack()

	def add(self):
		# event doesn't appear - don't know how to send it back
		# need time/date
		text = self.text.get('1.0', 'end-1c')
		newEvent = event(self.timeslot, self.timeslot, text)
		print(self.timeslot) # wonky time
		print(text)
		self.eventsList.append(newEvent)
		print(self.eventsList)
		self.master.destroy()
		#TODO:  create fields for event info 
		#	add submit button
		#	send submission to calendar
		#	error check
		# 	detailed documentation, passed parameters, etc

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



#### main program area
# john: "i changed it to work from root to a master window (so it works easier on windows 10 - i'm selfish)"
master_window = Tk()
gui = GUI(master_window)
master_window.mainloop()
