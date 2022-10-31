import sys
import os
currentDirectory = os.getcwd()
sys.path.append(currentDirectory + '/src/helpers')

from calculationHelpers import multiplyMatrix

def reflection3dXY(vector):
  matrixTransformation = [[1, 0, 0], [0, 1, 0], [0, 0, -1]]
  return multiplyMatrix(matrixTransformation, vector)

def reflection3dXZ(vector):
  matrixTransformation = [[1, 0, 0], [0, -1, 0], [0, 0, 1]]
  return multiplyMatrix(matrixTransformation, vector)

def reflection3dYZ(vector):
  matrixTransformation = [[-1, 0, 0], [0, 1, 0], [0, 0, 1]]
  return multiplyMatrix(matrixTransformation, vector)