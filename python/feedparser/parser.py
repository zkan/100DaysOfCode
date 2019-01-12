import feedparser


FEED_FILE = 'newreleases.xml'

feed = feedparser.parse(FEED_FILE)

print(feed.entries)
print()
if 'title' in feed.entries[0]:
    for entry in feed.entries:
        print(f'{entry.published} - {entry.title}: {entry.link}')
