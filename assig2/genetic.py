from problem import Problem
from node import Node
import time
import math
import random
from utility import goal_test
from utility import closer
from heuristics import heuristic
from organism import Organism


# genetic algorithm
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

  starting_op_count = round( math.log(problem.targetnum) / math.log(problem.startnum)) + 1
  population = []

  m = len(problem.ops)
  n = starting_op_count
  starting_population_count = 5; #round( (math.factorial(m) / (math.factorial(n) * math.factorial(m - n))) / 2 )

  for org in range(starting_population_count):
    op_seq = []
    for op in range(starting_op_count):
      op_seq.append(problem.ops[random.randint(0, len(problem.ops) - 1)])
    population.append(Organism(op_seq))

  while True: # we exit due to time below
    cut_off(population, start_time, problem.time)
    new_population = []
    calculate_fitness(population, problem)

    for i in range(len(population)):
      x = random_selection(population);
      y = random_selection(population);
      child = x.crossover(y)
      if small_random_chance():
        child = mutate(child)
      new_population.append(child)
    population = new_population

  return (best.data, best.depth, time.time()-start_time, node_count, depth, best)

def calculate_fitness(population, problem):
  sum_costs = 0
  charlie_s_magic_number = 2 / len(population)
  for org in population:
    org.set_data(problem)
    org.calculate_cost(problem)
    sum_costs += org.cost
  for org in population:
    org.set_fitness(charlie_s_magic_number - org.cost / sum_costs)

def random_selection(population):
  percentile = random.uniform(0.0, 1.0) #ex 0.11
  current_percent = 0
  selection = None

  for org in population:
    current_percent += org.fitness
    if percentile <= current_percent:
      selection = org
      break

  return selection

def cut_off(population, start_time, end_time):
  if time.time()-start_time > end_time - 0.001:
    return True
  found = False
  for org in population:
    print(org)
    #found =  org.data
  return found

def small_random_chance():
  #random > variable
  return False

def mutate(child):
  return child
