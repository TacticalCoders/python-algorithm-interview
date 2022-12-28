"""
가장 흔한 단어 (리트코드 819)
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라
- 대소문자 구분 x
- 구두점(마침표, 쉼표) 무시
- 입력 : 문자열
- 금지된 단어 : 리스트
- 출력 : 문자열(하나의 단어)
"""

# 문자열을 단어 단위로 구분하기 위하여 split()
# 구두점제거하여 리스트로 저장.
# -- 구두점은 토큰의 맨 마지막에 등장하므로 각 토큰의 마지막만 체크
# 리스트의 count값을 기준으로 정렬.
# 금지된 단어 제거
# 가장 앞에 있는 항목 출력.

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]


def mostCommonWord(paragraph, banned):
    paragraph = paragraph.lower()  # 소문자로 변경
    tokens = paragraph.split()
    words = []
    for token in tokens:
        if not token[-1].isalpha():
            token = token[:-1]
        words.append(token)
    word_set = set(words)

    max_cnt = 0
    max_word = ""
    for word in word_set:
        if word not in banned:
            if words.count(word) > max_cnt:
                max_word = word
                max_cnt = words.count(word)
    print(max_word)
    return max_word
