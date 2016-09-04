from problem import Problem
import time
import math

node_count = 0

# iterative algorithm
# @param problem - the input defining all problem parametersdef solve(problem):
def solve(problem):
  global node_count
  start_time = time.time()
  depth = 0
  best = problem.startnum
  result = best
  node_count = 0

  while(time.time() - start_time < problem.time): #while we have time!
    result = depth_limited_search(problem, depth)
    if goal_test(result, problem.targetnum): 
      best = result
      break
    elif closer(best, result, problem.targetnum):
      best = result
    depth += 1
  return (best, depth, time.time() - start_time, node_count, depth)

# TODO: implement
# idea: probably use the same set of heuristics to det answer
# @return true if the new val is closer than the old val
def closer(old, new, target):
  return True

# TODO: implement
# @param problem - the problem to solve
# @param limit - the depth limit
# @return the current val (the best so far?)
def depth_limited_search(problem, limit):
  return recursive_dls(problem.startnum, problem, limit) 

def recursive_dls(current, problem, limit):
  global node_count
  node_count += 1
  if goal_test(current, problem.targetnum):
    return current
  elif limit == 0:
    return current
  else:
    for op in problem.ops:
      child = problem.evalOperation(current, op)
      result = recursive_dls(child, problem, limit - 1)
      if cut_off(result, problem.targetnum):
        break
    return result
  # we can add a cutoff here, as in we're looking for 5, and only getting bigger 4 *2 *2 *2
  
  

# @return - if we reached the goal
def goal_test(result, target):
  return (float(result)) == (float(target))

# @return - if we reached the goal or hit a cut-off
def cut_off(result, target):
  if goal_test(result, target):
    return True
  return False
