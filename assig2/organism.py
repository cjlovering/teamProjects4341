from functools import total_ordering
from heuristic import heuristic

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

@total_ordering
class Organism:
  # constructor
  def __init__(self, opSeq):
    self.opSeq = opSeq
    self.data = None
    self.cost = None
    self.fitness = None
    return

  # define internal functions to order nodes in a priority queue
  def __eq__(self, other):
    return ((self.cost, self.data) ==
            (other.cost, other.data))
  def __lt__(self, other):
    return ((self.cost, self.data) <
            (other.cost, other.data))
  def __hash__(self):
    return hash(tuple((self.cost, self.data, self.depth)))
  def __str__(self):
    return  str(self.data) + " " + str(self.op)

  # sets a percentage to survive...
  def setData(opSeq, problem):
    val = problem.startnum

    # figure out the value of doing all the sequences
    for op in opSeq:
      val = problem.evalOp(val, op)

    self.data = val

  # sets the cost to survive...
  def setCost():
    self.cost = heuristic(self.data);

  # sets a percentage to survive...
  # @param {number} fitness - the % to be chosen for a pair
  def setFitness(fitness):
    self.fitness = fitness;

  def crossOver(otherOrganism):
    #do the cross over
    return

  def mutate():
    #mutate
    return
