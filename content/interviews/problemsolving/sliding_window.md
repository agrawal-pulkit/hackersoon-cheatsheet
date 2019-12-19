---
title: "Sliding Window"
date: 2019-12-11T11:14:00+05:30
 
weight: 999
---


{{< codecaption lang="python" title="sliding window">}}
def max_sum_window_sliding(l, n, k):
    print(l, n, k)
    current_sum = 0
    if n<k:
        return False
    for i in range(k):
        current_sum += l[i]
    print(current_sum)
    max_sum = current_sum

    for i in range(n-k):
        print(l[k+i],l[i])
        current_sum = current_sum + l[k+i]-l[i]
        print(current_sum)
        if max_sum < current_sum:
            max_sum = current_sum

    return max_sum

max_sum_value = max_sum_window_sliding([1, 4, 2, 10, 23, 3, 1, 0, 20], 9, 4)
print(max_sum_value)

{{< /codecaption >}}