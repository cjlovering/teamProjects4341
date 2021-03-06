import unittest
from operations import categorize_operation
from operations import categorize_problem
from operations import eval_operation

class TestOperation(unittest.TestCase):
  def _test_categorize_operation(self, operator, operand, result):
    self.assertEqual(categorize_operation(operator, operand), result)
  def _test_categorize_problem(self, ops, result):
    self.assertEqual(categorize_problem(ops), result)
  def _test_eval_operation(self, initial, operator, operand, result):
    self.assertEqual(eval_operation(initial, operator, operand), result)
  def test_categorize_operations(self):
    TestOperation._test_categorize_operation(self, '+', 5, True)
    TestOperation._test_categorize_operation(self, '+', -5, False)
    TestOperation._test_categorize_operation(self, '-', 5, False)
    TestOperation._test_categorize_operation(self, '-', -5, True)
    TestOperation._test_categorize_operation(self, '*', 5, True)
    TestOperation._test_categorize_operation(self, '*', -5, False)
    TestOperation._test_categorize_operation(self, '*', 0.5, False)
    TestOperation._test_categorize_operation(self, '*', -0.5, None)
    TestOperation._test_categorize_operation(self, '/', 5, False)
    TestOperation._test_categorize_operation(self, '/', 0.1, True)
    TestOperation._test_categorize_operation(self, '/', -0.1, None)
    TestOperation._test_categorize_operation(self, '^', 0.1, False)
    TestOperation._test_categorize_operation(self, '^', 5, True)
    TestOperation._test_categorize_operation(self, '^', 0, False)
  def test_categorize_problem(self):
    TestOperation._test_categorize_problem(self, [['+', 4],['-', 3]], None)
  def test_evaluate_operation(self):
    TestOperation._test_eval_operation(self, 6, '+', 4, 10)

if __name__ == '__main__':
  unittest.main();
