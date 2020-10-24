import json

data = {
	1:{
		"ID": 1, 
		"NAME": "jacksensdfsdfsdf"
	},
	2: {
		"ID": 2, 
		"NAME": "jacksensdfsdfsdf"
	}
}
i = len(data)
while i < 10:
	i = len(data) + 1
	data[i] = {"ID" : 3, "NAME":"asdasdasd"}

with open("data_json.json", "w") as write_file:
	json.dump(data, write_file)