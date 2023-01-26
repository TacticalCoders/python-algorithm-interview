"""
sol_1에서 두 개씩 min에 입력하여 계산하는데 매우 비효율적,
그냥 짝수 번째 원소끼리 더하면 됨.
"""


def arrayPairSum(self, nums):
    sum = 0
    nums.sort()

    for i, n in enumerate(nums):
        if i % 2 == 0:
            sum += n

    return sum
