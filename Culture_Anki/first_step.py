from pprint import pprint
import re
import os
import srt
import datetime
import json

from cfg import KNOWN_WORDS_PATH

def get_known_words():
    if not os.path.exists(KNOWN_WORDS_PATH):
        with open (KNOWN_WORDS_PATH, "w") as fout:
            known_vocabulary_list = ask_user_what_words_they_know()
            value = {"source" : "Common words corpus", "date_added" : datetime.datetime.today().strftime('%Y %b%d')
}
            known_words_dictionary = {}
            for word in known_vocabulary_list:
                known_words_dictionary[word] = value
            
            json.dump(known_words_dictionary, fout)
    else:
        with open (KNOWN_WORDS_PATH, "r") as fin:
            known_words_dictionary = json.load(fin)
    return known_words_dictionary

def get_100_words():
    
    with open("Most_used_words(1000).txt","r") as fin:
        L = [line.strip() for line in fin.readlines()]
    MostCommonInChunks = []
    for i in range(0, 10000, 100):
        MostCommonInChunks.append(L[i:i + 100])
    return MostCommonInChunks

def ask_user_what_words_they_know():
    known_vocabulary = []
    MostCommonInChunks = get_100_words()
    for chunk in MostCommonInChunks:
        print()
        pprint('Do you know the following 100 words? If so, input y; if not, input n.')
        pprint( chunk ) 
        evaluate = input()
        if evaluate == 'y':
            known_vocabulary += chunk         
        else:
            break
    return known_vocabulary

def gather_movie_vocabulary(path):   
    regex_words =r"[a-zA-Z]+'*[a-zA-Z]+"
    regex_sentences =r".*"
    todays_date = datetime.datetime.today().strftime('%Y %b%d')

    output = {}
    word_freq = {}

    with open("Most_used_words(1000).txt", "r") as fin:
        words_in_file = fin.readlines()
        for i, word in enumerate(words_in_file):
            word_freq[word.strip()] = i
    
    print(word_freq)

    with open(path,"r") as fin:
        str = fin.read()
    subtitle_generator = srt.parse(str)
    for subtitle in subtitle_generator:
        sentences = re.findall(regex_sentences, subtitle.content)
        for sentence in sentences:
            #print('sentence', sentence)
            words = re.findall(regex_words, sentence)
            #print(words)
            for word in words:
                word_data = output.setdefault(word, {})
                word_data.setdefault('sample_sentences', []).append(sentence)
                if 'first_start_time' not in word_data:
                    word_data['first_start_time'] = subtitle.start
                if 'first_end_time' not in word_data:
                    word_data['first_end_time'] = subtitle.end
                word_data['source'] = 'Inception' # FIXME
                word_data['date_added'] = todays_date

    
    return output

def does_user_know(words):
    unknown_vocabulary = set()
    known_vocabulary = set()
    print("Please tell me, if you know the following words,  word by word. If you know the word, press enter; otherwise press n+enter.")
    for item in words:
        doesnt_know_input = input(item)   
        if doesnt_know_input:
            unknown_vocabulary.add(item)
        else:
            known_vocabulary.add(item)
    return known_vocabulary, unknown_vocabulary
            



    

def main():
    known_words = get_known_words()

    path = input("Give me a path to a subtitle file, please.")
    movie_vocabulary = gather_movie_vocabulary(path)


    possibly_unknown_movie_vocabulary = [word for word in movie_vocabulary if word not in known_words]
    known_movie_vocabulary, unknown_movie_vocabulary = does_user_know(possibly_unknown_movie_vocabulary)
    print("You don't know the following words of the movie you've chosen:", "\n".join(unknown_movie_vocabulary))
    with open(KNOWN_WORDS_PATH, "a") as fapp:
        fapp.writelines("\n".join(known_movie_vocabulary))



   
   



if __name__ == "__main__":
    main()
           
    
 







# MovieVocabulary = set(lowerCased)
# print(MovieVocabulary)
# with open("Unknown_words_user_n.txt", "w") as fout:
#     fout.writelines("\n".join(MovieVocabulary))    




#/home/sonja/Dropbox/RC/Vocabulary project/Culture_Anki/Inception.2010.1080p.BluRay.DTS.DXVA.x264-TiMPE.EN.srt
