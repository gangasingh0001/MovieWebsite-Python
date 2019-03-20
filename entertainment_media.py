import webbrowser
import fresh_tomatoes
import medias


class Movie():
    """ Class Movie describes the trailer of different movies.

    The _init_ method takes the parameters which describes a particular
    movie.

    Args:
         movie_title (str): Title of the movie.
         movie_storyline (str): What the movie is about.
         poster_image (str):  Link to the Poster of the movie.
         trailer_youtube (str): Link of the video in youtube where
         movie is placed.

    Attributes:
         title (str): Title of the movie.
         storyline (str): Description of the movie.

    Methods:
         movies : It is an array of movies which is passed
         to open_movies_page() function
         open_movies_page(): This function open the movie
         page where our movies will be displayed.
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline

# Movie function is called from medias file where movies description are passed
Twilight = medias.Movie("Twilight",
                        "A story of vampire who fall in love with a girl",
                        "https://upload.wikimedia.org/wikipedia/en/b/b6/Twilight_%282008_film%29_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=QDRLSqm_WVg")

Iron_Man = medias.Movie("Iron Man",
                        "A suit which can protect the world",
                        "https://upload.wikimedia.org/wikipedia/fi/thumb/7/70/Ironmanposter.JPG/375px-Ironmanposter.JPG",  # NOQA
                        "https://www.youtube.com/watch?v=8hYlB38asDY")

The_Fate_Of_The_Furious = medias.Movie("The fate of the furious",
                                       "The Racing cars are"
                                       "very excited to watch",
                                       "https://upload.wikimedia.org/wikipedia/en/2/2d/The_Fate_of_The_Furious_Theatrical_Poster.jpg",  # NOQA
                                       "https://www.youtube.com/watch?v=JwMKRevYa_M")  # NOQA

Interstellar = medias.Movie("Interstellar",
                            "The journey to the other Universe",
                            "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=zSWdZVtXT7E")

Martian = medias.Movie("Martian",
                       "The story of the team of scientist goes to "
                       "mars and their is mishappening with one of them.",
                       "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",  # NOQA
                       "https://www.youtube.com/watch?v=ej3ioOneTy8")

Beauty_And_The_Beast = medias.Movie("Beauty and the Beast",
                                    "A story of a girl falling"
                                    "in love with a beast",
                                    "https://upload.wikimedia.org/wikipedia/en/d/d6/Beauty_and_the_Beast_2017_poster.jpg",  # NOQA
                                    "https://www.youtube.com/watch?v=e3Nl_TCQXuw")  # NOQA

# movies is the array of different movies
# open_movies_page function will open a webpage that shows the all movies
movies = [Twilight, Iron_Man, The_Fate_Of_The_Furious,
          Interstellar, Martian, Beauty_And_The_Beast]
fresh_tomatoes.open_movies_page(movies)
