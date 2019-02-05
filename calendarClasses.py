import pickle

class event:
	'''
	Contains all data needed to show and manipulate event.
	
	AS
	'''
	def __init__(self, start_time, end_time, name, desc, category, color, index):
		self.start_time = start_time
		self.end_time = end_time
		self.name = name
		self.desc = desc # Description
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
	'''
	Stores events in a file to use between program uses.
	Filename must be given, but if the file does not exist, it will be created in loadFile or saveFile
	whichever is called first.
	
	AS
	'''
	def __init__(self, filename):
		self.events = {} # Keys are date strings, values are event objects
		self.filename = filename # String

	
	def loadFile(self):
		'''
		Returns a dictionary: keys are date strings and values are event objects.
		'''
		with open(self.filename, 'rb+') as file:
			obj = pickle.load(file)
			return obj

	def saveFile(self):
		'''
		Saves entire dictionary to file. Every save overwrites previous data.
		'''
		with open(self.filename, 'wb+') as file:
			pickle.dump(self.events, file, protocol=2)

	def addEvent(self, event, day):
		'''
		Adds an already created event to the events dict and save the new data to the file.
		'''
		# List already exists
		if day in self.events:
			self.events[day].append(event)
		else:
			# Create new list for that day
			self.events[day] = [event]
		
		self.saveFile() 


	def removeEvent(self, event, day):
		'''
		Remove event from events dict, save and load new 
		'''
		self.events[day].remove(event)
		self.saveFile()
		#new = self.loadFile()
		#return new

	def editEvent(self, event, start_time=None, end_time=None, name=None, desc=None, category=None, color=None):
		'''
		All editing functions of an event are grouped into one place.
		This makes it easier to change the event class in future updates, and to use/find all editing methods.
		But it also requires filling non-used parameters with None(s) up until the last provided parameter.
		
		Examples:
		cal.editEvent(event, None, None, "Running")
		cal.editEvent(event, "01:30am")
		cal.editEvent(event, None, "10:05pm", None, None, None, "Blue")
		'''
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
		#new = self.loadFile()
		#return new

	def printCal(self):
		'''
		For testing.
		'''
		for day in self.events:
			for e in self.events[day]:
				e.printEvent()

	def getEvents(self):
		return self.events

