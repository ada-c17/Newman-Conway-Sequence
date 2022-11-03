# Dynamic Programming

Dynamic programming is a strategy for developing an algorithm where each subproblem is solved and the results recorded for use in solving larger problems.  In this exercise you will write a pair of dynamic programming methods.

## Newman-Conway Sequence

[Newman-Conway sequence](https://www.geeksforgeeks.org/newman-conway-sequence/) is the one which generates the following integer sequence.  1 1 2 2 3 4 4 4 5 6 7 7….. and follows below recursive formula.

```
P(1) = 1
P(2) = 1
for all n > 2
P(n) = P(P(n - 1)) + P(n - P(n - 1))
```

Note: if the input is 0 or less, a ValueError is raised.

Given a number n then print n terms of Newman-Conway Sequence

Examples:

```
Input : 0
Output: ValueError

Input : 1
Output: 1

Input : 2
Output : 1 1

Input : 4
Output : 1 1 2 2

Input : 13
Output : 1 1 2 2 3 4 4 4 5 6 7 7 8

Input : 20
Output : 1 1 2 2 3 4 4 4 5 6 7 7 8 8 8 8 9 10 11 12
```

You should be able to do this in O(n) time complexity.



## Resources

- [GeeksforGeeks: Newman-Conway Sequence](https://www.geeksforgeeks.org/newman-conway-sequence/)
