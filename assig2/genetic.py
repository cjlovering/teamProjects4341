from problem import Problem
from node import Node
import time
import math
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

  population = []
  while True: # we exit due to time below
    cut_off(population, start_time, problem.time)
    new_population = []
    for i in range(len(population)):
      x = random_selection(population, fitness);
      y = random_selection(population, fitness);
      child = x.crossover(y)
      if small_random_chance():
        child = mutate(child)
    cull(population)
    population = new_population

  return (best.data, best.depth, time.time()-start_time, node_count, depth, best)

  def random_selection(population, fitness):
    for org in population:
       # consider

  def cut_off(population, start_time, end_time):
    if time.time()-start_time > end_time - 0.001:
      return True
    found = False
    for org in population:
      #found =  org.data

    return found

  def small_random_chance():
    #random > variable
    return false

  def cull(population):
    return population
