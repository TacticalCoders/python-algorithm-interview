"""
투 포인터를 이용한 방법
왼쪽 포인터와 오른쪽 포인터의 합이 크다면 오른쪽 포인터를 왼쪽으로,
작다면 왼쪽 포인터를 오른쪽으로 옮기는 방식
다만 이 풀이는 먼저 오름차순 정렬이 되어야 하기에 인덱스가 변경되므로 오답이다.
만약 인덱스가 아니라 값을 찾는 문제에서는 적용할 수 있을 것이다.
"""


def twoSum(self, nums, target):
    nums.sort()
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]