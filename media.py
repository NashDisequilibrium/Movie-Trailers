import webbrowser

#Create movie class which will be used for all of the movies we have.This will then be used by entertainment_centre.py

class Movie():
    valid_ratings = ["g", "PG", "PG-13", "R"]

    #There will be four aspects to each movie, including the video.
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
# Browser is opened so that the application is run.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
