"""
문자열 배열을 받아 애너그램 단위로 그룹핑하라.
*애너그램. 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것.(어구전철)
ex) 문전박대 -> 대박전문
"""

# 서로 다른 단어의 문자열의 구성 성분이 같으면 됨.
# 순서는 상관없음.

words = ["eat", "tea", "tan", "ate", "nat", "bat"]

character = {}
for word in words:
    character[word] = list(word)
    character[word].sort()

values = character.values()
print(values)
value_set = set(values)
keys = character.keys()
result = []

for value in value_set:
    ann = [key for key in keys if character[key] == value]
    result.append(ann)

print(result)