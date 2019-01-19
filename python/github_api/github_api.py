from github import Github, InputFileContent


gh = Github()
print(gh.rate_limiting)

zkan = gh.get_user('zkan')
print(zkan)
