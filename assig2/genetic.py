from problem import Problem
from node import Node
import time
import math
from utility import goal_test
from utility import closer
from heuristics import heuristic
from organism import Organism

# iterative algorithm
# @param problem - the input defining all problem parameters
def solve(problem):
  global node_count
  global start_time
  global best
  start_time = time.time()
  depth = 0
  best = Node(heuristic(problem.startnum, problem), problem.startnum, 0, None, None)
  result = best
  node_count = 0

  population = []
  while True: # we exit due to time below
    #crossover

    #mutate

    #cull




  return (best.data, best.depth, time.time()-start_time, node_count, depth, best)
