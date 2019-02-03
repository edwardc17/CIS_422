import sys
from calendarGui import *
import datetime
import calendar
import random
if sys.version[0] == '2':
    from Tkinter import *
else:
    from tkinter import *

root=Tk()
root.resizable(width=False, height=False)
f1 = Frame()
f2 = GUI(root)
create = Button(f1, text = "Create", width=13,\
	command = lambda: f2.onClick("", "", "", "", "", f2.idx, 0)).grid(row = 0,column=0, padx = 1, pady = 20)

time_region = Label(f1, text = "GMT-08")
time_region.grid(row = 1, column = 0)

def createFiveDays(mainFrame, frame):
	currentDay = datetime.datetime.now()
	for i in range(5):
		dateDelta = datetime.timedelta(days=i)
		tempDate = currentDay + dateDelta
		l_date = Label(mainFrame, width = 20, text = "{}".format(tempDate.strftime("%Y-%m-%d")))
		l_date.grid(row = 1, column = i + 1)
		frame.currentThreeDays[l_date.cget("text")] = l_date

createFiveDays(f1, f2)
f1.grid(row = 0, column = 0, padx = 10, sticky=W)
f2.grid(row = 1, column = 0, sticky = N+S+W+E)

root.mainloop()