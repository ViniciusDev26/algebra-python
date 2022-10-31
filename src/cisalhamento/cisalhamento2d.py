def cisalhamento2D(vector, dx, dy):
  x = vector[0]
  y = vector[1]

  vectorResult = []

  newx = x + (dx*y)
  newy = y + (dy*x)

  if(not(y == dy) and x == dx):
    vectorResult.append(x)
    vectorResult.append(newy)
  elif(not(x == dx) and y == dy):
    vectorResult.append(newx)
    vectorResult.append(y)
  else:
    vectorResult.append(newx)
    vectorResult.append(newy)

  return vectorResult
