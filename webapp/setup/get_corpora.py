#for themoviedb
import requests
from pprint import pprint
#for opensubtitles
from xmlrpc.client import ServerProxy, Transport
from secrets import password, username
import zlib
import base64
# import io
import chardet
from collections import Counter
import srt
import re
import time


urls = [f"https://api.themoviedb.org/3/discover/movie/?page={num}&api_key=e0345752ecea521b0ae6ecdd206d86ee" for num in range(1,2)]


def discover_movie_page(n):
    return f"https://api.themoviedb.org/3/discover/movie/?page={n}\
             &api_key=e0345752ecea521b0ae6ecdd206d86ee"


# def discover_movies_urls(n_pages):
#     return [discover_movie_page(i) for i in range(1, n_pages + 1)]


def perform_request(url):
    return requests.get(url).json()


def get_the_movie_db_ids(n):
    response = perform_request(discover_movie_page(n))
    return [movie['id'] for movie in response['results']]


def exstract_imdbid(movie_db_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_db_id}?api_key=e0345752ecea521b0ae6ecdd206d86ee"
    response = perform_request(url)
    return response['imdb_id']


movie_db_ids = get_the_movie_db_ids(1)
imdb_id = exstract_imdbid(movie_db_ids[4])
# for id in movie_db_ids:
#     print(id)
#     print(exstract_imdbid(id))


class OpenSubtitlesClient:
    def __init__(self, username, password, language):
        self.client = ServerProxy('http://api.opensubtitles.org/xml-rpc', allow_none=True)
        self.token = self.client.LogIn(username, password, language, "TemporaryUserAgent")['token']
    
    def get_list_subtitle_response(self, query, language):
        response = self.client.SearchSubtitles(self.token, [{'query': query, 'sublanguageid': language}], [{'limit' : 3}])
        return response['data']

    def download_encrypted_subtitles(self, subtitle_file_id):
        response = self.client.DownloadSubtitles(self.token, [subtitle_file_id])
        decompresses_subtitle_file = zlib.decompress(base64.b64decode(response['data'][0]['data']), 16 + zlib.MAX_WBITS)
        return decompresses_subtitle_file

    def get_encryption_method(self, encrypted_subtitles):
        return chardet.detect(encrypted_subtitles)['encoding']

    def decode(self, encryption_method, data):
        return data.decode(encryption_method)


number_corrupted_files = 0


def get_list_of_subtitle_content(subtitles):
    srt_generator = srt.parse(subtitles)
    try:
        return [chunk.content.replace('\n', ' ') for chunk in srt_generator]
    except srt.SRTParseError:
        number_corrupted_files += 1
        return []

# subtitle_response = client.DownloadSubtitles(token_response['token'], ['1953644498'])


# def get_titles(url):
#     response = requests.get(url).json()
#     return response

# pprint(get_titles(discover_movie_page(1)))
# pprint(get_titles(url_movie_request))

# titles = [(movie["title"], movie['imdbid'] for url in urls for movie in get_titles(url)["results"]]
# print(titles)
#print(len(titles))

#client = ServerProxy('http://api.opensubtitles.org/xml-rpc', allow_none=True)
#token_response = client.LogIn("sonjita1", password, "en", "TemporaryUserAgent")
#pprint(token_response)

# list_subtitle_response = client.SearchSubtitles(token_response['token'], [{'query' : 'harry potter', 'sublanguageid': 'eng'}], [{'limit' : 3}])
#pprint(client.SearchSubtitles(token_response['token'], [{'query': 'tt5848272', 'sublanguageid': 'eng'}], [{'limit' : 3}]))


# subtitle_response = client.DownloadSubtitles(token_response['token'], ['1953644498'])
#5102597
# pprint(subtitle_response)

open_subtitles_client = OpenSubtitlesClient(username, password, 'en')
subtitle_infos = open_subtitles_client.get_list_subtitle_response(imdb_id, 'eng')
first_subtitle_id = subtitle_infos[0]['IDSubtitleFile']
data = open_subtitles_client.download_encrypted_subtitles(first_subtitle_id)
encryption_method = open_subtitles_client.get_encryption_method(data)
decoded_data = open_subtitles_client.decode(encryption_method, data)
subtitle_list = get_list_of_subtitle_content(decoded_data)

#data = subtitle_response['data'][0]['data']
#encoding = subtitle_response['data'][0]['encoding']
# subtitle_bytes = zlib.decompress(base64.b64decode(data), 16 + zlib.MAX_WBITS)
# print(str(subtitle_bytes, 'UTF-8'))

# subtitle_generator = srt.parse(str(subtitle_bytes, 'UTF-8'))
# subtitle_list = [lines.content for lines in subtitle_generator]

# Matches any word of ASCII characters and optionally words with apostrophes
# and hyphens. Ignores script styling.
regex_words = re.compile(r"[a-zA-Z]+(?:'|-)?[a-zA-Z]*(?![\w]*>)")
english_corpus = Counter()
for line in subtitle_list:
    for word in re.findall(regex_words, line):
        english_corpus[word] += 1
print(len(english_corpus.keys()))


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

