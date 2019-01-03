from dataclasses import dataclass
from typing import List

import requests


@dataclass
class Episode:
    category: str
    id: int
    url: str
    title: str
    description: str


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
