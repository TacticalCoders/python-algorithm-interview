"""
3번 풀이 조회 구조 개선

2개의 for문을 합쳐서 하나의 for문으로 처리.
"""


def twoSum(self, nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i