import fresh_tomatoes
import media

#Each of the movies is listed. They are all instances of the class Movie, which can be found in media.py 

citizen_kane = media.Movie("Citizen Kane 9/10",
                        "Kane seeks his moral redemption",
						#image for movie is taken from Wikimedia
                        "http://upload.wikimedia.org/wikipedia/en/c/ce/Citizenkane.jpg",
                        #movie trailers are pulled from youtube, see class in media.py 
						"https://www.youtube.com/watch?v=_1A_WUNQlKY")

faust = media.Movie("Faust 10/10",
                     "Faust's soul is wagered with Mephistopheles",
                     "http://upload.wikimedia.org/wikipedia/en/a/ad/Faust_1926_MGM_poster_US_Release.jpg",
                     "https://www.youtube.com/watch?v=8lmaBc9TAxc")

there_will_be_blood = media.Movie("There Will Be Blood 8/10",
                                  "Creating an oil empire...",
                                  "http://upload.wikimedia.org/wikipedia/en/d/da/There_Will_Be_Blood_Poster.jpg",
                                  "https://www.youtube.com/watch?v=f3THVbr4hlY")

no_country = media.Movie("No Country For Old Men 7/10",
                                  "Assassin hunts down victim",
                                  "http://upload.wikimedia.org/wikipedia/en/8/8b/No_Country_for_Old_Men_poster.jpg",
                                  "https://www.youtube.com/watch?v=38A__WT3-o0")

american_beauty = media.Movie("American Beauty 8/10",
                                  "Man has existential crisis",
                                  "http://upload.wikimedia.org/wikipedia/en/b/b6/American_Beauty_poster.jpg",
                                  "https://www.youtube.com/watch?v=3ycmmJ6rxA8")

some_like_it_hot = media.Movie("Some Like It Hot 9/10",
                                  "Men dress as women to escape the mafia",
                                  "http://upload.wikimedia.org/wikipedia/en/b/b4/Some_Like_It_Hot_poster.jpg",
                                  "https://www.youtube.com/watch?v=rI_lUHOCcbc")

                               
                                     

movies = [citizen_kane, faust, there_will_be_blood, no_country, american_beauty, some_like_it_hot]
fresh_tomatoes.open_movies_page(movies)
