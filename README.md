# Organization of Programming Languages

Python scripts written for CS3342 assignments at Western Univeristy

## Assignment 1

---

Script (`comm_rm.py`) to remove comments from C++ file

### Usage

- Open help menu

  ```bash
  python comm_rm.py -h
  ```

- Remove comments from file a.cpp and save as a_clean.cpp

  ```bash
  python comm_rm.py a.cpp a_clean.cpp
  ```

### Errors

Program will throw error if the input/output files are not C++ extension files

## Assignment 2

---

Script(`balance.py`) computes the minimum number of edit operations to balance a string

> A string consisting only of parentheses, `(` and `)` is called balanced if its parentheses can be properly matched: each open parenthesis, `(`, with a following closed parenthesis, `)`.

> The program outputs
>
> 1. the smallest edit distance, `d`, between the input string and a balanced string
> 2. a balanced string at edit distance `d` from the input.

### Example

1. `python balance.py "(()())()"`  
   outputs d = 0, balanced string: "(()())()"

2. `python balance.py "))()))"`  
   outputs: d = 2, balanced string: "()()()"
