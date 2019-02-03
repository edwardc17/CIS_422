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
		

class GUI(Frame):
	def __init__(self, rt):
		# this seems like it was required to get windows with data transfer
		# 	working properly - john
		#super(GUI, self).\
		#	__init__(rt)

		Frame.__init__(self, rt)
		self.scrollFrame = ScrollFrame(self)
		self.rt = rt
		rt.title("Calendar")
		self.cal = Calendar("saveFile.dat")
		self.labels = []
		self.currentDays = {}
		self.idx = 0
		self.eventLabelList = []
		self.create_widgets()
		self.scrollFrame.pack(side="top", fill="both", expand=True)
		print(self.winfo_width())

	def create_widgets(self):
		#time scale
		self.timeScale = ['00:00 AM', '01:00 AM' , '02:00 AM', '03:00 AM', '04:00 AM', '05:00 AM',
						'06:00 AM', '07:00 AM', '08:00 AM', '09:00 AM', '10:00 AM', '11:00 AM',
						'12:00 PM', '01:00 PM', '02:00 PM', '03:00 PM', '04:00 PM', '05:00 PM',
						'06:00 PM', '07:00 PM', '08:00 PM', '09:00 PM', '10:00 PM', '11:00 PM']

		self.master.protocol("WM_DELETE_WINDOW", self.exit)
		self.createTimescale()

	def clickEvent(self):
		self.widget.config(background = "green")

	
	def exit(self):
		#https://stackoverflow.com/questions/16242782/change-words-on-tkinter-messagebox-buttons
		win = Toplevel()
		win.title('warning')
		message = "You may lose any unsaved changes"
		Label(win, text=message).pack()
		Button(win, text='Go back to calendar', command=win.destroy).pack()
		
		Button(win, text='I already saved my changes!', command=self.deleteAll).pack()

	def deleteAll(self):
		gc.collect()
		self.scrollFrame.viewPort.destroy()
		self.rt.destroy()

	#### creates timescale slots where events can show up (presumably?)
	# john: "i modified this so the boxes are clickable. is this a layout design
	#		something you guys have settled on? it seems like we're going
	#		need to define start and end times for each time slot. "
	def createTimescale(self):
		r = 0
		for c in self.timeScale:
			Label(self.scrollFrame.viewPort, text=c, relief=RIDGE,width=15, height=2).grid(row=r,column=0, rowspan = 12)
			# creates timeslot slots
			
			dayOneTime = Label(self.scrollFrame.viewPort, bg= 'white', relief=GROOVE,width=20, height=2)
			#dayOneTime.bind("<1>", lambda event, obj=self: onClick(event, obj, dayOneTime))
			dayOneTime.grid(row=r, column=1, rowspan = 12)
			dayOneEvent.append(dayOneTime)

			dayTwoTime = Label(self.scrollFrame.viewPort, bg= 'grey', relief=GROOVE,width=20, height=2)
			#dayTwoTime.bind("<1>", lambda event, obj=self: onClick(event, obj, dayTwoTime))
			dayTwoTime.grid(row=r,column=2,  rowspan = 12)
			dayTwoEvent.append(dayTwoTime)

			dayThreeTime = Label(self.scrollFrame.viewPort, bg= 'white', relief=GROOVE,width=20, height=2)
			#dayThreeTime.bind("<1>", lambda event, obj=self: onClick(event, obj, dayThreeTime))
			dayThreeTime.grid(row=r,column=3,  rowspan = 12)
			dayThreeEvent.append(dayThreeTime)

			dayFourTime = Label(self.scrollFrame.viewPort, bg= 'grey', relief=GROOVE,width=20, height=2)
			#dayThreeTime.bind("<1>", lambda event, obj=self: onClick(event, obj, dayThreeTime))
			dayFourTime.grid(row=r,column=4,  rowspan = 12)

			dayFiveTime = Label(self.scrollFrame.viewPort, bg= 'white', relief=GROOVE,width=20, height=2)
			#dayThreeTime.bind("<1>", lambda event, obj=self: onClick(event, obj, dayThreeTime))
			dayFiveTime.grid(row=r,column=5,  rowspan = 12)
			#### declare timeslot to add to array (begintime, label)
			# (need to input actual date?) yep
			slot1 = TimeSlot(c, dayOneTime)
			slot2 = TimeSlot(c, dayTwoTime)
			slot3 = TimeSlot(c, dayThreeTime)
						#if dayOneTime in timeSlots:
							#timeSlots[dayOneTime].append(slot1))
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
		if exist == 0:
			self.top.title("Adding an Event")
		else:
			self.top.title("Editing Or Removing an Event")
		#self.top.geometry("1200x720")
		#self.top.transient(self.scrollFrame.viewPort)
		self.appc = CreateEvent(self.scrollFrame.viewPort, self, self.top, event_name, start_time, end_time, date, description, idx, exist)

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

		#self.scrollFrame.viewPort = rt
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

#### main program area
# john: "i changed it to work from root to a master window (so it works easier on windows 10 - i'm selfish)"
'''
master_window = Tk()
gui = GUI(master_window)
gui.pack(side="top", fill="both", expand=True)
master_window.mainloop()
'''