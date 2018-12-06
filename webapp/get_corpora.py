#for themoviedb
import requests
from pprint import pprint
from pythonopensubtitles.opensubtitles import OpenSubtitles
#for opensubtitles
from xmlrpc.client import ServerProxy, Transport
from secrets import password 
import gzip
import zlib
import base64
import io
import chardet

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
#pprint(data)
#print(token)


client = ServerProxy('http://api.opensubtitles.org/xml-rpc', allow_none=True)
token_response = client.LogIn("sonjita1", password, "en", "TemporaryUserAgent")
#pprint(token_response)

pprint(client.SearchSubtitles(token_response['token'], [{'query' : 'harry potter', 'sublanguageid': 'eng'}], [{'limit' : 3}]))

subtitle_response = client.DownloadSubtitles(token_response['token'], ['1953644498'])
#5102597
# pprint(subtitle_response)

data = subtitle_response['data'][0]['data']
#encoding = subtitle_response['data'][0]['encoding']
subtitle_bytes = zlib.decompress(base64.b64decode(data), 16 + zlib.MAX_WBITS)
print(str(subtitle_bytes, 'UTF-8'))


# data = subtitle_response['data'][0]['data']
# subtitle_decripted = zlib.decompress(base64.b64decode(data), 16 + zlib.MAX_WBITS).decode('windows')
# pprint(subtitle_decripted)

# subtitle_decripted = zlib.decompress(base64.b64decode(subtitle_response['data'][0]['data']), 32 + zlib.MAX_WBITS).decode('UTF-8')

#pprint(subtitle_decripted)

# compressed_data = base64.b64decode(subtitle_response['data'][0]['data'])
# sub_text = gzip.GzipFile(fileobj=io.BytesIO(compressed_data)).read()

# pprint(sub_text)



# subtitle_bytes = gzip.decompress(base64.b64decode(subtitle_response['data'][0]['data']))
#print(chardet.detect(subtitle_bytes)['encoding'])
#subtitle_decripted = subtitle_bytes.decode('windows-1255')
#pprint(subtitle_decripted)
#f=gzip.open()
#16 + zlib.MAX_WBITS
#print("type:", type(subtitle_decripted))

#pprint(subtitle_decripted.hex())

