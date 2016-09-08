import unittest
from operations import categorize_operation
from operations import categorize_problem
from operations import eval_operation


class TestOperator(unittest.TestCase):
  def _test_categorize_operation(self, operator, operand, result):
    self.assertEqual(categorize_operation(operator, operand), result)
  def _test_categorize_problem(self, ops, result):
    self.assertEqual(categorize_problem(ops), result)
  def test_categorize_operations(self):
    TestOperator._test_categorize_operation(self, '+', 5, True)
    TestOperator._test_categorize_operation(self, '+', -5, False)
    TestOperator._test_categorize_operation(self, '-', 5, False)
    TestOperator._test_categorize_operation(self, '-', -5, True)
    TestOperator._test_categorize_operation(self, '*', 5, True)
    TestOperator._test_categorize_operation(self, '*', -5, False)
    TestOperator._test_categorize_operation(self, '*', 0.5, False)
    TestOperator._test_categorize_operation(self, '*', -0.5, None)
    TestOperator._test_categorize_operation(self, '/', 5, False)
    TestOperator._test_categorize_operation(self, '/', 0.1, True)
    TestOperator._test_categorize_operation(self, '/', -0.1, None)
    TestOperator._test_categorize_operation(self, '^', 0.1, False)
    TestOperator._test_categorize_operation(self, '^', 5, True)
    TestOperator._test_categorize_operation(self, '^', 0, False)

if __name__ == '__main__':
  unittest.main();