import numpy as np

def multiplyMatrix(matrixA, matrixB):
  return np.matmul(matrixA, matrixB)

def convertRadiusToGraus(angleInRadius):
  return angleInRadius * (np.pi / 180)
