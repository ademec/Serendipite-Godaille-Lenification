import csv
import json

DATA_FOLDER = "../data"
WORDS_FILENAME = "liste-nom.csv"
SURNAME_MODEL_FILENAME = "prenoms.json"
LASTNAME_MODEL_FILENAME = "noms.json"
ALPHA = '\0 abcdefghijklmnopqrstuvwxyzçéèëïöüêîôû-\''

def generate_model(words):
  model = []
  for _ in range(len(ALPHA)):
    plane = []
    for __ in range(len(ALPHA)):
      line = []
      for ___ in range(len(ALPHA)):
        line.append(0)
      plane.append(line)
    model.append(plane)
  
  for word in words:
    i = 0
    j = 0
    for c in word:
      if c not in ALPHA:
        print(word)
        return
      k = ALPHA.index(c)
      model[i][j][k] += 1
      i = j
      j = k
    model[i][j][0] += 1
  
  for i in range(len(ALPHA)):
    for j in range(len(ALPHA)):
      s = sum(model[i][j])
      if s > 0:
        cumul = 0
        for k in range(1, len(ALPHA)):
          v = cumul + model[i][j][k]
          model[i][j][k] = v / s
          cumul = v

  return model

if __name__ == "__main__":
  with open(DATA_FOLDER + WORDS_FILENAME, "r", encoding="utf-8") as f:
    names = list(csv.reader(f))
  
  surnames = []
  lastnames = []
  for [surname, lastname] in names:
    surnames.append(surname.lower())
    lastnames.append(lastname.lower())
  
  print(len(surnames), len(lastnames))
  
  surname_model = generate_model(surnames)
  lastname_model = generate_model(lastnames)
  
  with open(DATA_FOLDER + SURNAME_MODEL_FILENAME, "w") as f:
    json.dump(surname_model, f)
  
  with open(DATA_FOLDER + LASTNAME_MODEL_FILENAME, "w") as f:
    json.dump(surname_model, f)
