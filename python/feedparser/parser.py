import feedparser


FEED_FILE = 'newreleases.xml'

feed = feedparser.parse(FEED_FILE)

print(feed.entries)
print()
for entry in feed.entries:
    print(f'{entry.published} - {entry.title}: {entry.link}')
