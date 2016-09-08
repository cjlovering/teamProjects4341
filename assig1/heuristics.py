# heuristic functions
import math

squareDifference = lambda current, target : abs(current ** 2 - target ** 2)

def heuristics():
  return (absDifference, squareDifference)

def heuristic(current, target):
  return absDifference(current, target)

def abs_difference(current, target):
  return abs(current - target)

#h = heuristics()
#for f in h:
 #print(f(7,9))
