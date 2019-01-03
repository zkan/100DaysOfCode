import collections
from typing import List

import requests


Episode = collections.namedtuple('Episode', 'category, id, url, '
                                            'title, description')


def find_talk_python_episodes(keywords: str) -> List[Episode]:
    query = keywords.replace(' ', '-')
    url = 'http://search.talkpython.fm/api/search'
    params = {
        'q': query
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    results = response.json().get('results')

    episodes = []
    for each in results:
        if each.get('category') == 'Episode':
            episodes.append(Episode(**each))

    return episodes
