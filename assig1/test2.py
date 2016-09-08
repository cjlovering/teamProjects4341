from functools import total_ordering

try:
    import Queue as Q  # ver. < 3.0                                                                                                            
except ImportError:
    import queue as Q

@total_ordering
class Rock:
    def __init__(self, priority, description):
        self.lastname = priority
        self.firstname = description
        return

    def __eq__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))

@total_ordering
class Rode:
  def __init__(self, cost, data, depth, parent, op):
    self.cost = cost;
    self.data = data;
    self.depth = depth;
    self.parent = parent;
    self.op = op
    return

    def __lt__(self, other):
      return ((self.cost, self.data) < (other.cost, other.data));

    def __eq__(self, other):
      return ((self.cost, self.data) == (other.cost, other.data));
    
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
  
  # h cost, data, depth, last node, val, operation                                                                                              #  current = (heuristic(problem.startnum, problem.targetnum), problem.startnum, 0, None, problem.startnum, None)
     
if __name__=='__main__':
  q = Q.PriorityQueue()

  q.put(Rock('b', 'Proficient'))
  q.put(Rock('a', 'Expert'))
  q.put(Rock('c', 'Novice'))

  while not q.empty():
      next_level = q.get()
      print("Processing level:", next_level.lastname)
