import feedparser


FEED_FILE = 'newreleases_talkpython.xml'

feed = feedparser.parse(FEED_FILE)

if 'title' in feed.entries[0]:
    for entry in feed.entries:
        print(f'{entry.published} - {entry.title}: {entry.link}')
