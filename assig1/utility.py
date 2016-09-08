from heuristics import abs_difference

# @return - if we reached the goal
def goal_test(result, target):
  return (float(result)) == (float(target))

# idea: probably use the same set of heuristics to det answer
# @return true if the new val is closer than the old val
def closer(old, new, target):
    return abs_difference(new, target) < abs_difference(old, target)
