from functools import total_ordering

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

@total_ordering
class Node:
  def __init__(self, cost, data, depth, parent, op):
    self.cost = cost;
    self.data = data;
    self.depth = depth;
    self.parent = parent;
    self.op = op
    self.index = 0
    return

  def __eq__(self, other):
    return ((self.cost, self.data) ==
            (other.cost, other.data))
  def __lt__(self, other):
    return ((self.cost, self.data) <
            (other.cost, other.data))
  def __hash__(self):
    return hash(tuple((self.cost, self.data, self.depth)))

  def printPath(self):
      temp = self
      path = []

      while temp is not None:
        path.append(temp)
        temp = temp.parent

      path.reverse()

      for node in range(len(path)):
        num = path[node].data
        
        if node == len(path) - 1 :
          print(num)
        else:
          op = path[node + 1].op
          print(num, op[0], op[1])

            
