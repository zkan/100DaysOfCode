import feedparser
import plotly
import plotly.graph_objs as go


url = 'http://projects.bobbelderbos.com/pcc/dates/all.rss.xml'
blog_feed = feedparser.parse(url)
entries = blog_feed['entries']
print(entries)
