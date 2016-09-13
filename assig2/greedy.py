from problem import Problem
from node import Node
import queue
import time

from utility import goal_test
from utility import closer
from heuristics import heuristic

# greedy algorithm
# @param problem - the input defining all problem parameters
def solve(problem):
  nodeCount = 0
  maxDepth = 0
  current = Node(heuristic(problem.startnum, problem), problem.startnum, 0, None, None)
  frontier = queue.PriorityQueue() #sorted on cost of operation
  frontier.put(current)
  explored = set()  #set
  frontierSet = set()
  frontierSet.add(current)
  start_time = time.time()
  best = current

  while time.time() - start_time  < problem.time - 0.0001: #while we have time
    if frontier.empty():
      break
    current = frontier.get()
    if goal_test(current.data, problem.targetnum):
      break #success
    explored.add(current)

    # bookkeeping
    depth = current.depth + 1
    if depth > maxDepth:
      maxDepth = depth

    # apply all operations to the current node
    for op in problem.ops:
      child = problem.evalOp(current.data, op)
      if child not in explored or frontierSet:
        nodeCount += 1  # bookkeeping
        child_node = Node(heuristic(child, problem), child, depth, current, op)

        # maintain best so far
        if closer(best.data, child, problem.targetnum):
          best = child_node
        frontier.put(child_node)
        frontierSet.add(child)

  # if we run out of time, make sure we are returning the best solution
  if heuristic(current.data, problem) < heuristic(best.data, problem):
    best = current

  # return the answer and bookkeeping information
  return (best.data, best.depth, time.time()-start_time, nodeCount, maxDepth, best)
