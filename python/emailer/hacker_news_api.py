# HackerNewsAPI: https://github.com/HackerNews/API

from dataclasses import dataclass

import requests


@dataclass
class Story:
    title: str
    url: str


def get_story_data(item_id):
    url = f'https://hacker-news.firebaseio.com/v0/item/{item_id}.json'
    results = requests.get(url).json()
    story = Story(
        title=results.get('title'),
        url=results.get('url')
    )
    return story


def get_top_10_best_stories():
    url = 'https://hacker-news.firebaseio.com/v0/beststories.json'
    results = requests.get(url).json()
    return [get_story_data(each) for each in results[:10]]
