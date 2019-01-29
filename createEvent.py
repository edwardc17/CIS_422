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
		self.top.geometry("1600x720+%d+%d" %( ( (root.winfo_screenwidth() / 2.) - (350 / 2.) ), ( (root.winfo_screenheight() / 2.) - (150 / 2.) ) ) )
		self.top.transient(self)
		self.appc = Demo(self.top, self.t1)

class Demo(object):
	def __init__(self, master, t1):
		self.master = master
		self.frame = Frame(self.master)
		self.t1 = t1
		self.widget()

	def widget(self):
		self.lname = Label(self.master, width = 30, text = "Event name: ")
		self.ename = Entry(self.master)
		self.ldscrp = Label(self.master, text = "Event description: ")
		self.edscrp = Text(self.master, width = 30, height = 6)
		self.lfrom = Label(self.master, text = "From: ")
		self.efrom = Entry(self.master)
		self.lto = Label(self.master, text = "to: ")
		self.eto = Entry(self.master)

		self.lname.grid(row = 1, column = 1, pady = 20)
		self.ename.grid(row = 1, column = 2, sticky=W, pady = 20)
		self.ldscrp.grid(row = 2, column = 1, pady = 20)
		self.edscrp.grid(row = 2, column = 2, sticky=W, pady = 20)
		self.lfrom.grid(row = 3, column = 1, pady = 20)
		self.efrom.grid(row = 3, column = 2, sticky=W, pady = 20)
		self.lto.grid(row = 3, column = 3, pady = 20)
		self.eto.grid(row = 3, column = 4, sticky=W, pady = 20)

		self.bsub = Button(self.master, text = "submit",command = self.onSubmit)
		self.bdel = Button(self.master, text = "delete", command = self.clear)
		self.bsub.grid(row = 4, column = 3)
		self.bdel.grid(row = 4, column = 4)
	def clear(self):
		pass

	def onSubmit(self):
		self.t1.insert(INSERT, self.ename.get())
        
'''
class DatePicker:
    def __init__(self, parent):
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
        left = tk.Button(self.parent, text='<', command=self.go_prev)
        self.wid.append(left)
        left.grid(row=0, column=1)
         
        header = tk.Label(self.parent, height=2, text='{}   {}'.format(calendar.month_abbr[m], str(y)))
        self.wid.append(header)
        header.grid(row=0, column=2, columnspan=3)
         
        right = tk.Button(self.parent, text='>', command=self.go_next)
        self.wid.append(right)
        right.grid(row=0, column=5)
         
        days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        for num, name in enumerate(days):
            t = tk.Label(self.parent, text=name[:3])
            self.wid.append(t)
            t.grid(row=1, column=num)
         
        for w, week in enumerate(self.cal.monthdayscalendar(y, m), 2):
            for d, day in enumerate(week):
                if day:
                    b = tk.Button(self.parent, width=1, text=day, command=lambda day=day:self.selection(day, calendar.day_name[(day-1) % 7]))
                    self.wid.append(b)
                    b.grid(row=w, column=d)
                     
        sel = tk.Label(self.parent, height=2, text='{} {} {} {}'.format(
            self.day_name, calendar.month_name[self.month_selected], self.day_selected, self.year_selected))
        self.wid.append(sel)
        sel.grid(row=8, column=0, columnspan=7)
'''
root=Tk()
app=Application(root)
app.mainloop()