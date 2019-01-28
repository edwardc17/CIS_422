import calendarClasses
def main():
	#print("in main")
	today = calendarClasses.event("1:37pm", "1/18/19", "Hello")
	tomorrow = calendarClasses.event("1:37pm", "1/19/19", "Bye")
	cal = calendarClasses.calendar('saveFile.dat')
	#print("objects made")

	cal.addEvent(today)
	obj = cal.loadFile()
	#print(obj[0].printEvent())

	cal.addEvent(tomorrow)
	obj = cal.loadFile()
	print("1")
	for i in obj:
		i.printEvent()

	#cal.removeEvent(today)
	#obj = cal.loadFile()

	print("2")
	cal.editEvent(today, "2:39pm")
	today.printEvent()

	print("3")
	obj = cal.loadFile()
	for i in obj:
		i.printEvent()

	print("4")
	cal.editEvent(tomorrow, None, "1/22/19")
	tomorrow.printEvent()
	
	print("5")
	obj = cal.loadFile()
	for i in obj:
		i.printEvent()
	
	print("6")
	cal.editEvent(today, None, None, "Yo")
	today.printEvent()

	print("7")
	obj = cal.loadFile()
	for i in obj:
		i.printEvent()

	print("8")
	cal.editEvent(tomorrow, "10pm", None, "poo")
	tomorrow.printEvent()
	#obj[0].printEvent()

print("hi")
main()
