"""
투 포인터를 최대(높이가 최고로 높은 곳)로 이동하는 방법

좌나 우에 있는 가장 높은 기둥의 높이에서 현재의 높이를 뺀 값을 누적
가장 높은 기둥을 기준으로 좌우로 나눠지게 되므로 이 기둥을 찾을 때까지 양끝이 가까워짐.
"""

def trap(self, height):
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume
