from Tkinter import *
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
		self.top.geometry("300x150+30+30")
		self.top.transient(self)
		self.appc=Demo(self.top, self.t1)

class Demo(object):
	def __init__(self, master, t1):
		self.master = master
		self.frame = Frame(self.master)
		self.t1 = t1
		self.widget()

	def widget(self):
		self.e1=Entry(self.master)
		self.e1.grid(row=1,column=1)
		self.b1=Button(self.master,text="submit",command=self.onSubmit)
		self.b1.grid(row=2,column=1)

	def onSubmit(self):
		self.t1.insert(INSERT, self.e1.get())


root=Tk()
app=Application(root)
app.mainloop()