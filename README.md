# Problem
Implement a Last In First Out(LIFO) stack object in python

## Operations
1. **is_empty**:  returns whether the stack has less than a one element in it or not
2. **push**: add an element to the top of the stack
3. **pop**: removes and returns the top element on the stack

## Axioms
1. When a stack is first created *is_empty* should returns true
2. after pushing an element to a stack *is_empty* should returns false
3. when the number of pushes is less than or equal the number of pops *is_empty* should returns true
4. using *pop* on an empty stack should returns None
