import sys
import os
currentDirectory = os.getcwd()
sys.path.append(currentDirectory + '/src/helpers')

import numpy as np
from calculationHelpers import multiplyMatrix

def rotation2d(vector, angle):
  angleInGraus = angle * (np.pi / 180)
  matrixTransformation = [[np.cos(angleInGraus), -np.sin(angleInGraus)], [np.sin(angleInGraus), np.cos(angleInGraus)]]
  
  if(angle == 0): return vector
  if(angle < 0):
    matrixTransformation = [[np.cos(angleInGraus), np.sin(angleInGraus)], [-np.sin(angleInGraus), np.cos(angleInGraus)]]

  return multiplyMatrix(matrixTransformation, vector)
  