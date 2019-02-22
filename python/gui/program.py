from gooey import Gooey, GooeyParser

import api


@Gooey(program_name='Talk Python Search App',
       program_description='Search Talk Python\'s data for episodes')
def main():
    print()
    print('******* SEARCH TALK PYTHON *******')

    keywords = get_keywords()
    results = api.find_talk_python_episodes(keywords)
    print(f'There are {len(results)} matching episodes:')
    for index, each in enumerate(results, 1):
        print(f'{index}. [Episode {each.id}] {each.title} ({each.url})')


def get_keywords():
    # keywords = input('What keywords to search for? ')
    # return keywords
    parser = GooeyParser()
    parser.add_argument('keywords', help='Keywords')
    args = parser.parse_args()
    return args.keywords


if __name__ == '__main__':
    main()
