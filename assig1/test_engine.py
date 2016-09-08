from main import main
from parser import parseFile
from os import listdir
from os.path import isfile, join
import re
from problem import Problem

testfiles = [f for f in listdir("./tests") if isfile(join("./tests", f))]

solutions = []

for file in testfiles:
  if re.match('test', file) is not None:
    solutions.append(main(parseFile("tests/" + file), False))

for fi in range(0, len(testfiles), 2):
  print(solutions[fi], solutions[fi+1])
