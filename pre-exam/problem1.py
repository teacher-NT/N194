def sum_unique(nums: list) -> int:
    res = 0
    for i in nums:
        if nums.count(i) == 1:
            res += i
    return res
# Testlar:
print(sum_unique([1, 2, 3, 2, 1, 4]))
# Output: 7
# Izoh: 3 + 4 = 7
print(sum_unique([5, 5, 5]))
# Output: 0
print(sum_unique([10, 20, 30]))
# Output: 60
print(sum_unique([]))
# Output: 0