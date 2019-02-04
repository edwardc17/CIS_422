import pickle


class event:
	'''
	Stores events in a file to use between program uses.
	AS
	'''
	def __init__(self, start_time, end_time, name, desc, category, color, index):
		self.start_time = start_time
		self.end_time = end_time
		self.name = name
		self.desc = desc
		self.category = category
		self.color = color
		self.index = index


	# Edit individual values
	def editEventStartTime(self, start_time):
		self.start_time = start_time

	def editEventEndTime(self, end_time):
		self.end_time = end_time

	def editEventDesc(self, desc):
		self.desc = desc

	def editEventTitle(self, name):
		self.name = name

	def editEventCategory(self, category):
		self.category = category

	def editEventColor(self, color):
		self.color = color

	def getEventIndex(self, index):
		self.index = index

	# Get individual values
	def getStartTime(self):
		return self.start_time

	def getEndTime(self):
		return self.end_time

	def getName(self):
		return self.name

	def getDesc(self):
		return self.desc

	def getCategory(self):
		return self.category

	def getColor(self):
		return self.color

	def getIndex(self):
		return self.index


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
		self.saveFile()
		new = self.loadFile()
		return new

	def editEvent(self, event, start_time=None, end_time=None, name=None, desc=None, category=None, color=None):
		'''
		Must add None(s) up to the last argument you want to use.

		'''
		# only add what needs to be changed
		# must add None(s) if adding an arg past an unavailable arg
		if start_time:
			event.editEventTime(start_time)
		if end_time:
			event.editEventDate(end_time)
		if name:
			event.editEventName(name)
		if desc:
			event.editEventDesc(desc)
		if category:
			event.editEventCategory(category)
		if color:
			event.editEventColor(color)
		if index:
			event.editEventIndex(index)

		
		self.saveFile()
		new = self.loadFile()
		return new

	def printCal(self):
		'''
		For testing.
		'''
		for day in self.events:
			for e in self.events[day]:
				e.printEvent()

	def getEvents(self):
		return self.events
