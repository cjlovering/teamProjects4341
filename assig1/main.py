# imports
import sys
from parser import parse
from problem import Problem
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
    
  errors = 0
  val = result[0]
  steps = result[1]
  time = result[2]
  nodes = result[3]
  max = result[4]

  print("Algorithm used: " + problem.alg)
  print("Errors: %r" % errors)
  print("Value found: %r" % val)
  print("Steps taken: %r" % steps)
  print("Time taken: %r" % time)
  print("Nodes expanded: %r" % nodes)
  print("Max depth travered: %r" % max)

if __name__ == "__main__":
   main(sys.argv[1:])
