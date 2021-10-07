import os
import pickle
from api.core.cleaner import clean_lemm_general

def dict_all_words():
    dictionary_words = {}
    for i in os.listdir('api/database/raw_data'):
        try:
            with open(f'api/database/raw_data/{i}', encoding='utf-8', newline='') as f:
                artist_text = f.read()
                dictionary_words[i[:-4]] = clean_lemm_general(artist_text)
        except:
            print(i)
    return dictionary_words


def dict_words(name: str):
    if name + '.txt' in os.listdir('api/database/raw_data'):
        with open(f'api/database/raw_data/{name}.txt', encoding='utf-8', newline='') as f:
            artist_text = f.read()
            dictionary_words = pickle.load(open("api/database/dictionary_words.pickle", 'rb'))
            dictionary_words[name] = clean_lemm_general(artist_text)
            pickle.dump(dictionary_words, open("api/database/dictionary_words.pickle", 'wb'))
            return dictionary_words
    else:
        print(False)

def del_let (name: str):
     diction = pickle.load(open("../database/dictionary_words.pickle", 'rb'))
     diction.pop(name)
     pickle.dump(diction, open("../database/dictionary_words.pickle", 'wb'))

#del_let('Юлия Кадышева (Yulia Kadysheva)')
#del_let('Алла Пугачёва (Alla Pugacheva)')
#del_let('FACE')
