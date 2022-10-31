import sys
import os
currentDirectory = os.getcwd()
sys.path.append(currentDirectory + '/src/helpers')

from calculationHelpers import multiplyMatrix

def reflection2dX(vector):
  matrixTransformation = [[-1, 0], [0, 1]]
  return multiplyMatrix(matrixTransformation, vector)

def reflection2dY(vector):
  matrixTransformation = [[1, 0], [0, -1]]
  return multiplyMatrix(matrixTransformation, vector)