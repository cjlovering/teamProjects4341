import random
from heuristics import heuristic

class Organism:
  # constructor
  def __init__(self, op_seq):
    self.op_seq = op_seq
    self.data = None
    self.cost = None
    self.fitness = None
    return

  # sets a percentage to survive...
  def set_data(self, problem):
    val = problem.startnum

    # figure out the value of doing all the sequences
    for op in self.op_seq:
      print("Val: %r" % val)
      print(op)
      val = problem.eval_op(val, op)

    self.data = val

  # sets the cost to survive...
  def calculate_cost(self, problem):
    self.cost = heuristic(self.data, problem);

  # sets a percentage to survive...
  # @param {number} fitness - the % to be chosen for a pair
  def set_fitness(self, fitness):
    self.fitness = fitness;

  def crossover(self, other_org):
    #calc the new_ops
    new_ops = []
    child = Organism(new_ops)
    r = random.randint(0, len(self.op_seq))

    return Organism(self.op_seq[:r]+other_org.op_seq[r:])

  def mutate(self):
    #mutate
    return self
