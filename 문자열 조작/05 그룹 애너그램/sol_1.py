import collections


def groupAnagrams(self, strs):
    anagrams = collections.defaultdict(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return list(anagrams.values())

# sorted는 문자열을 오름차순으로 정렬함과 동시에 리스트로 분해한다.
# "".join은 리스트를 하나의 문자열로 병합해준다.

# 문제의 키포인트는 애너그램임을 파악할 때 '정렬'을 떠올리는 것이다.
# 문자의 종류와 수는 같으므로 오름차순 정렬을 하면 같아질 것이라고 생각해야 한다.
# 또한 이를 키 값으로 하여 딕셔너리에 바로 할당하는 것이 아니라 append()를 통해 계속 추가할 수 있다는 점도 알아두자.
