"""
리스트 컴프리헨션
정규식
딕셔너리 이용(defaultdict)
collections.Counter()
"""
import collections
import re


def mostCommonWord(self, paragraph, banned):
    # 정규식에서 \w는 단어 문자를 뜻함. ^은 not.
    # 즉, 단어가 아닌 것을 공백으로 치환하겠다는 뜻.
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
        .lower().split()
                if word not in banned]

    counts = collections.defaultdict(int)
    for word in words:
        counts[word] += 1

    return max(counts, key=counts.get)  # 값(value)가 가장 큰 키를 가져오겠다는 뜻.(argmax)

    # counts = collections.Counter(words)  # collections의 counter 사용
    # return counts.most_common(1)[0][0]  # most_common(1)로 가장 흔하게 등장하는 단어의 첫 번째 값을 가져옴.
