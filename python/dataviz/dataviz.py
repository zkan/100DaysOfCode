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


if __name__ == '__main__':
    url = 'http://projects.bobbelderbos.com/pcc/dates/all.rss.xml'
    blog_feed = feedparser.parse(url)
    entries = blog_feed['entries']

    pub_dates = [convert_to_datetime(entry.published) for entry in entries]
    posts_by_month = Counter(pub_dates)
    print(posts_by_month)

    categories = [get_category(entry.link) for entry in entries]
    cnt = Counter(categories)
    print(cnt.most_common())
