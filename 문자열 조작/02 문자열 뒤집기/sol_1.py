"""
투 포인터를 이용한 스왑
"""


class Solution:
    def reverse_string(self, s) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
