import types
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

  def printProblem(self): 
    print (self.alg, self.startnum, self.targetnum, self.time, self.ops)
    
  def evalOperation(self, number, op):
    return buildOperation(number, op[0], op[1])


def buildOperation(init, stringOperator, operand):
  if stringOperator == '+':
    return init + operand
  if stringOperator == '-':
    return init - operand
  if stringOperator == '/':
    return init / operand
  if stringOperator == '*':
    return init * operand
  if stringOperator == '^':
    return math.pow(init, operand)
  if stringOperator == '!':
    return math.factorial(init)
  print("did not find operator: %r" % stringOperator)
  
