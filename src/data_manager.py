import json
secret = json.load(open("secret.json", "r"))
data_object = json.load(open("data_object.json", "r"))

def save_data_object():
    with open('data_object.json', 'w') as outfile:
        json.dump(data_object, outfile)