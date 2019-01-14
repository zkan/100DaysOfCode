import api


def main():
    client = api.MovieSearchClient()
    response = client.search_movies('game')
    print(response.json())

    print()

    response = client.search_movies_by_director('steven')
    print(response.json())

    print()

    response = client.get_movie_by_imdb('tt0181689')
    print(response.json())


if __name__ == '__main__':
    main()
