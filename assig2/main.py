# imports
import sys
from parser import parseFile
from parser import parseCommandLine
from problem import Problem
from node import Node
import genetic

# general system
def main(problem, debug, params):

  if params is None:
    params = [1, 30, 1, 150, 0.01, 0.90, 0.00]  #[minOp, maxOp, elitism, starting_population, mutation_chance, crossover_chance, threshold]
  result = genetic.solve(problem, params)
  
  best = result[0]
  val = best.data
  error = abs(val - problem.targetnum)
  size = len(best.op_seq)
  time = result[1]
  population = result[2]
  generation = result[3]

  if debug == None or debug == True:
    #operations.print_seq(problem.startnum, best.op_seq)

    print("Value found: %r" % val)
    print("Error: %r" % error)
    print("Size of organism: %r" % size)
    print("Time taken: %r" % time)
    print("Population size: %r" % population)
    print("Number of generations: %r" % generation)

  return (val, size, time, population, generation)

if __name__ == "__main__":
   main( parseFile(parseCommandLine(sys.argv[1:])), True, None)
