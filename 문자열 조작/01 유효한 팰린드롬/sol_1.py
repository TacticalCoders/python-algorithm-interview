"""
문자열을 리스트로 변환하는 방법
"""


def is_palindrome(self, s: str) -> bool:
    # 전처리
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    # 팰린드롬 여부 판별
    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True
"""
리스트를 사용하면 이렇게 간편하게 확인할 수 있다.
파이썬 리스트는 pop() 함수를 지원한다.
인자로 0을 지정하면 맨 앞의 값을 가져올 수 있다.
아우 인자도 전달하지 않으면 맨 뒤의 값을 리턴.

문자와 숫자가 아닌 숫자는 무시해야 한다. -> char.isalnum()
대문자 소문자는 같게 취급되어야 한다. -> islowr()
문자와 숫자만을 대상으로 비교해야 한다. -> 리스트를 활용
앞 뒤를 피교하며 점점 안쪽으로 비교해야 한다. -> pop() 함수 사용
"""