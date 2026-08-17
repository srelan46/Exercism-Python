def find_fewest_coins(coins, target):
    dp = [float('inf')] * (target + 1)
    chosen = [None] * (target + 1)
    if target<0:
        raise ValueError("target can't be negative")
    dp[0] = 0

    for coin in coins:
        for curr in range(coin, target + 1):
            if dp[curr - coin] + 1 < dp[curr]:
                dp[curr] = dp[curr - coin] + 1
                chosen[curr] = coin

    if dp[target] == float('inf'):
        raise ValueError("can't make target with given coins")

    result = []
    curr = target

    while curr > 0:
        coin = chosen[curr]
        result.append(coin)
        curr -= coin
    result.sort()
    return result