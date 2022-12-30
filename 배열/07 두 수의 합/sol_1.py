"""
무차별 대입 방식 브루트 포스
비효율적인 풀이 방법이다.
시간복잡도는 O(n^2)
"""

def twoSum(self, nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]  # 내 풀이와 다른 부분. 빈 리스트를 선언하고 추가할 게 아니라
            # 이렇게 바로 리스트 형태로 반환하는 것이 더 깔끔하다.