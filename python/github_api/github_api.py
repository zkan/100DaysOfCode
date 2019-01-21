from dataclasses import dataclass

import os

import requests_cache
from github import Github


requests_cache.install_cache(cache_name='github_cache',
                             backend='sqlite',
                             expire_after=180)

GITHUB_ACCESS_TOKEN = os.environ.get('GITHUB_ACCESS_TOKEN')


gh = Github(GITHUB_ACCESS_TOKEN)
print(gh.rate_limiting)

zkan = gh.get_user('zkan')
print(zkan)

repos = zkan.get_repos()
print(repos)


@dataclass
class Repo:
    name: str
    stars: int
    forks: int


repos = []
for each in zkan.get_repos():
    if each.fork:
        continue

    repos.append(Repo(name=each.name,
                      stars=each.stargazers_count,
                      forks=each.forks_count))

sorted_repos = sorted(repos, key=lambda x: x.stars, reverse=True)[:5]
print(sorted_repos)

projects = ['pronto-dashboard',]
for each in projects:
    repo = gh.get_organization('prontodev').get_repo(each)
    pulls = repo.get_pulls(state='open', sort='created', base='develop')
    for pr in pulls:
        print(pr)

