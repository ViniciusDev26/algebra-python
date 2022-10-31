def projection2DX(vector: list) -> list:
  matrixTransformation = [1, 0]
  result = []
  index = 0
  for number in vector:
    result.append(number * matrixTransformation[index])
    index += 1
    
  return result

def projection2DY(vector: list) -> list:
  matrixTransformation = [0, 1]
  result = []
  index = 0
  for number in vector:
    result.append(number * matrixTransformation[index])
    index += 1

  return result
