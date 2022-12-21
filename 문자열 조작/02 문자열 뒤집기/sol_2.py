"""
더 파이썬다운 방식. 기본 기능을 적극활용하자.
"""

class Solution:
    def reverse_string(self, s) -> None:
        s.reverse()  # reverse()는 리스트에만 제공된다.
        # 슬라이싱을 사용하는 방법도 있다.
        s = s[::-1]
        s[:] = s[::-1] # 리트코드 에러 트릭