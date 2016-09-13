import types
import operations
import math

#class to bundle problem parameters
class Problem:
  def __init__(self, alg, startnum, targetnum, time, ops):
    NumberTypes = (int, float)
    assert isinstance(alg, str), "alg is not an string: %r" % alg
    assert isinstance(startnum, NumberTypes), "startnum is not a number: %r" % startnum
    assert isinstance(targetnum, NumberTypes), "targetnum is not a number: %r" % targetnum
    assert isinstance(time, NumberTypes), "time is not a number: %r" % time
    for op in ops:
      assert isinstance(op[0], str), "operator is not a string: %r" % op[0]
      try:
        assert isinstance(op[1], NumberTypes), "operand is not a number: %r" % op[1]
      except:
        print("operand is not a number: %r" % op[1])

    self.alg = alg
    self.startnum = startnum
    self.targetnum = targetnum
    self.time = time
    self.ops = ops
    self.increasing = operations.categorize_problem(self.ops)
    self.sub_targets = operations.calculate_subtargets(self.targetnum, self.ops)

  def __str__(self):
    return ""
  # prints the problem details
  def printProblem(self):
    print (self.alg, self.startnum, self.targetnum, self.time, self.ops)

  # evaluates the operation on a given number
  # @param number - the number to be evaluated
  # @param op - the operation to be executed
  def evalOp(self, number, op):
    return math.floor(operations.eval_operation(number, op[0], op[1]))

  # determines if this branch should be cutoff
  # @param {number} current - the current value of the state
  # @return {boolean}
  def cut_off(self, current):
    if self.increasing == None:
      return False
    if current > self.targetnum:
      print(current)
      if self.increasing:
        return True
    elif current < self.targetnum:
      if not self.increasing:
        return True
    return False
