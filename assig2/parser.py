#!/usr/bin/python
import sys, getopt
from problem import Problem

#usage: python Parser.py -i tests/<filename>
# @param argv - commandline arguments
# @return - name of the input file
def parseCommandLine(argv):
   inputfile = ''
   outputfile = ''
   try:
     opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
     print('test.py -i <inputfile>')
     sys.exit(2)
   for opt, arg in opts:
     if opt == '-h':
       print('test.py -i <inputfile>')
       sys.exit()
     elif opt in ("-i", "--ifile"):
       inputfile = arg
     elif opt in ("-o", "--ofile"):
       outputfile = arg
   return inputfile

# @param inputfile - name of the input file
# @return - problem details
def parseFile(inputfile):
   testfile = open(inputfile, "r")
   alg = testfile.readline().strip(' \t\n\r')
   startnum = num(testfile.readline().strip(' \t\n\r'))
   endnum = num(testfile.readline().strip(' \t\n\r'))
   time = num(testfile.readline().strip(' \t\n\r'))
   tempOps = testfile.read().lstrip().rstrip().split()
   ops = []
   for index in range(0, len(tempOps), 2):
     ops.append((tempOps[index], num(tempOps[index+1])))
   testfile.close()
   problem = Problem( alg, startnum, endnum, time, ops )
   return problem

# @param s - number to be converted
# @return - appropriately converted number
def num(s):
  try:
    return int(s)
  except ValueError:
    return float(s)

if __name__ == "__main__":
   parse(sys.argv[1:])
