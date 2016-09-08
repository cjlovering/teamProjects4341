import re
import unittest
from os import listdir
from os.path import isfile, join

from main import main
from parser import parseFile
from problem import Problem
from test_operations import TestOperation

# all the test files in /tests
testfiles = [f for f in listdir("./tests") if isfile(join("./tests", f))]

# solutions to problems
solutions = []

# display for a solution
def printSolution(s):
  print("alg: ", s[0][0:6], "error: ", s[1], "result: ", s[2], "steps: ", s[3], "time: ", s[4],"nodes: ", s[5],  "max depth: ", s[6], "branching f: ", len(s[7].ops))

for file in testfiles:
  if re.match('test', file) is not None:
    solutions.append(main(parseFile("tests/" + file), False))

for fi in range(0, len(testfiles), 2):
  printSolution(solutions[fi])
  printSolution(solutions[fi+1])
  print("----------------------------------------")
