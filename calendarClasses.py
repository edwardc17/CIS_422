import pickle

''' Get rid of?
class day:
	def __init__(self, date):
		self.date = date
		self.events = []
'''
class event:
	'''

	'''
	def __init__(self, time, date, title, text, row, column):
		self.time = time
		self.date = date
		self.title = title
		self.text = text
		self.row = row
		self.column = column

	def printEvent(self):
		print("date: " + self.date + " time: " + self.time + " text: " + self.text)

	def getEvent(self):
		return self.time + " " + self.date + " " + self.title + " " + self.text

	def editEventTime(self, time):
		self.time = time

	def editEventDate(self, date):
		self.date = date

	def editEventText(self, text):
		self.text = text

	def editEventTitle(self, title):
		self.title = title

	def getTime(self):
		return self.time

	def getDate(self):
		return self.date

	def getTitle(self):
		return self.title

	def getText(self):
		return self.text

	def getRow(self):
		return self.row

	def getColumn(self):
		return self.column


class Calendar:
	# Will add stuff for categories later here
	def __init__(self, filename):
		self.events = {} # Data for saving, by day
		self.file = filename
	
	def loadFile(self):
		'''

		'''
		# obj is a list always
		with open(self.file, 'rb') as file:
			obj = pickle.load(file)
			return obj

	def saveFile(self):
		'''

		'''
		# Any new additions must be appended to the whole data collection.
		# Problematic if data collection becomes very large,
		# but would be working with the collection anyway.
		with open(self.file, 'wb') as file:
			pickle.dump(self.events, file, protocol=2)

	def addEvent(self, event, day):
		'''

		'''
		# create event here or just pass it?
		#time, date, text
		#newE = event(time, date, text)
		if day in self.events:
			self.events[day].append(event)
		else:
			self.events[day] = [event]
		#self.events.append(event)
		self.saveFile() 
		#new = self.loadFile()
		#return new

	def removeEvent(self, event, day):
		'''

		'''
		self.events[day].remove(event)
		#self.events.remove(event)
		self.saveFile()
		new = self.loadFile()
		return new

	# ignore for now
	def editEvent(self, event, time=None, date=None, title=None, text=None):
		'''

		'''
		# only add what needs to be changed
		# must add None(s) if adding an arg an unavailable arg
		if time:
			event.editEventTime(time)
		if date:
			event.editEventDate(date)
		if title:
			event.editEventTitle(title)
		if text:
			event.editEventText(text)
		
		self.saveFile()
		new = self.loadFile()
		return new

	def printCal(self):
		'''

		'''
		# Not helpful
		for day in self.events:
			for e in self.events[day]:
				e.printEvent()

	def getEvents(self):
		return self.events
