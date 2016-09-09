import unittest
from parser import parseCommandLine
from parser import parseFile
from parser import num
from problem import Problem

class TestParser(unittest.TestCase):
  def _test_parse_command_line(self, argv, result):
    self.assertEqual(parseCommandLine(argv), result)
  def _test_parse_file(self, inputfile, result):
    self.assertEqual(parseFile(inputfile).alg, result.alg)
    self.assertEqual(parseFile(inputfile).startnum, result.startnum)
    self.assertEqual(parseFile(inputfile).targetnum, result.targetnum)
    self.assertEqual(parseFile(inputfile).time, result.time)
    self.assertEqual(parseFile(inputfile).ops, result.ops)
  def _test_num(self, s, result):
    self.assertEqual(num(s), result)

  def test_parse_command_line(self):
    TestParser._test_parse_command_line(self, ['-i', 'tests/test01'], "tests/test01")
  def test_parse_file(self):
    ops = [('+', 3), ('-', 1), ('/', 2), ('*', 5), ('^', 2)]
    result =  Problem( "greedy", 4, 11, 0.2, ops )
    TestParser._test_parse_file(self, "tests/test01", result)
  def test_num(self):
    TestParser._test_num(self, 11.0344, 11)
    TestParser._test_num(self, 2**63, 2**63)
    TestParser._test_num(self, -9., -9)
    TestParser._test_num(self, ~100, -101)
    TestParser._test_num(self, 1|3, 3)

if __name__ == '__main__':
  unittest.main();
