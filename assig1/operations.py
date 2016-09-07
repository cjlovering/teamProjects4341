import math

# @return - True if increasing, False if decreasing, None if unchanging or neither
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
      return False  # should we generally guard against this
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

# @return - True if increasing, False if decreasing
def categorizeProblem(ops):
  inc = True
  for op in ops:
    inc = inc and categorizeOperation(op[0], op[1])
    if not inc:
      break; #early escape
  if inc:
    return True
  dec = True
  for op in ops:
    dec = dec and not categorizeOperation(op[0], op[1])
    if inc:
      break; #early escape
  if dec:
    return True
  return None  #its not inc or dec

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
