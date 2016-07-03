import fresh_tomatoes
import movies
from urllib2 import urlopen
from json import load, dumps
from collections import OrderedDict

# create dictionary of IMDB movie IDs and youtube trailers
movie_dict_for_api = OrderedDict([
    ("tt0107290", "https://www.youtube.com/watch?v=lc0UehYemQA"),
    ("tt0128445", "https://www.youtube.com/watch?v=GxCNDpvGyss"),
    ("tt0088763", "https://www.youtube.com/watch?v=qvsgGtivCgs"),
    ("tt0133093", "https://www.youtube.com/watch?v=m8e-FF8MsqU"),
    ("tt0816692", "https://www.youtube.com/watch?v=Lm8p5rlrSkY"),
    ("tt1748122", "https://www.youtube.com/watch?v=7N8wkVA4_8s")
    ])

# create new dictionary that will contain all movie objects
movie_data = OrderedDict()

# loop through movie IDs to get title, plot & poster via APIs
# create instances of the Movie object
# add them to the movie_data dictionary using title as object name
for movie_id, trailer_url in movie_dict_for_api.items():
    api_key = "&api_key=7433ae4e86361bbfa859a115b86c16b5"
    get_info = "http://api.themoviedb.org/3/find/" + movie_id + "?external_source=imdb_id" + api_key  # noqa
    get_poster = "http://api.themoviedb.org/3/movie/" + movie_id + "/images?" + api_key  # noqa
    response = urlopen(get_info)
    response2 = urlopen(get_poster)
    movie_json = load(response)
    poster_json = load(response2)
    title = movie_json["movie_results"][0]["title"]
    plot = movie_json["movie_results"][0]["overview"]
    poster_url = "http://image.tmdb.org/t/p/w500"
    poster_url += poster_json['posters'][0]['file_path']
    movie_obj = movies.Movie(title, plot, poster_url, trailer_url)
    movie_data[title] = movie_obj

# shows page with each movie poster as a single tile with link to trailer
fresh_tomatoes.open_movies_page(movie_data)




