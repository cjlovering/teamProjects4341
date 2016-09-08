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
    return hash(tuple(self))
 
  def printPath(self):
      temp = self
      path = []

      while temp is not None:
        path.append(temp)
        temp = temp.parent

      path.reverse()

      for node in path:
        num = node.data
        op = node.op
        if not op == None:
          print(num, op[0], op[1])
        else:
          print(num)
  
q = Q.PriorityQueue()

q.put(Node('b', 'Proficient',1,2,3))
q.put(Node('a', 'Expert',1,2,3))
q.put(Node('c', 'Novice',2,3,4))

while not q.empty():
    next_level = q.get()
    print("Processing level:", next_level.data)


