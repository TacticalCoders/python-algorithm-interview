"""
첫 번째 수를 뺀 결과 키 조회
비교나 탐색 대신 한 번에 정답을 찾을 수 있는 방법
"""


def twoSum(self, nums, target):
    nums_map = {}

    for i, num in enumerate(nums):
        nums_map[num] = i  # 숫자와 인덱스를 매핑

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


"""
2번 풀이와 아이디어는 같지만 딕셔너리는 해시 테이블로 구성되어 조회가 훨씬 빠르다(평균적으로 O(1))
"""
