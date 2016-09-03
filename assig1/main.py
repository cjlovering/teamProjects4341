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
  resutt = []
  
  if GREEDY == problem.alg:
    result = greedy.solve(problem)
  else:
    result = iterative.solve(problem)

    

if __name__ == "__main__":
   main(sys.argv[1:])
