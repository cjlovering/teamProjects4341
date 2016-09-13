import unittest
from iterative import solve
from problem import Problem

class TestIterative(unittest.TestCase):
  def _test_iterative(self, problem, result):
    sol = solve(problem)
    sol[5].print_path()
    self.assertEqual(sol[0], result[0])
    self.assertEqual(sol[1], result[1])
  def test_iterative(self):
    # choose best path not first path
    p = Problem('iterative', 5, 10, 10, [('+', 1),('+', 5)])
    r = (10, 1)
    TestIterative._test_iterative(self, p, r)
    # choose a path that works
    p1 = Problem('iterative', 5, 10, 10, [('+', 1),('*', 3)])
    r1 = (10, 5)
    TestIterative._test_iterative(self, p1, r1)

if __name__ == '__main__':
  unittest.main();
