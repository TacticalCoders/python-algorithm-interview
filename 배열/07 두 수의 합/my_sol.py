"""
리트코드 1번
덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.
입력
nums = [2, 7, 11, 15], target = 9
출력 = [ 0, 1 ]
"""


# 두 수이므로 비교적 간단.
# 배열을 어떻게 순회할 것인가.
# 확인해야 하는 경우는 4개에서 2개를 선택하는 4C2, 즉 6개의 경우만 체크하면 된다.
# 2 -> 7,11,15
# 7 -> 11, 15
# 11 -> 15

def two_sum(nums, target):
    index = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                index.append(i)
                index.append(j)
    return index


nums = [2, 7, 11, 15]
target = 9

print(two_sum(nums, target))
# 이렇게 모든 조합을 더해서 일일이 확인해보는 무차별 대입 방식을 Brute-Force라 한다.
