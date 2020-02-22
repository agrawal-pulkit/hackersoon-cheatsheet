---
title: "Buy and Sell Stock once"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---

{{< codecaption lang="python" title="Buy and Sell Stock once" >}}

"""

This problem is concerned with the problem of optimally buying and selling a stock once, as described on Page 2. As an example, consider the following sequence of stock prices:
The maximum profit that can be made with one buy and one sell is 30-buy at 260 and sell at 290. Note that 250 is not the lowest price, nor 290 the
<31.0,31.5,275,295,260,270,290,230,255,250>.
highest price.
This solution is based on two assumption.
1. max profit 
2. min price so far 
"""
def buy_and_sell_stock_once(arr):
    max_profit, min_price_so_far = 0, float('inf')

    for price in arr:
        max_profit_sell_today = price - min_price_so_far
        max_profit = max(max_profit, max_profit_sell_today)
        min_price_so_far = min(min_price_so_far, price)
    
    return max_profit

arr = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
result = buy_and_sell_stock_once(arr)
print("result: ", result)


"""
We can also solve this problem using maximum sum sub-array method.
which is an example of kadane's algorithm.
Largest Sum Contiguous Subarray.
"""
def kadanes_algo(arr):

    max_so_far, max_ending_here = 0, 0

    for i in range(len(arr)):
        max_ending_here += arr[i]

        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here

    return max_so_far

def buy_and_sell_stock(arr):
    for i in range(len(arr)-1):
        arr[i] = arr[i+1] - arr[i]
    max_profit = kadanes_algo(arr[:-1])
    return max_profit

arr = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
result = buy_and_sell_stock(arr)
print("using kadane's Algo result: ", result)

{{< /codecaption >}}