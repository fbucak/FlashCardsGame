import json


class User:
    def __init__(self, name="Name", level=1, totaltime=0):
        self.name = name
        self.level = level
        self.totaltime = totaltime
    
    def readjson(self):
        with open(r'username.json', 'r') as json_file:
            data = json.loads(json_file)
            return data
   
    def savejson(self, dict):
        with open(r'username.json', 'w') as json_file:
            json.dump(dict, json_file)