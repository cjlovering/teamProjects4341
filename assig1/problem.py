#class to bundle problem parameters
class Problem:
  def __init__(self, alg, startnum, targetnum, time, ops):
    self.alg = alg
    self.startnum = startnum
    self.targetnum = targetnum
    self.time = time
    self.ops = ops

  def printProblem(self):
    print (self.alg, self.startnum, self.targetnum, self.time, self.ops)
