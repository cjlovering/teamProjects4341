# imports
import sys
from parser import parseFile
from parser import parseCommandLine
from problem import Problem
import operations
import genetic

# general system
def main(problem, debug, params):

  if params is None:
    #params = [1, 30, 4, 100, 0.01, 0.90, 0.00, True, False, [0.33,0.33,0.34], 2 ]
    params = [1, 30, 4, 150, 0.01, 0.90, 0.00, True, False, [0.33,0.33,0.34], 1 ]

    #[minOp, maxOp, elitism, starting_population, mutation_chance, crossover_chance, threshold, random_start, greedy_random, mutation_roles, children_num]
  result = genetic.solve(problem, params)

  if result is None:
    print("there is no solution: only invalids")
    return None

  best = result[0]
  val = best.data
  error = abs(val - problem.targetnum)
  size = len(best.op_seq)
  time = result[1]
  population = result[2]
  generation = result[3]

  if debug == None or debug == True:
    best.print_seq(problem.startnum, problem)

    print("Value found: %r" % val)
    print("Error: %r" % error)
    print("Size of organism: %r" % size)
    print("Time taken: %r" % time)
    print("Population size: %r" % population)
    print("Number of generations: %r" % generation)

  return (error, size, time, generation)

if __name__ == "__main__":
   main( parseFile(parseCommandLine(sys.argv[1:])), True, None)
