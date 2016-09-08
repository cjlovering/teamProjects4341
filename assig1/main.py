# imports
import sys
from parser import parse
from problem import Problem
from node import Node
import greedy
import iterative

# constants
ITERATIVE = 'iterative'
GREEDY = 'greedy'

# general system
def main(argv):
  problem = parse(argv)
  
  if GREEDY == problem.alg:
    result = greedy.solve(problem)
  else:
    result = iterative.solve(problem)
    
  val = result[0]
  error = abs(val - problem.targetnum)
  steps = result[1]
  time = result[2]
  nodes = result[3]
  max = result[4]
  endNode = result[5]
  try: 
    endNode.printPath()
  except:
    print("No steps taken...")

  print("Algorithm used: " + problem.alg)
  print("Error: %r" % error)
  print("Value found: %r" % val)
  print("Steps taken: %r" % steps)
  print("Time taken: %r" % time)
  print("Nodes expanded: %r" % nodes)
  print("Max depth traversed: %r" % max)

if __name__ == "__main__":
   main(sys.argv[1:])
