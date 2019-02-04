import pickle

data = {'2019-02-03': {'event1':['description for event1','8:00','9:00']}}
data['2019-02-03']['event2'] = ['description for event2','10:00','11:30']
#data['2019-02-04'] = {}
#data['2019-02-05'] = {}

with open('calendar.pickle','wb') as f:
	pickle.dump(data,f,protocol=pickle.HIGHEST_PROTOCOL)



with open('calendar.pickle', 'rb') as f:
	calendar = pickle.load(f)

test = {}
test = calendar
for date,event_dic in calendar.items():
	if date == '2019-02-03':
		for event, eventItem in event_dic.items():
			print(eventItem[0])
