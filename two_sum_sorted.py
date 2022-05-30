from typing import List

"""
TESTS

t1 = [2,3,4,5,8,11,18], 8



"""
t1 = [
    [2,3,4,5,8,11,18],
    8
]

def twoSumSorted(arr: List[int], target: int) -> List[int]:
    l, r = 0, len(arr) - 1

    while l < r:
        s = arr[l] + arr[r]
        if s == target:
            return [l, r]
        if s < target:
            l += 1
        else:
            r -= 1

    return []
        

print(twoSumSorted(t1[0], t1[1]))