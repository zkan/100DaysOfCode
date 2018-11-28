from collections import Counter


file_name = 'harry.txt'

with open(file_name) as f:
    text = f.read()
    words = text.split(' ')
    c = Counter(words)
    print(f'Top 5 common words: {c.most_common(5)}')
