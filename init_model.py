import csv
import json

from constants import DATA_FOLDER, WORDS_FILENAME, SURNAME_MODEL2D_FILENAME, LASTNAME_MODEL2D_FILENAME, SURNAME_MODEL3D_FILENAME, LASTNAME_MODEL3D_FILENAME
from wordgen.model import generate_model2d, generate_model3d

if __name__ == "__main__":
  with open(DATA_FOLDER + WORDS_FILENAME, "r", encoding="utf-8") as f:
    names = list(csv.reader(f))
  
  surnames = []
  lastnames = []
  for [surname, lastname] in names:
    surnames.append(surname.lower())
    lastnames.append(lastname.lower())
  
  surname_model3d = generate_model3d(surnames)
  lastname_model3d = generate_model3d(lastnames)
  surname_model2d = generate_model2d(surnames)
  lastname_model2d = generate_model2d(lastnames)
  
  with open(DATA_FOLDER + SURNAME_MODEL2D_FILENAME, "w") as f:
    json.dump(surname_model2d, f)
  
  with open(DATA_FOLDER + LASTNAME_MODEL2D_FILENAME, "w") as f:
    json.dump(surname_model2d, f)

  with open(DATA_FOLDER + SURNAME_MODEL3D_FILENAME, "w") as f:
    json.dump(surname_model3d, f)
  
  with open(DATA_FOLDER + LASTNAME_MODEL3D_FILENAME, "w") as f:
    json.dump(surname_model3d, f)