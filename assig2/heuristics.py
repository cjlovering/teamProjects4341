# heuristic functions
import math

HEURISTIC_OUT_OF_RANGE = 12312312312222212

# heuristic to detemine how far the current is from a sub goal
def sub_problems(current, problem):
  subtarget_diff = []
  try:
    for opi in range(len(problem.ops)):
      if problem.ops[opi][0] == '+':
        subtarget_diff.append(abs(current - (problem.sub_targets[opi])))
      if problem.ops[opi][0] == '-':
        subtarget_diff.append(abs(current - (problem.sub_targets[opi])))
      if problem.ops[opi][0] == '/':
        subtarget_diff.append(abs(current - (problem.sub_targets[opi])))
      if problem.ops[opi][0] == '*':
        subtarget_diff.append(abs(current - (problem.sub_targets[opi])))
  except:
    return HEURISTIC_OUT_OF_RANGE  # numbers were too big

  return min(subtarget_diff)

# default heuristic
def abs_difference(current, target):
  return abs(current - target)

# return the smallest value resulting from our set of heuristics
def heuristic(current, problem):
  return min([abs_difference(current, problem.targetnum), sub_problems(current, problem)])
