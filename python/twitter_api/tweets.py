from dataclasses import dataclass
import datetime
import os

# import matplotlib
import tweepy
from wordcloud import WordCloud


@dataclass
class Tweet:
    id: int
    text: str
    created: datetime.datetime
    likes: int
    rts: int


TWITTER_ACCOUNT = 'zkancs'

TWITTER_KEY = os.environ.get('TWITTER_KEY')
TWITTER_SECRET = os.environ.get('TWITTER_SECRET')
TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET')


auth = tweepy.OAuthHandler(TWITTER_KEY, TWITTER_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth)


def get_tweets():
    for tw in tweepy.Cursor(api.user_timeline, screen_name=TWITTER_ACCOUNT,
                            exclude_replies=False, include_rts=True).items(10):
        yield Tweet(id=tw.id, text=tw.text, created=tw.created_at,
                    likes=tw.favorite_count, rts=tw.retweet_count)


if __name__ == '__main__':
    tweets = list(get_tweets())
    print(len(tweets))
    print(tweets)

    excl_rts = [tweet for tweet in tweets if not tweet.text.startswith('RT')]
    print(len(excl_rts))
    print(excl_rts)

    print('Top 10 Tweets')
    top_10 = sorted(excl_rts, key=lambda tw: (tw.likes + tw.rts) / 2,
                    reverse=True)
    print(top_10)

    all_tweets = ' '.join(tw.text.lower() for tw in tweets)
    print(all_tweets)

    # wordcloud = WordCloud().generate(all_tweets)
    # print(wordcloud)

    # import matplotlib.pyplot as plt
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")
