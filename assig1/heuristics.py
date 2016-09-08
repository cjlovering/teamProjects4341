# heuristic functions
import math


def sub_problems(current, problem):
  subtarget_diff = []
  for op in problem.ops:
    if op[0] == '+':
      subtarget_diff.append(abs(current - (problem.targetnum - op[1])))
    if op[0] == '-':
      subtarget_diff.append(abs(current - (problem.targetnum + op[1])))
    if op[0] == '/':
      subtarget_diff.append(abs(current - (problem.targetnum * op[1])))
    if op[0] == '*':
      subtarget_diff.append(abs(current - (problem.targetnum / op[1])))
#    if op[0] == '^':
#      subtarget_diff.append(abs(current - (math.pow(problem.targetnum, 1 / op[1]))))
  return min(subtarget_diff)

def abs_difference(current, target):
  return abs(current - target)

def heuristic(current, problem):
  return min([abs_difference(current, problem.targetnum), sub_problems(current, problem)])
