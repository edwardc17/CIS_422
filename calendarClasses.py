import pickle

class event:
	def __init__(self, time, date, text):
		self.time = time
		self.date = date
		self.text = text

	def printEvent(self):
		print("date: " + self.date + " time: " + self.time + " text: " + self.text)

	def editEventTime(self, time):
		self.time = time

	def editEventDate(self, date):
		self.date = date

	def editEventText(self, text):
		self.text = text

class calendar:
	def __init__(self, filename):
		self.events = [] # Data for saving
		self.file = filename
	
	def loadFile(self):
		# obj is a list
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

	def removeEvent(self, event):
		self.events.remove(event)
		self.saveFile()

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

	def printCal():
		for i in self.events:
			i.printEvent()