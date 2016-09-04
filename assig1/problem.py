from types import *
import types

#class to bundle problem parameters
class Problem:
  def __init__(self, alg, startnum, targetnum, time, ops):
    NumberTypes = (int, float)
    assert isinstance(alg, str), "alg is not an string: %r" % alg
    assert isinstance(startnum, NumberTypes), "startnum is not a integer: %r" % startnum
    assert isinstance(targetnum, NumberTypes), "targetnum is not a integer: %r" % targetnum
    assert isinstance(time, NumberTypes), "time is not a integer: %r" % time
    for op in ops:
      assert isinstance(op[0], str), "operator is not a string: %r" % op[0]
      assert isinstance(op[1], NumberTypes), "operand is not a integer: %r" % op[1]


    self.alg = alg
    self.startnum = startnum
    self.targetnum = targetnum
    self.time = time
    self.ops = ops

  def printProblem(self): 
    print (self.alg, self.startnum, self.targetnum, self.time, self.ops)
