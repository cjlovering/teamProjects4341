## assig2

### usage:
general:
```
  python3 main.py -i <inputfile>
```
test:
```
  python3 test_engine.py
```

The 'test_engine.py' file will run all the tests in the folder '/tests'.
The files 'test_greedy.py', 'test_iterative.py', 'test_operations.py',
and 'test_parser.py' are unittests for their corresponding files. Run them
by executing:

```
  python3 test_******.py
```

### tasks:
- [ ] float operators & math
- [ ] diverse start
	- [ ] random length
	- [ ] 50/50 random or greedy starting position (?)
- [ ] consider length of solutions (30 max)
- [ ] crossover for diff lengths
- [ ] mutation: modify, delete, add ops