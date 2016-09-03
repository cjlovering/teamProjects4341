#!/usr/bin/python

import sys, getopt
from problem import Problem

#usage: python Parser.py -i tests/<filename>
def parse(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   testfile = open(inputfile, "r")
   alg = testfile.readline().strip(' \t\n\r')
   startnum = testfile.readline().strip(' \t\n\r')
   endnum = testfile.readline().strip(' \t\n\r')
   time = testfile.readline().strip(' \t\n\r')
   tempOps = testfile.read().split()
   ops = []
   for index in range(0, len(tempOps), 2):
     ops.append({tempOps[index], tempOps[index+1]})

   problem = Problem( alg, startnum, endnum, time, ops )
   return problem

if __name__ == "__main__":
   parse(sys.argv[1:])
