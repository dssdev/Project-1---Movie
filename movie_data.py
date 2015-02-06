import movie_class
import fresh_tomatoes

predator = movie_class.Movie("Predator",
                             "http://images.moviepostershop.com/predator-movie-poster-1987-1020261352.jpg",
                             "https://www.youtube.com/watch?v=Y1txEAywdiw",
                             "107",
                             movie_class.Rating.R)

shank = movie_class.Movie("Shawshank Redemption",
                          "http://www.impawards.com/1994/posters/shawshank_redemption_ver1.jpg",
                          "https://www.youtube.com/watch?v=6hB3S9bIaco",
                          "142",
                          movie_class.Rating.R)

wonderfullife = movie_class.Movie("It's a Wonderful Life",
                          "http://cache2.allpostersimages.com/p/LRG/37/3724/9ZOAF00Z/posters/it-s-a-wonderful-life-donna-reed-james-stewart-1946.jpg",
                          "https://www.youtube.com/watch?v=LJfZaT8ncYk",
                          "130",
                          movie_class.Rating.G)

fresh_tomatoes.open_movies_page([predator,shank,wonderfullife])
