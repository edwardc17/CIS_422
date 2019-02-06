'''
Author:  Anna Saltveit(AS)
Update date:  Feburary 5, 2019
'''

import pickle
import os.path

class EventObj:
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

	def editEventIndex(self, index):
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

	# For testing.
	def printEvent(self):
		print("Event: ", self.name)
		print("Event category: ", self.category)
		print("Event description: ", self.desc)
		print("Start from ", self.start_time, " to ", self.end_time)
		print("Event color: ", self.color)
		print("Event index: ", self.index)
		print("-----------------------------------------------------------------------")

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
		if not os.path.isfile(self.filename):
			# If self.filename doesn't exist, create it with 'w+'
			with open(self.filename, 'w+') as file:
				# Don't do anything else with file, as it's empty
				return {}
		else:
			# self.filename exists, so open and read it
			with open(self.filename, 'rb') as file:
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
		Adds an already created event to the events dict and saves the new data to the file.
		'''
		# List of events already exists
		if day in self.events:
			self.events[day].append(event)
		else:
			# Create new list of events for that day
			self.events[day] = [event]
		
		self.saveFile() 


	def removeEvent(self, event, day):
		'''
		Remove event from events dict, saves it. 
		'''
		self.events[day].remove(event)
		self.saveFile()


	def printCal(self):
		'''
		For testing.
		'''
		for day in self.events:
			for e in self.events[day]:
				e.printEvent()

	def getEvents(self):
		return self.events


