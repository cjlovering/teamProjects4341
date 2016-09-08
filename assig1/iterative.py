from problem import Problem
from node import Node
import time
import math
from utility import goal_test
from heuristics import heuristic


node_count = 0

# iterative algorithm
# @param problem - the input defining all problem parametersdef solve(problem):
def solve(problem):
  global node_count
  start_time = time.time()
  depth = 0
  best = Node(0, problem.startnum, 0, None, None)
  result = best
  node_count = 0

  while(time.time() - start_time + 0.00001 * depth < problem.time): #while we have time + fudge factor TODO: (experiment)
    if cut_off(result.data, problem.targetnum, problem):  #cut search here: inc or found goal
      best = result
      break
    elif closer(best.cost, result.data, problem):  #update best so far
      best = result
    result = depth_limited_search(problem, depth)
    depth += 1
  
  if closer(best.cost, result.data, problem):  #update best so far (if last iteration finds answer)
    best = result
  return (best.data, best.depth, time.time()-start_time, node_count, depth, best)

# idea: probably use the same set of heuristics to det answer
# @return true if the new val is closer than the old val
def closer(old, new, problem):
  return heuristic(new, problem) < old
    
# @param problem - the problem to solve
# @param limit - the depth limit
# @return the current val (the best so far?)
def depth_limited_search(problem, limit):
  n = Node(0, problem.startnum, 0, None, None)
  return recursive_dls(n, problem, limit) 

def recursive_dls(current, problem, limit):
  global node_count
  node_count += 1
  if goal_test(current.data, problem.targetnum):
    print("goal")
    return current
  elif limit == 0:
    return current
  else:
    for op in problem.ops:
      child = problem.evalOp(current.data, op)
      child_node = Node(0, child, current.depth + 1, current, op)
      result = recursive_dls(child_node, problem, limit - 1)
      if cut_off(result.data, problem.targetnum, problem):
        break
  return result
  
# @return - if we reached the goal or hit a cut-off
def cut_off(result, target, problem):
  if goal_test(result, target):
    return True
  elif problem.cut_off(result):
    return True
  return False
