"""
문자열을 뒤집는 함수를 작성하라.
- 입력값은 문자 배열.
- 리턴 없이 내부리스트 조작
"""

# 맨 뒤에서 부터 한 칸씩 교체하면 되는거 아녀?
def revers_string(s_list):
    start = 0
    end = len(s_list) - 1
    while start <= end:
        s_list[start], s_list[end] = s_list[end], s_list[start]
        start += 1
        end -= 1
    print(s_list)

x = input("입력:")
x = [ c for c in x]
revers_string(x)