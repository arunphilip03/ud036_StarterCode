import media
import fresh_tomatoes
import json

movies_data_file = "movies_data.json"
movies_list = []

# Load and parse movies data from the json file and create movie instances.

with open(movies_data_file) as movies_file:
    movies_data = json.load(movies_file)

    for movie_data in movies_data['movies']:
        movie = media.Movie(movie_data['title'],
                            movie_data['imageUrl'],
                            movie_data['youtubeUrl'])
        
        # Create a list of movie instances.
        
        movies_list.append(movie)
        


# Display the movie website.

fresh_tomatoes.open_movies_page(movies_list)

