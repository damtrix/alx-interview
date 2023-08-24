#!/usr/bin/python3
"""
Interview Question on: fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    """ fewest number of coins needed to meet total """
    if total <= 0:
        return 0
    # sort the coins in descending order
    coins.sort(reverse=True)
    remains = 0
    for coin in coins:
        if total <= 0:
            break
        store = total // coin
        remains += store
        total -= (store * coin)
    if total != 0:
        return -1
    return remains
