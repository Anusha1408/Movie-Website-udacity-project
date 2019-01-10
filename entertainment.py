import media
import fresh_tomatoes

#  Inserting the SkyScrapper Object and the information of SkyScrapper

SkyScrapper = media.Movie("Sky Scrapper",
                          "The sky is the limit",
                          "https://newhdphotos.com/wp-content/uploads/2018/02/skyscraper-poster-dwayne-johnson.jpg ",   # NOQA
                          "https://youtu.be/watch?v=t9QePUT-Yt8")


#  Inserting the Deadpool_2 Object and  the information of Deadpool_2
Deadpool_2 = media.Movie("Deadpool 2",
                         "From the studio that killed Wolverinet",
                         "https://images.alphacoders.com/939/thumb-350-939907.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=D86RtevtfrA")


#  Inserting the Black Panther  Object and the information of Black Panther
Black_Panther = media.Movie("Black Panther",
                            "The Avengers have a new king",
                            "https://wallpapercave.com/wp/wp1869889.jpg",     # NOQA
                            "https://www.youtube.com/watch?v=dxWvtMOGAhw")


# Inserting the A star is Born Object and the information of A Star is Born
A_Star_Is_Born = media.Movie("A Star Is Born",
                             "Fate Raised Her ToFame,killed the man she loved",
                             "https://www.warnerbros.co.uk/~/media/images/warner%20bro/movies/a%20star%20is%20born/key%20art.ashx",     # NOQA
                             "https://www.youtube.com/watch?v=nSbzyEJ8X9E")

#  create an array of movies to pass to the fresh_tomatoes.py function called
#  open_movies_page
movies = [SkyScrapper, Deadpool_2, Black_Panther, A_Star_Is_Born]

#  call the open_movies_page function
fresh_tomatoes.open_movies_page(movies)

