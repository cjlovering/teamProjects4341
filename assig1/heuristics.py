# heuristic functions
import math

NOT_THIS_HEURISTIC = 12312312312222212

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
    return NOT_THIS_HEURISTIC  # numbers were too big
#    if op[0] == '^':
#      subtarget_diff.append(abs(current - (math.pow(problem.targetnum, 1 / op[1]))))
  return min(subtarget_diff)

def abs_difference(current, target):
  return abs(current - target)

def heuristic(current, problem):
  return min([abs_difference(current, problem.targetnum), sub_problems(current, problem)])
