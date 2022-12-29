"""
리트코드 5번
가장 긴 팰린드롬 부분 문자열을 출력하라.
입력 - "badad"
출력 - "bad", "aba"

입력 - "cbbd"
출력 - "bb"
"""

# 맨 앞에서부터 리스트를 순회
# 포인터가 이동한 후 인덱스를 벗어나지 않는 범위에서
# 1. 오른쪽 확장 후 팰린드롬 여부 검사
# 2. 왼쪽 확장 후 팰린드롬 여부 검사
# 3. 왼쪽 오른쪽 모두 확장 후 팰린드롬 여부 검사

input_str = "babad"
pailn = []

for i in range(len(input_str)):
    for n in range(len(input_str)):
        if i - n >= 0:  # 왼쪽으로 확장
            word = input_str[i-n:i+n]
            if word == word[::-1]:
                pailn.append(word)
        if i + n < len(input_str):  # 오른쪽으로 확장
            word = input_str[i:i + n]
            if word == word[::-1]:
                pailn.append(word)
        if i - n >= 0 and i + n < len(input_str): # 양쪽으로 확장
            word = input_str[i-n:i + n]
            if word == word[::-1]:
                pailn.append(word)
    # 다음 글자로 이동

print(pailn)
print(sorted(pailn, key=len)[-1])
