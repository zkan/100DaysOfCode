import requests


URL = 'http://store.steampowered.com/feeds/newreleases.rss'

if __name__ == '__main__':
    r = requests.get(URL)
    with open('newreleases.xml', 'wb') as f:
        f.write(r.content)
