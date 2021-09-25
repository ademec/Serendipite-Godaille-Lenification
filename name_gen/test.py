import random
import json

from marksman import marksman
from model import create_model

if __name__ == '__main__':
    names_file = 'dataset/fr_gutenberg.txt'
    model_file = 'model.json'
    recreate_model = False

    if recreate_model:
        # only one name per line in the dataset file 
        with open(names_file, 'r', encoding='utf8') as f:
            names = f.read().splitlines()
        model = create_model(names)
        with open(model_file, 'w', encoding='utf8') as f:
            json.dump(model, f, ensure_ascii=False, separators=(',', ':'), indent=2)
    else:
        with open(model_file, 'r', encoding='utf8') as f:
            model = json.load(f)

    for i in range(10):
        id_bits = [random.randint(0, 1) for _ in range(128)]
        name = marksman(id_bits, model)
        print(name)
