# imports
import sys
from parser import parseFile
from parser import parseCommandLine
from problem import Problem
from node import Node
import genetic

# general system
def main(problem, debug):
  result = genetic.solve(problem)
  return; #TODO fix printing below

  val = result[0]
  error = abs(val - problem.targetnum)
  organism = result[1]
  time = result[2]
  population = result[3]
  generation = result[4]

  if debug == None or debug == True:
    try:
      endNode.print_path()
    except:
      print("No steps taken...")

    print("Value found: %r" % val)
    print("Error: %r" % error)
    print("Size of organism: %r" % organism)
    print("Time taken: %r" % time)
    print("Population size: %r" % population)
    print("Number of generations: %r" % generation)

  return (error, organism, time, population, generation)

if __name__ == "__main__":
   main( parseFile(parseCommandLine(sys.argv[1:])), True)
