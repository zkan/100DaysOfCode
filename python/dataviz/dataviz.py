from datetime import datetime
from collections import Counter
import re

import feedparser
import plotly
import plotly.graph_objs as go


def convert_to_datetime(date_str):
    date_str = date_str.split('+')[0].strip()
    dt = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S')
    return f'{dt.year}-{dt.month}'


def get_category(link):
    known = dict(codechallenge='challenge',
                 twitter='news',
                 special='special',
                 guest='guest',)
    default = 'article'
    category = re.sub(r'.*\.es/([a-z]+).*', r'\1', link)
    return known.get(category) or default


def transpose_list_of_tuples(data):
    if isinstance(data, dict):
        data = data.items()
    transposed = list(zip(*data))
    return transposed


if __name__ == '__main__':
    url = 'http://projects.bobbelderbos.com/pcc/dates/all.rss.xml'
    blog_feed = feedparser.parse(url)
    entries = blog_feed['entries']

    pub_dates = [convert_to_datetime(entry.published) for entry in entries]
    posts_by_month = Counter(pub_dates)
    print(posts_by_month)

    categories = [get_category(entry.link) for entry in entries]
    cnt = Counter(categories)
    categories = cnt.most_common()
    print(categories)

    tags = [tag.term.lower() for entry in entries for tag in entry.tags]
    cnt = Counter(tags)
    tags = cnt.most_common()
    print(tags)

    print(transpose_list_of_tuples(posts_by_month))

    x, y = transpose_list_of_tuples(posts_by_month)
    data = [go.Bar(x=x, y=y)]
    plotly.offline.plot(data, filename='post-frequency.html')
