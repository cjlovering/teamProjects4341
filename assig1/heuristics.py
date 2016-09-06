# heuristic functions
import math


absDifference = lambda current, target : abs(current - target)
squareDifference = lambda current, target : abs(current ** 2 - target ** 2)

def heuristics():
  return (absDifference, squareDifference)

def heuristic(current, target):
  return absDifference(current, target)

#h = heuristics()
#for f in h:
 #print(f(7,9))



