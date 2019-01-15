import api


def main():
    client = api.MovieSearchClient()

    while True:
        question = 'How do you want to search the movies ' \
            '1) by keyword 2) by director 3) by IMDB code? '
        user_choice = int(input(question))

        results = []
        if user_choice == 1:
            keyword = input('Enter your keyword: ')
            response = client.search_movies(keyword)
            results = response.json()['hits']
        elif user_choice == 2:
            director_name = input("Enter a director's name: ")
            response = client.search_movies_by_director(director_name)
            results = response.json()['hits']
        elif user_choice == 3:
            imdb_code = input("Enter a IMDB code: ")
            response = client.get_movie_by_imdb(imdb_code)
            results.append(response.json())
        else:
            print('See you next time!')
            break

        for each in results:
            print()
            print(f"IMDB Code: {each['imdb_code']}")
            print(f"Title: {each['title']}")
            print(f"Director: {each['director']}")

        print()


if __name__ == '__main__':
    main()
