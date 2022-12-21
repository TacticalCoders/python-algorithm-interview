"""
데크(덱) 자료형을 이용한 방법
리스트보다 속도를 높일 수 있다.
"""
import collections


def is_palindrome(self, s: str):
    # 전처리
    strs = collections.deque()  # deque를 선언하기 위해선 collections를 import 해야 한다.
    for char in s:
        if char.isalnum():
            strs.append(char.lower())  # deque에 삽입하는 법은 리스트와 같다.

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.popleft() != strs.pop():  # deque에서는 popleft()를 통해 맨 앞의 원소를 가져올 수 있다.
            return False

    return True


"""
데크를 사용하면 약 5배 가까이 속도를 높일 수 있다.
리스트의 pop(0)이 O(n)이지만 popleft()는 O(1)이기 때문.
"""
