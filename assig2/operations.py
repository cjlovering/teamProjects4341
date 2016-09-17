import math

# @return - True if increasing, False if decreasing, None if unchanging or neither
def categorize_operation(stringOperator, operand):
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
      return None
    elif operand > 0 and operand < 1:
      return True
    elif operand > 0:
      return False
    elif operand == 0:
      return None  # should we generally guard against this
  if stringOperator == '*':
    if operand > 0 and operand < 1:
      return False
    if operand > 0:
      return True
    elif operand < 0 and operand > -1:
      return None
    elif operand < 0:
      return False
    elif operand == 0:
      return False  # effectively decreasing the val
  if stringOperator == '^':
    if operand > 0 and operand < 1:
      return False
    elif operand > 0:
      return True
    elif operand < 0 and operand > -1:
      return None
    elif operand == 0 or operand == 1:
      return False   #effectively decreasing the val
  if stringOperator == '!':
    return True #well only if negative, but for now
  print("did not find operator: %r" % stringOperator)

# @return - True if increasing, False if decreasing
def categorize_problem(ops):
  inc = True
  for op in ops:
    inc = inc and categorize_operation(op[0], op[1])
    if not inc:
      break; #early escape
  if inc:
    return True
  dec = True
  for op in ops:
    dec = dec and not categorize_operation(op[0], op[1])
    if inc:
      break; #early escape
  if dec:
    return True
  return None  #its not inc or dec

# executes the calculation
# @return - the value of the operator applied to the init value and the operand
def eval_operation(init, stringOperator, operand):
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

# precalculates the sub target operations
# @param target - the number target
# @param ops - the operations
# @return - the sub targets
def calculate_subtargets(target, ops):
  sub_targets = []
  for op in ops:
    if op[0] == '+':
      sub_targets.append(target - op[1])
    if op[0] == '-':
      sub_targets.append(target + op[1])
    if op[0] == '/':
      sub_targets.append(target * op[1])
    if op[0] == '*':
      sub_targets.append(target / op[1])

  return sub_targets
