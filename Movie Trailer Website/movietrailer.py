import media
import fresh_tomatoes

''' 
list all movies we'd like to show up on the html page, we will initialize an movie object and pass as arguments
the movie's name, description, poster image url, and trailer image url.
'''

forrest = media.Movie("Forrest Gump", "An honest man in a dishonest world",
                      "http://t0.gstatic.com/images?q=tbn:ANd9GcSppDgk99BKVA4TJtWc1FN4-HUkdWrFNfMm1-M0nQ01sIOcbTZu",
                      "https://www.youtube.com/watch?v=QgnJ8GpsBG8")
# print (forrest.storyline)

lego_movie = media.Movie("The Lego Movie", "An average lego finds his true purpose",
                         "https://images-na.ssl-images-amazon.com/images/M"
                         "/MV5BMTg4MDk1ODExN15BMl5BanBnXkFtZTgwNzIyNjg3MDE@._V1_UY1200_CR90,0,630,1200_AL_.jpg",
                         "https://www.youtube.com/watch?v=fZ_JOBCLF-I")
fury = media.Movie("Fury", "A tank batallion behind enemy lines",
                   "https://upload.wikimedia.org/wikipedia/en/1/17/Fury_2014_poster.jpg",
                   "https://www.youtube.com/watch?v=-OGvZoIrXpg")

movies = [forrest, lego_movie, fury]
fresh_tomatoes.open_movies_page(movies)
