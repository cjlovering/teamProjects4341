from problem import Problem
import queue
import time

from utility import goal_test
from heuristics import heuristic



# greedy algorithm
def solve(problem):
  nodes = 0
  maxDepth = 0
  current = (heuristic(problem.startnum, problem.targetnum), problem.startnum, 0) # h cost, data, depth
  frontier = queue.PriorityQueue()  #sorted on sorted(list(entries))[0] TODO: create a data struct with sorting and O(1) lookup
  frontier.put(current)
  explored = set()  #set
  frontierSet = set()
  frontierSet.add(current)
  start_time = time.time()
  
  while True:
    if frontier.empty():
      return (1,-1,-1,-1,-1) #failure
    current = frontier.get()
    if goal_test(current[1], problem.targetnum):
      break #success
    explored.add(current)
    
    for op in problem.ops:
      child = problem.evalOp(current[1], op)
      if child not in explored or frontierSet:
        nodes += 1
        depth = current[2] + 1
        if depth > maxDepth:
          maxDepth = depth
        child_node = (heuristic(child, problem.targetnum), child, depth)
#       child_node = (heuristic(child, problem.targetnum) + current[0], child, depth) # consider f = f + h vs f = h
        frontier.put(child_node)
        frontierSet.add(child_node)
      #TODO: this?
      #elif child in frontierSet:
        #if new heuristic is lower then replace frontier node with this one
        
       # print("todo")

  return (current[1], current[2], time.time()-start_time, nodes, maxDepth)
