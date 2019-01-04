import webbrowser

import api


def main():
    print()
    print('******* SEARCH TALK PYTHON *******')
    keywords = input('What keywords to search for? ')

    results = api.find_talk_python_episodes(keywords)
    print(f'There are {len(results)} matching episodes:')
    for index, each in enumerate(results, 1):
        print(f'{index}. [Episode {each.id}] {each.title} ({each.url})')

    print()
    episode_urls = {index: each.url for index, each in enumerate(results, 1)}
    number = int(input('Pick the episode number to listen: '))
    url = f'https://talkpython.fm{episode_urls[number]}'

    # If new is 0, the url is opened in the same browser window if possible.
    # If new is 1, a new browser window is opened if possible.
    # If new is 2, a new browser page (“tab”) is opened if possible.
    webbrowser.open(url, new=2)


if __name__ == '__main__':
    main()
