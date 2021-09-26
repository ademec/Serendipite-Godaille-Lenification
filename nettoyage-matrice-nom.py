import json
import csv
ALPHA = ' \0 abcdefghijklmnopqrstuvwxyzçéèëïöüêîôû-\''

with open('./data/noms2d.json') as f:
    model2d = json.load(f)

i = 0
with open("./data/noms2D.csv", 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for i in range(len(model2d)):
        row = model2d[i].copy()
        wr.writerow(row)
