import sys
import os
currentDirectory = os.getcwd()
sys.path.append(currentDirectory + '/src/helpers')
from calculationHelpers import multiplyMatrix

def projection3DXY(vector: list) -> list:
  matrixTransformation = [[1, 0, 0], [0, 1, 0], [0, 0, 0]]

  return multiplyMatrix(matrixTransformation, vector)

def projection3DYZ(vector: list) -> list:
  matrixTransformation = [[0, 0, 0], [0, 1, 0], [0, 0, 1]]

  return multiplyMatrix(matrixTransformation, vector)

def projection3DXZ(vector: list) -> list:
  matrixTransformation = [[1, 0, 0], [0, 0, 0], [0, 0, 1]]

  return multiplyMatrix(matrixTransformation, vector)

def projection2DY(vector: list) -> list:
  matrixTransformation = [0, 1]
  result = []
  index = 0
  for number in vector:
    result.append(number * matrixTransformation[index])
    index += 1

  return result
