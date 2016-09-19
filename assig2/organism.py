import random
from heuristics import heuristic
from problem import Problem

class Organism:
  # constructor
  def __init__(self, op_seq):
    self.op_seq = op_seq
    self.data = None
    self.cost = None
    self.fitness = None
    self.invalid = False
    return

  # sets a percentage to survive...
  # @param {Problem} problem - the problem we are trying to solve
  def set_data(self, problem):
    val = problem.startnum

    # figure out the value of doing all the sequences
    for op in self.op_seq:
      try:
        val = problem.eval_op(val, op)
      except:
        self.invalid = True
        break
    self.data = val

  # print seq in a formatted manner with correct values
  # @param {Number} start - the starting number
  # @param {Problem} problem - the problem we are trying to solve
  def print_seq(self, start, problem):
    val = start

    for op in range(len(self.op_seq)):
      num = problem.eval_op(val, self.op_seq[op])

      if op == len(self.op_seq):
        print(num)
      else:
        print(val, self.op_seq[op][0], self.op_seq[op][1], '=', num)
      val = num

  # sets the cost to survive...
  def calculate_cost(self, problem):
    self.cost = heuristic(self.data, problem);

  # sets a percentage to survive...
  # @param {number} fitness - the % to be chosen for a pair
  def set_fitness(self, fitness):
    self.fitness = fitness;

  # crosses over with another organism
  # @param {Organism} other_org - the other parent
  # @return - the child
  def crossover(self, other_org):
    #calc the new_ops
    new_ops = []
    child = Organism(new_ops)
    r = random.randint(0, min(len(self.op_seq), len(other_org.op_seq)))

    return Organism(self.op_seq[r:]+other_org.op_seq[:r])

  # mutates the org
  # @param {Array} mut_index - the relative probablities of add/del/mod
  # @param {Problem} problem - the problem we are trying to solve
  def mutate(self, mut_index, problem):
    r = random.uniform(0, 1)
    rand_index = random.randint(0, len(self.op_seq) - 1)
    if (r < mut_index[0]):
      #delete
      self.op_seq.pop(rand_index)
    elif (r < mut_index[0] + mut_index[1]):
      #add
      self.op_seq.append(problem.ops[random.randint(0, len(problem.ops) - 1)])
    else:
      #modify
      self.op_seq[rand_index] = problem.ops[random.randint(0, len(problem.ops) - 1)]
    return self
