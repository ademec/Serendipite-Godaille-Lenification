from constants import ALPHA

def generate_model3d(words):
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
        for k in range(len(ALPHA)):
          v = cumul + model[i][j][k]
          model[i][j][k] = v / s
          cumul = v

  return model

def generate_model2d(words):
  model = []
  for _ in range(len(ALPHA)):
    model.append([0] * len(ALPHA))
  
  for word in words:
    i = 0
    for c in word:
      if c not in ALPHA:
        print(word)
        return
      j = ALPHA.index(c)
      model[i][j] += 1
      i = j
    model[i][0] += 1

  for i in range(len(ALPHA)):
    s = sum(model[i])
    if s > 0:
      for j in range(len(ALPHA)):
        model[i][j] = model[i][j] / s
  
  return model
