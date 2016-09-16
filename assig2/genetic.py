from problem import Problem
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
  global organism_size
  global start_time
  global best
  global generation
  start_time = time.time()
  organism_size = 0
  generation = 0
  mutation_rate = 0.05 #not sure
  best = None
  target = problem.targetnum
  result = best
  elitism = 1
  
  starting_op_count = 5;#round( math.log(problem.targetnum) / math.log(problem.startnum)) + 1
  population = []

  m = len(problem.ops)
  n = starting_op_count
  starting_population_count = 150; #round( (math.factorial(m) / (math.factorial(n) * math.factorial(m - n))) / 2 )

  for org in range(starting_population_count):
    op_seq = []
    for op in range(starting_op_count):
      op_seq.append(problem.ops[random.randint(0, len(problem.ops) - 1)])
    population.append(Organism(op_seq))

  # data & fitness value calculations
  calculate_fitness(population, problem)

  while True: # we exit due to time below
    generation += 1
    
    if cut_off(population, start_time, problem.time, target):
      break;
    
    new_population = []

    # breeding time
    for i in range(len(population)):
      x = random_selection(population);
      y = random_selection(population);
      child = x.crossover(y)
      if small_random_chance():
        child = mutate(child)
      new_population.append(child)

    # elitism
    population.sort(key=lambda x: x.cost, reverse=True)

    for i in range(elitism):
      new_population.append(population[i])
      
    # data
    for org in new_population:
      org.set_data(problem)
      org.calculate_cost(problem)

    # culling the invalids
    invalids = []
    for orgIndex in range(len(new_population)):
      if new_population[orgIndex].invalid:
        invalids.append(orgIndex)
    invalids.reverse()
    for index in invalids:
      del new_population[index]

    # culling the weak
    to_cull = len(new_population) - starting_population_count
    if to_cull > 0:
      new_population.sort(key=lambda x: x.cost, reverse=False)
      del new_population[(len(new_population) - to_cull):]

    # finding the fitness
    calculate_fitness(new_population, problem)

    # setting the next generation
    population = new_population
  
  return (best.data, organism_size, time.time()-start_time, len(population), generation)

def calculate_fitness(population, problem):
  sum_costs = 0
  for org in population:
    org.set_data(problem) # TODO: factor out
    org.calculate_cost(problem)
    sum_costs += org.cost
  for org in population:
    org.set_fitness(1 - (org.cost / sum_costs))

def random_selection(population):
  percentile = random.uniform(0.0, len(population) - 1) #this is the sum of all fitness values
  current_percent = 0
  last_percent = 0
  selection = None

  for org in population:
    current_percent += org.fitness
    if percentile <= current_percent and percentile > last_percent:
      selection = org
      break
    else:
      last_percent = current_percent
  return selection

def cut_off(population, start_time, end_time, target):
  global best
  if best is None:
    best = population[0];

  if time.time()-start_time > end_time - 0.001:
    return True
  found = False
  i = 0
  for org in population:
    i += 1
    if goal_test(org.data, target):
      found = True
      break
    if closer(best.data, org.data, target):
      best = org
    
  return found

def small_random_chance():
  #random > variable
  return False
