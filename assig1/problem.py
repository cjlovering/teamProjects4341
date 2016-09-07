import types
import operations

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
    self.increasing = operations.categorizeProblem(self.ops)

  # prints the problem details
  def printProblem(self):
    print (self.alg, self.startnum, self.targetnum, self.time, self.ops)

  # evaluates the operation on a given number
  # @param number - the number to be evaluated
  # @param op - the operation to be executed
  def evalOp(self, number, op):
    return operations.buildOperation(number, op[0], op[1])

  # determines if this branch should be cutoff
  # @param current - the current value of the state
  # @return {boolean}
  def cut_off(self, current):
    if self.increasing == None:
      return False
    if current > self.targetnum:
      if self.increasing:
        return True
    elif current < self.targetnum:
      if not self.increasing:
        return True
    return False
