import json

f = open("backup_data.json")
data = json.load(f)
for i in data["Instant_Games"]:
    print(i)
f.close()
