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

2a) The algorithm does not give the optimal number of coins when coins = [1, 4, 5] and n = 8. You take out the largest coin (n) and are left with 3, for which you need three 1 coins. The optimal solution would have been two 4 coins, but you instead used four coins.

2b) If min coins is the minimum amount of coins needed to make change, then minCoins(n) = {0 if n = 0, min_(di<n){1 + minCoins(n - di)} if n >0}. This is optimal since if we choose coin di first, the remaining amount is n - di. The optimal solution for n must include n - di for some di, so the problem can be broken into smaller subproblems, and their solutions can be reused.

### 2c) def min_coins(d, n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0 

    for i in range(1, n + 1):
        for coin in d:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[n] if dp[n] != float('inf') else -1
The work would be W(n) = O(nk) where k = the number of denominations and span would be S(n) = O(n)
