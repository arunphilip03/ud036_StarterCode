import webbrowser


class Movie(object):
    """ This class stores movie related information.
    Attributes:
        title: A string indicating the title of the movie.
        poster_image_url: A string to hold the poster image url of the movie.
        trailer_youtube_url: A string to hold the youtube trailer url
                             of the movie.
    """

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """Initialize Movie"""
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
