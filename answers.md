# CMPS 2200 Assignment 3
## Answers

**Name:**Charlie Coun


Place all written answers from `assignment-03.md` here for easier grading.

1a) function change(N):
    count = 0
    while N > 0:
        largest_coin = 2**floor(log2(N))
        N -= largest_coin
        count += 1
    return count
