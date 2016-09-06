import types
import math

Zero = 'zero'

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

  # prints the problem details
  def printProblem(self): 
    print (self.alg, self.startnum, self.targetnum, self.time, self.ops)
    
  # evaluates the operation on a given number
  # @param number - the number to be evaluated
  # @param op - the operation to be executed
  def evalOp(self, number, op):
    return buildOperation(number, op[0], op[1])

  # determines if this branch should be cutoff
  # @param current - the current value of the state
  # @return {boolean}
  def cut_off(self, current):
    if current > self.targetnum:
      inc = True
      for op in self.ops:
        inc = inc and categorizeOperation(op[0], op[1])
      if inc:
        return True
    elif current < self.targetnum:
      for op in self.ops:
        if categorizeOperation(op[0], op[1]):
          return False
      return True

# @return - True if increasing, False if decreasing, Zero if unchanging
def categorizeOperation(stringOperator, operand):
  if stringOperator == '+':
    if operand > 0:
      return True
    elif operand < 0:
      return False
    elif operand == 0:
      return True  # can't be decreased
  if stringOperator == '-':
    if operand < 0:
      return True
    elif operand > 0:
      return False
    elif operand == 0:
      return True  # can't be decreased
  if stringOperator == '/':
    if operand < 0:
      return True
    elif operand > 0:
      return False
    elif operand == 0:
      return Zero  # should we generally guard against this
  if stringOperator == '*':
    if operand > 0:
      return True
    elif operand < 0:
      return False
    elif operand == 0:
      return False  # effectively decreasing the val
  if stringOperator == '^':
    if operand > 0:
      return True
    elif operand < 0:
      return False
    elif operand == 0:
      return False   #effectively decreasing the val
  if stringOperator == '!':
    return True

  print("did not find operator: %r" % stringOperator)

# executes the calculation
# @return - the value of the operator applied to the init value and the operand
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
  
