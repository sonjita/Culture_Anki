#for themoviedb
import requests
from pprint import pprint
#for opensubtitles
from xmlrpc.client import ServerProxy, Transport
from webapp.setup.secrets import password, username
import zlib
import base64
# import io
import chardet
from collections import Counter
import srt
import re


def discover_movie_page(n):
    return f"https://api.themoviedb.org/3/discover/movie/?page={n}\
             &api_key=e0345752ecea521b0ae6ecdd206d86ee"


def perform_request(url):
    return requests.get(url).json()


def get_the_movie_db_ids(n):
    response = perform_request(discover_movie_page(n))
    return [movie['id'] for movie in response['results']]


def exstract_imdbid(movie_db_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_db_id}?api_key=e0345752ecea521b0ae6ecdd206d86ee"
    response = perform_request(url)
    return response['imdb_id']


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
        # number_corrupted_files += 1
        return []


english_corpus = Counter()
open_subtitles_client = OpenSubtitlesClient(username, password, 'en')
movie_db_ids = get_the_movie_db_ids(1)
for id in movie_db_ids:
    imdb_id = exstract_imdbid(id)
    subtitle_infos = open_subtitles_client.get_list_subtitle_response(imdb_id, 'eng')
    if len(subtitle_infos) > 0:
        first_subtitle_id = subtitle_infos[0]['IDSubtitleFile']
        data = open_subtitles_client.download_encrypted_subtitles(first_subtitle_id)
        encryption_method = open_subtitles_client.get_encryption_method(data)
        decoded_data = open_subtitles_client.decode(encryption_method, data)
        subtitle_list = get_list_of_subtitle_content(decoded_data)
        # Matches any word of ASCII characters and optionally words with apostrophes
        # and hyphens. Ignores script styling.
        regex_words = re.compile(r"[a-zA-Z]+(?:'|-)?[a-zA-Z]*(?![\w]*>)")
        for line in subtitle_list:
            for word in re.findall(regex_words, line):
                english_corpus[word] += 1
print(len(english_corpus.keys()))

