import requests
import pprint
from pythonopensubtitles.opensubtitles import OpenSubtitles

ost = OpenSubtitles()

url_movie_request = "https://api.themoviedb.org/3/movie/335983?api_key=e0345752ecea521b0ae6ecdd206d86ee"

#urls = [f"https://api.themoviedb.org/3/discover/movie/?page={num}&api_key=e0345752ecea521b0ae6ecdd206d86ee" for num in range(1,2)]

def get_titles(url):
    response = requests.get(url).json()
    return response
#pprint.pprint(get_titles(url_movie_request))

#titles = [(movie["title"], movie["id"]) for url in urls for movie in get_titles(url)["results"]]
#print(titles)
#print(len(titles))

data = ost.download_subtitles(["tt0137523"])
pprint.pprint(data)
print(token)