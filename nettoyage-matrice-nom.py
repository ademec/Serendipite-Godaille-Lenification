import json
import csv
ALPHA = '\0 abcdefghijklmnopqrstuvwxyzçéèëïöüêîôû-\''

f = open('./data/prenoms.json')
model3d = json.load(f)
model2d = []
for liste in range(len(ALPHA)):
    model2d.append([0] * len(ALPHA))

for i in range(len(ALPHA)):
    for j in range(len(ALPHA)):
        for k in range(len(ALPHA)):
            model2d[i][j] += model3d[i][j][k]

with open("./data/prenoms2D.csv", 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
     for elem in model2d:
        wr.writerow(elem)
