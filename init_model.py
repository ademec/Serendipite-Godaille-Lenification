import csv
import json

from constants import DATA_FOLDER, WORDS_FILENAME, SURNAME_MODEL_FILENAME, LASTNAME_MODEL_FILENAME
from wordgen.model import generate_model

if __name__ == "__main__":
  with open(DATA_FOLDER + WORDS_FILENAME, "r", encoding="utf-8") as f:
    names = list(csv.reader(f))
  
  surnames = []
  lastnames = []
  for [surname, lastname] in names:
    surnames.append(surname.lower())
    lastnames.append(lastname.lower())
  
  surname_model = generate_model(surnames)
  lastname_model = generate_model(lastnames)
  
  with open(DATA_FOLDER + SURNAME_MODEL_FILENAME, "w") as f:
    json.dump(surname_model, f)
  
  with open(DATA_FOLDER + LASTNAME_MODEL_FILENAME, "w") as f:
    json.dump(surname_model, f)