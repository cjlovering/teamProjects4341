import unittest
from greedy import solve
from problem import Problem

class TestGreedy(unittest.TestCase):
  def _test_greedy(self, problem, result):
    sol = solve(problem)
    sol[5].print_path()
    self.assertEqual(sol[0], result[0])
    self.assertEqual(sol[1], result[1])
  def test_greedy(self):
    # choose best path not first path
    p = Problem('greedy', 5, 10, 10, [('+', 1),('+', 5)])
    r = (10, 1)
    TestGreedy._test_greedy(self, p, r)
    # choose a path that works
    p1 = Problem('greedy', 5, 10, 10, [('+', 1),('*', 3)])
    r1 = (10, 5)
    TestGreedy._test_greedy(self, p1, r1)

if __name__ == '__main__':
  unittest.main();
