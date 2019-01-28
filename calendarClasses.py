import pickle

class day:
	def __init__(self, date):
		self.date = date
		self.events = []

class event:
	def __init__(self, time, date, text, category=None):
		self.time = time
		self.date = date
		self.text = text
		# For changes in the future
		self.category = category

	def printEvent(self):
		# Not helpful
		print("date: " + self.date + " time: " + self.time + " text: " + self.text)

	def getEvent(self):
		return self.time + " " + self.date + " " + self.text

	def editEventTime(self, time):
		self.time = time

	def editEventDate(self, date):
		self.date = date

	def editEventText(self, text):
		self.text = text

	def getTime(self):
		return self.time

	def getDate(self):
		return self.date

	def getText(self):
		return self.text


class calendar:
	# Will add stuff for categories later here
	def __init__(self, filename):
		self.events = [] # Data for saving
		self.file = filename
	
	def loadFile(self):
		# obj is a list always
		with open(self.file, 'rb') as file:
			obj = pickle.load(file)
			return obj

	def saveFile(self):
		# Any new additions must be appended to the whole data collection.
		# Problematic if data collection becomes very large,
		# but would be working with the collection anyway.
		with open(self.file, 'wb') as file:
			pickle.dump(self.events, file, protocol=2)

	def addEvent(self, event):
		# create event here or just pass it?
		#time, date, text
		#newE = event(time, date, text)
		self.events.append(event)
		self.saveFile() 
		new = self.loadFile()
		return new

	def removeEvent(self, event):
		self.events.remove(event)
		self.saveFile()
		new = self.loadFile()
		return new

	def editEvent(self, event, time=None, date=None, text=None):
		# only add what needs to be changed
		# must add None(s) if adding an arg after time
		if time:
			event.editEventTime(time)
		if date:
			event.editEventDate(date)
		if text:
			event.editEventText(text)
		self.saveFile()
		new = self.loadFile()
		return new

	def printCal(self):
		# Not helpful
		for i in self.events:
			i.printEvent()

	def getEvents(self):
		return self.events

	# put in GUI file
	# dictionary - events per day
	def LoadPage(self):
		# If file isn't empty
		if os.stat(self.file).st_size != 0:
			events = self.loadFile()
			for event in events:
				# add event label/button to calendar
				pass

