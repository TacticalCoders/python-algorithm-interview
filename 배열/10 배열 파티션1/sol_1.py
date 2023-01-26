"""
n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수 출력.

입력
[1, 4, 3, 2]
출력
4
min(1,2) + min(3,4) = 4

오름차순 풀이
min이 최대여야 합도 최대.
min이 최대가 되려면 오름차순 정렬 sort()하여 차례대로 입력
"""


def arrayPairSum(self, nums):
    sum = 0
    pair = []
    nums.sort()

    for n in nums:
        # 앞에서 부터 오름차순으로 페어를 만들어 합 계산
        pair.append(n)
        if len(pair) == 2:
            sum += min(pair)
            pair = []

    return sum
