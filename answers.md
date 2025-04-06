# CMPS 2200 Assignment 3
## Answers

**Name:** Charlie Coun


Place all written answers from `assignment-03.md` here for easier grading.

### 1a) function change(n):
    count = 0
    while n > 0:
        largest_coin = 2**floor(log2(n))
        n -= largest_coin
        count += 1
    return count

1b) Optimal substructure: The remaining amount, N - largest coin, will be solved in the same way and will be optimal and independent.
Greedy choice: The largest coin is always included in some optimal solution since we always pick a coin that corresponds to the largest bit still set in the binary representation.

1c) W(n) = O(logn) since the loop runs at a worst case log2n times for each of the sets in n.
S(N) = O(logn) since the algorithm is sequential so span = work

