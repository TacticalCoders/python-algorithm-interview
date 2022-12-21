"""
주어진 문자열이 팰린드롬인지 확인하라.
(팰린드롬: 앞뒤가 똑같은 단어, 문장. 뒤집어도 같은 말이 된다.)
- 대소문자 구분x
- 영문자와 숫자만을 대상
"""


# 나의 풀이
# 대문자 A와 a는 같은 것. -> 모든 문자를 대문자로 바꾸거나 소문자로 바꾼다. -> string.lower()
# 영문자와 숫자만 고려 -> 영문자와 숫자 외의 문자는 모두 제거한다. -> isalnum으로 체크

def check_palindrome(str):
    str = str.lower()
    start = 0
    end = len(str) - 1
    is_palin = True
    while start < end:
        while not str[start].isalnum() and start < end:  # ".," 은 True임
            start += 1
        while not str[end].isalnum() and end > start:
            end -= 1

        if str[start] != str[end]:
            is_palin = False
        start += 1
        end -= 1

    if is_palin:
        return "true"
    else:
        return "false"


x = input("문자를 입력하세요:")
print(check_palindrome(x))
