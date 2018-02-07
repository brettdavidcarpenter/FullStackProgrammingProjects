# Movie-Trailer-Project

A simple movie trailer website project for Udacity's full stack [nanodegree program]
(https://www.udacity.com/nanodegree). The project demonstrates the use of a Movie object class in Python to generate
a static webpage, which displays a listing of favorite movies and links each movie to its trailers video on YouTube.
The project also includes some CSS and jQuery involved in the display of the webpage.

# Starting the Project

To start this project, download the project files from here: <https://github.com/udacity/ud036_StarterCode>.

After downloading the project files, a movie trailer page can be created by importing media.py and fresh_tomatoes.py at the start of your Python script. Then create individual Movie objects by calling media.Movie() and supplying it with four arguments -- title, year, poster_url, and trailer_url. Lastly, to generate the movie trailers page, call fresh_tomatoes.open_movies_page() and supply it with an array of the movie objects you created.

```
import media
import fresh_tomatoes

#information for object arguments
title = "Pulp Fiction"
year = 1994
poster_url = "http://goo.gl/V5fb9n"
trailer = "https://www.youtube.com/watch?v=ewlwcEBTvcg"

# Create Movie object
pulp_fiction = media.Movie(title, year, poster_url, trailer_url)

# Create movie trailer page with array of one movie
fresh_tomatoes.open_movies_page([pulp_fiction])
```
