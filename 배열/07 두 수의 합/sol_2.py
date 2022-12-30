"""
in을 이용한 탐색
모든 조합을 비교하지 않고,
타겟에서 첫 번째 값을 뺀 target - n이 존재하는지 탐색

내부 함수로 구현된 in은 매번 값을 비교하는 것에 비해 훨씬 빠르다.
"""


def twoSum(self, nums, target):
    for i, n in enumerate(nums): # 1번 풀이와 달리 for 문을 한 번만 사용했다.
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]
