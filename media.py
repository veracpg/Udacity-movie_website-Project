#Import webbrower to access the .open function

import webbrowser

#Creat a class with the correct arguments for each Instances
class Movie():
  #Constructor
  def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
      self.title = movie_title
      self.storyline = movie_storyline
      self.poster_image_url = poster_image
      self.trailer_youtube_url = trailer_youtube

  #Instance Method: allow the program to open in all instaces the url youtube link in a new window
  def show_trailer(self):
      webbrowser.open(self.trailer_youtube_url)
