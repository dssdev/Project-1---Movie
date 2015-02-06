from enum import Enum

class Movie():
    """Creates an instance of a movie with the required parameters:
        title - Text movie title
        poster - URL to an image of the movie poster
        trailer - URL to a YouTube video
        runtime - Duration of the movie in minutes
        rating - Rating enum - G,PG,PG13 or R

        Methods:
        isKidFriendly - returns true if G or PG, false if PG13 or R"""
    def __init__(self, title, poster,trailer,runtime, rating):
        self.title=title
        self.poster_image_url=poster
        self.trailer_youtube_url=trailer
        self.runtime=runtime
        self.rating=rating
    
    def isKidFriendly(self):
        if self.rating.value <= 2: return True
        else: return False

class Rating(Enum):
    G = 1
    PG = 2
    PG13 = 3
    R = 4
