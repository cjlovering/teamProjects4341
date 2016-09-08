# heuristic functions
import math


abs_difference = lambda current, problem : abs(current - problem.targetnum)
square_difference = lambda current, problem : abs(current ** 2 - problem.targetnum ** 2)

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

def heuristics():
  return (abs_difference, square_difference)

def heuristic(current, problem):
  return min([abs_difference(current, problem), sub_problems(current, problem)])

#h = heuristics()
#for f in h:
 #print(f(7,9))

