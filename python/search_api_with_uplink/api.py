import uplink


class MovieSearchClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm')

    @uplink.get('/api/search/{keyword}')
    def search_movies(self, keyword):
        """ Search movies with keyword """

    @uplink.get('/api/director/{director_name}')
    def search_movies_by_director(self, director_name):
        """ Search movies by director """

    @uplink.get('/api/movie/{imdb_number}')
    def get_movie_by_imdb(self, imdb_number):
        """ Get movie by IMDB code """
