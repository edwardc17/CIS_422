import pickle

class event:
	def __init__(self, time, date, text):
		self.time = time
		self.date = date
		self.text = text

	def printEvent(self):
		print("date: " + self.date + " time: " + self.time + " text: " + self.text)

class calendar:
	def __init__(self, filename):
		self.events = [] # Data for saving
		self.file = filename

	
	def loadFile(self):
		# Manipulation of data happens outside of function
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
		self.events.append(event)
		self.saveFile() 
		#loadFile() # Need to load for GUI? but not here?

	def removeEvent(self, event):
		self.events.remove(event)
		self.saveFile()
		#loadFile() # Need to load for GUI? but not here?

	def printCal():
		for i in self.events:
			i.printEvent()