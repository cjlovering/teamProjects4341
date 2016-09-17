import random
from numpy import linspace
import unittest
from os import listdir
from os.path import isfile, join

from main import main
from parser import parseFile
from problem import Problem
from test_operations import TestOperation




# how many test cycles
iterations = 100

# problem params
values_vals = [1, 2, 3, 0.5, 0.2, 0.1, 10, 20, -1, -2, -3, -0.5, -0.2, -0.1, -10, -20]
goal_vals = [-100, -50, 0, 50, 100]
start_vals = [-100, -50, 0, 50, 100]
times_vals = [0.5, 1, 3, 10]
operator_count_range = 25
operators_vals = ['+', '-', '*', '^', '/']
alg = 'genetic'

# alg params
min_op_range = [0, 5]
max_op_range = [25, 50]
mutation_chance_range = [0, 0.10]
crossover_chance_range = [0.55, 1.0]
threshold_range = [0.00, 0.05]
mutation_roles = [1, 0.5, 0.3, 0.2, 0.1, 0]  # delete, add, modify (relative percents) --> 0,0,1 (always modify) 0.33, 0.33, 0.34  | 0.5, 0.2, 0.3

elitism_range = [0, 10]
starting_population_vals = [10, 20, 30, 50, 100, 150, 200, 250]
random_start_p = 0.5
greedy_start_p = 0.5
children_num_vals = [1,2,3,4,5]

def generate_problems():
  problems = []
  for goal in goal_vals:
    for start in start_vals:
      for time in times_vals:
        op_count = random.randint(1, operator_count_range)
        ops = []
        for r in range(op_count):
          val = values_vals[random.randint(0, len(values_vals) - 1)]
          op = operators_vals[random.randint(0, len(operators_vals) - 1)]
          ops.append([op, val])
        problems.append(Problem(alg, start, goal, time, ops))
  return problems

def test(problem, index):
  params = []
  # constants for now
  min_op = 1
  max_op = 30
  mutation_chance = 0.05
  crossover_chance = 0.95
  threshold = 0
  mutation_roles = [0.33, 0.33, 0.34]
  
  #variables
  starting_population = 150
  elitism = 1
  random_start = False
  greedy_start = False
  children_num = 1

  results = []

  #change elitism
  for elitism in range(elitism_range[0], elitism_range[1]):
    params.append([min_op, max_op, elitism, starting_population, mutation_chance, crossover_chance, threshold, True, True, mutation_roles, children_num])  

  for param in params:
    result = main(problem, False, param)
    results.append([result, param])
  save(results, problem, "elitism", index)
  elistism = 1
  params = []
  results = []

  #change starting_population
  for starting_population in starting_population_vals:
    params.append([min_op, max_op, elitism, starting_population, mutation_chance, crossover_chance, threshold, True, True, mutation_roles, children_num])  

  for param in params:
    result = main(problem, False, param)
    results.append([result, param])
  save(results, problem, "starting_population", index)
  starting_population = 150
  params = []
  results = []
    

  #change mutation_chance
  for mutation_chance in linspace(mutation_chance_range[0], mutation_chance_range[1], 5):
    params.append([min_op, max_op, elitism, starting_population, mutation_chance, crossover_chance, threshold, True, True, mutation_roles, children_num])  

  for param in params:
    result = main(problem, False, param)
    results.append([result, param])
  save(results, problem, "mutation_chance", index)
  mutation_chance = 0.05
  params = []
  results = []

  # change the children num
  for children_num in children_num_vals:
    params.append([min_op, max_op, elitism, starting_population, mutation_chance, crossover_chance, threshold, True, True, mutation_roles, children_num])  

  for param in params:
    result = main(problem, False, param)
    results.append([result, param])
  save(results, problem, "children_num", index)
  children_num = 1
  params = []
  results = []

# we're gonna focus on the params not the problem
def save(results, problem, name, index):
  filename = 'results/' + name + str(index) + '.csv'
  target = open(filename, 'w')
  for result_pair in results:
    output = result_pair[0]
    params = result_pair[1]

    for param in output:
      target.write(str(param))
      target.write(',')
    for param in params:
      target.write(str(param))
      target.write(',')
    target.write('\n')
  target.close()

problems = generate_problems()
for p in range(len(problems)):
  test(problems[p], p)
