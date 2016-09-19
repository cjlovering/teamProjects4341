## assig2

### usage:
general:
```
  python3 main.py -i <inputfile>
```
test:
```
  mkdir results
  python3 test_engine.py
```

The 'test_engine.py' file will run a significant number of generated tests. 
The files 'test_greedy.py', 'test_iterative.py', 'test_operations.py',
and 'test_parser.py' are unittests for their corresponding files. Run them
by executing:

```
  python3 test_******.py
```

### tasks:
- [x] float operators & math
- [x] diverse start
	- [x] random length
	- [x] 50/50 random or greedy starting position 
- [x] consider length of solutions (30 max)
- [x] crossover for diff lengths
- [x] mutation: modify, delete, add ops
- [x] extensive testing
  - [x] test engine
- [x] tune parameters
