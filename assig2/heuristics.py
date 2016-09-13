# heuristic functions
import math

# default heuristic
def abs_difference(current, target):
  return abs(current - target)

# return the smallest value resulting from our set of heuristics
def heuristic(current, problem):
  return abs_difference(current, problem.targetnum)
