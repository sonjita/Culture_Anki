from pprint import pprint
import re
import os

KNOWN_WORDS_PATH  = "/home/sonja/Dropbox/RC/Vocabulary project/First_step/Known_words_user_x.txt"

def get_known_words():
    if not os.path.exists(KNOWN_WORDS_PATH):
        with open (KNOWN_WORDS_PATH, "w") as fout:
            known_vocabulary_list = ask_user_what_words_they_know()
            fout.writelines("\n".join(known_vocabulary_list))
    else:
        with open (KNOWN_WORDS_PATH, "r") as fin:
            known_vocabulary_list = [item.strip() for item in fin.readlines()]
    return set(known_vocabulary_list)

def ask_user_what_words_they_know():
    known_vocabulary = []
    with open("Most_used_words(1000).txt","r") as fin:
        L = [line.strip() for line in fin.readlines()]
    MostCommonInChunks = []
    for i in range(0, 10000, 1000):
        MostCommonInChunks.append(L[i:i+1000])
    for chunk in MostCommonInChunks:
        print()
        pprint('Do you know the following 1000 words? If so, input y; if not, input n.')
        pprint( chunk ) 
        evaluate = input()
        if evaluate == 'y':
            known_vocabulary += chunk         
        else:
            break
    return known_vocabulary

def gather_movie_vocabulary(path):   
    regex =r"[a-zA-Z]+'*[a-zA-Z]+"
    with open(path,"r") as fin:
        str = fin.read()
    return {item.lower() for item in re.findall(regex, str)}

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
