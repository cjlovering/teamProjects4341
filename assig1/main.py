# imports
import sys
from parser import parseFile
from parser import parseCommandLine
from problem import Problem
from node import Node
import greedy
import iterative

# constants
ITERATIVE = 'iterative'
GREEDY = 'greedy'

# general system
def main(problem, debug):
  
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


  if debug == None or debug == True:
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
  
  return (problem.alg, error, val, steps, time, nodes, max)

if __name__ == "__main__":
   main( parseFile(parseCommandLine(sys.argv[1:])), True)


