"""
스택을 쌓아서 푸는 방법

이전 높이포다 현재 높이가 높아졌을 때를 기준으로 격차 만큼 부피를 채움.
'이전 높이'는 스택으로 채워 나가다 높이가 높아졌을 때 하나씩 꺼냄
"""


def trap(self, height):
    stack = []
    volume = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not len(stack):
                break

            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)

    return volume
