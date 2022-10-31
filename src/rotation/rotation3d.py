import sys
import os
currentDirectory = os.getcwd()
sys.path.append(currentDirectory + '/src/helpers')

import numpy as np
from calculationHelpers import multiplyMatrix, convertRadiusToGraus

def rotation3dX(vector, angle):
  angleInGraus = convertRadiusToGraus(angle)
  matrixTransformation = [[1, 0, 0], [0, np.cos(angleInGraus), -np.sin(angleInGraus)], [0, np.sin(angleInGraus), np.cos(angleInGraus)]]

  if(angle == 0): return vector
  if(angle < 0):
    matrixTransformation = [[1, 0, 0], [0, np.cos(angleInGraus), np.sin(angleInGraus)], [0, -np.sin(angleInGraus), np.cos(angleInGraus)]]

  return multiplyMatrix(matrixTransformation, vector)

def rotation3dY(vector, angle):
  angleInGraus = convertRadiusToGraus(angle)
  matrixTransformation = [[np.cos(angleInGraus), 0, np.sin(angleInGraus)], [0, 1, 0], [-np.sin(angleInGraus), 0, np.cos(angleInGraus)]]
  
  if(angle == 0): return vector
  if(angle < 0):
    matrixTransformation = [[np.cos(angleInGraus), 0, -np.sin(angleInGraus)], [0, 1, 0], [np.sin(angleInGraus), 0, np.cos(angleInGraus)]]


  return multiplyMatrix(matrixTransformation, vector)

def rotation3dZ(vector, angle):
  angleInGraus = convertRadiusToGraus(angle)
  matrixTransformation = [[np.cos(angleInGraus), -np.sin(angleInGraus), 0], [np.sin(angleInGraus), np.cos(angleInGraus), 0], [0, 0, 1]]
  
  if(angle == 0): return vector
  if(angle < 0):
    matrixTransformation = [[np.cos(angleInGraus), np.sin(angleInGraus), 0], [-np.sin(angleInGraus), np.cos(angleInGraus), 0], [0, 0, 1]]

  return multiplyMatrix(matrixTransformation, vector)