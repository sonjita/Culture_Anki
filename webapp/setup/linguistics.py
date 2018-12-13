import nltk
from nltk import *
from nltk.stem import WordNetLemmatizer
import re
from nltk.corpus import wordnet as wn


def tokenize(sentence):
    regex_words = re.compile(r"[a-zA-Z]+(?:'|-)?[a-zA-Z]*(?![\w]*>)")
    return [word for word in re.findall(regex_words, sentence)]


TRANSLATE_POS = {"v" : "v", "n" : "n", "j" : "j", "r" : "r"}


def add_pos_to_word(list_words):
    return [(word, pos[0].lower()) for word, pos in nltk.pos_tag(list_words)]

print(nltk.pos_tag(["nicely"]))

def lemmatize_all_words_in_list(list):
    lemmatizer = WordNetLemmatizer()
    recognized_words = []
    unrecognized_words = []
    for word, pos in add_pos_to_word(list):
        pos = TRANSLATE_POS.get(pos)
        print(word)
        try:
            if pos == "r":
                lemma = wn.synset(f"{word}.r.1").lemmas()[0].pertainyms()[0].name()
            elif pos:
                lemma = lemmatizer.lemmatize(word, pos=pos)
            else:
                lemma = word
            recognized_words.append(lemma)
        except Exception as e:
            print("word: ", word)
            print("exception: ", e)
            print("pos: ", pos)
            print("------------")
            unrecognized_words.append(word)
    return recognized_words, unrecognized_words 
        
    


sentence = "The dogs kissed the cats smoothly."
sentence2 = "I had the feeling that what we wanted was to have incorporated this into sentences nicely if it was summer when I was feeling uspet while setting the server up."



print(lemmatize_all_words_in_list(tokenize(sentence2)))


lemmatizer = WordNetLemmatizer()



word = "kisses"
lemma = lemmatizer.lemmatize(word)
