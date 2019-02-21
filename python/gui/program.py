import api


def main():
    print()
    print('******* SEARCH TALK PYTHON *******')
    keywords = input('What keywords to search for? ')

    results = api.find_talk_python_episodes(keywords)
    print(f'There are {len(results)} matching episodes:')
    for index, each in enumerate(results, 1):
        print(f'{index}. [Episode {each.id}] {each.title} ({each.url})')


if __name__ == '__main__':
    main()
