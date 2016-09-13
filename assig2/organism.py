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
  def setData(self, problem):
    val = problem.startnum

    # figure out the value of doing all the sequences
    for op in self.op_seq:
      val = problem.eval_op(val, op)

    self.data = val

  # sets the cost to survive...
  def setCost(self):
    self.cost = heuristic(self.data);

  # sets a percentage to survive...
  # @param {number} fitness - the % to be chosen for a pair
  def setFitness(self, fitness):
    self.fitness = fitness;

  def crossover(self, otherOrganism):
    #calc the new_ops
    new_ops = []
    child = Organism(new_ops)
    #do the cross over
    return

  def mutate(self):
    #mutate
    return
