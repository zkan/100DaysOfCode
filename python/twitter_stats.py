from collections import Counter
import csv
import re


hashtags = Counter()

with open('tweets.csv', 'r') as csvfile:
    tweets = [row for row in csv.DictReader(csvfile)]
    for each in tweets:
        matching_hashtags = re.compile(r'(#\S+)').findall(each['text'])
        if matching_hashtags:
            for hashtag in matching_hashtags:
                hashtags[hashtag.lower()] += 1

print('Most used hashtags:')
print('-' * 10)
for key, count in hashtags.most_common(5):
    print(f'{key:15} {count:5}')
