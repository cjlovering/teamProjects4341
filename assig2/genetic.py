import time
import math
import random

from problem import Problem
from utility import goal_test
from utility import closer
from heuristics import heuristic
from organism import Organism

# genetic algorithm
# @param problem - the input defining all problem parameters
def solve(problem, params):
  try:
    r = _solve(problem, params)
  except:
    return None  # there is no solution (only invalids)

# genetic algorithm
def _solve(problem, params):
  global generation

  minOp = params[0]
  maxOp = params[1]
  elitism = params[2]
  starting_population = params[3]
  mutation_chance = params[4]
  crossover_chance = params[5]
  threshold = params[6]
  random_start = params[7]
  greedy_huh = params[8]  # if we add operators greedily to start
  mutation_role_percents = params[9] # percent to delete, add, or modify
  children_num = params[10] # number of children each pair of parents should create

  start_time = time.time()

  generation = 0
  organism_count = 0 # we're keeping track of this in order to compare additional params (such as over-producing)

  target = problem.targetnum

  population = []

  # create the initial population
  for org in range(starting_population):
    op_seq = []
    starting_op_count = random.randint(minOp, maxOp) #see how we do!
    for op in range(starting_op_count):
      r = random.randint(0, 1)

      if r == 0:
        #greedy selection
        try:
          selected_op = op
          val = problem.eval_op(problem.startnum, selected_op)
          selected_val = val
    
          for operation in problem.ops:
            val = problem.eval_op(val, operation)
            if closer(selected_val, val, problem.targetnum):
              selected_op = operation
          op_seq.append(selected_op)
        except:
          op_seq.append(problem.ops[random.randint(0, len(problem.ops) - 1)])
      else:
        op_seq.append(problem.ops[random.randint(0, len(problem.ops) - 1)])
    population.append(Organism(op_seq))

  # data & fitness value calculations
  for org in population:
    org.set_data(problem)
    org.calculate_cost(problem)
  calculate_fitness(population)

  while True:
    # bookkeeping
    generation += 1

    # check if we're done! (or run out of time)
    if cut_off(population, start_time, problem.time, target):
      break;

    # breeding time
    new_population = []
    for i in range(len(population)):
      x = random_selection(population)
      y = random_selection(population)
      child = x.crossover(y)
      if small_random_chance(mutation_chance) and len(child.op_seq) > 1:
        child.mutate(mutation_role_percents, problem)
      new_population.append(child)

    # elitism
    population.sort(key=lambda x: x.cost, reverse=False)
    for i in range(elitism):
      if i < len(population) / 2:  # no more than 1/2 the population
        new_population.append(population[i])

    # calculate values and set the costs
    for org in new_population:
      org.set_data(problem)
      org.calculate_cost(problem)

    # culling the invalids
    cull_the_invalids(new_population)

    # culling the weak
    cull_the_weak(new_population, starting_population)

    # finding the fitness
    calculate_fitness(new_population)

    # setting the next generation
    population = new_population


  # get the best so far
  population.sort(key=lambda x: x.cost, reverse=False)
  best = population[0]

  return (best, time.time()-start_time, len(population), generation)

def cull_the_invalids(new_population):
  invalids = []
  for orgIndex in range(len(new_population)):
    if new_population[orgIndex].invalid:
      invalids.append(orgIndex)
  invalids.reverse()
  for index in invalids:
    del new_population[index]

def cull_the_weak(new_population, starting_population_count):
  to_cull = len(new_population) - starting_population_count
  if to_cull > 0:
    new_population.sort(key=lambda x: x.cost, reverse=True)
    del new_population[(len(new_population) - to_cull):]

# @param population - the current set of organisms
def calculate_fitness(population):
  sum_costs = 0
  for org in population:
    sum_costs += org.cost
  for org in population:
    org.set_fitness(1 - (org.cost / sum_costs))

# @param population - the current set of organisms
# @return - returns a random organism from the given population
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
  if selection is None:
    selection = population[random.randint(0, len(population) - 1)]
  return selection

# @param population - the current set of organisms
# @param start_time - when we started
# @param end_time - how much time we're alloted
# @param target - the number we're aiming for, the correct answer!
# @return {Boolean} - returns if we're done searching or not
def cut_off(population, start_time, end_time, target):
  if time.time()-start_time > end_time - 0.004:  #at 0.001 we went over once in a while
    return True
  for org in population:
    if goal_test(org.data, target):
      return True
  return False

# @param params - the object containing paramets for this run of the proble,
# @return {Boolean} - if a small random chance occured!
def small_random_chance(mutation_chance):
  return random.uniform(0.0, 1.) < mutation_chance
