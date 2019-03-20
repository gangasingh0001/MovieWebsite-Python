import webbrowser


class Movie():
    """ Class Movie describes the description about movie.

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
         poster_image_url (str): URL of the Image of movie.
         trailer_youtube_url (str): Movie URL on youtube.

    Methods:
         show_trailer(): This function open the movie URL
         on a new browser window and can be played.
    """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """shows the trailer of movie

        Args:
           trailer_youtube_url (str): Movie URL on youtube.
        """
        webbrowser.open(self.trailer_youtube_url)
