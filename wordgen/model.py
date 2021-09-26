from constants import ALPHA

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
  
  '''
  for i in range(len(ALPHA)):
    for j in range(len(ALPHA)):
      s = sum(model[i][j])
      if s > 0:
        cumul = 0
        for k in range(len(ALPHA)):
          v = cumul + model[i][j][k]
          model[i][j][k] = v / s
          cumul = v
  '''
  for i in range(len(ALPHA)):
    for j in range(len(ALPHA)):
      s = sum(model[i][j])
      if s > 0:
        for k in range(len(ALPHA)):
          model[i][j][k] = model[i][j][k] / s

  return model
