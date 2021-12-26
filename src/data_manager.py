import json

class data_object:
    def __init__(self, path):
        self.path = path
        with open(path, 'r') as file:
            self.data = json.load(file)

    def get(self, key):
        return self.data[key]

    def save(self):
        with open(self.path, 'w') as outfile:
            json.dump(self.data, outfile)

    def update(self, key, value):
        self.data[key] = value
        self.save()
    
    def append(self, key, value):
        self.data[key].append(value)
        self.save()



secret = data_object("secret.json")
meta_data = data_object("data.json")