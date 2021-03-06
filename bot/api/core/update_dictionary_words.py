import os
import pickle

from nltk.util import pr
from api.core.cleaner import clean_lemm_general

def dict_all_words():
    '''Функуия создает первичный словарь dictionary_words.'''
    dictionary_words = {}
    for i in os.listdir('bot/api/database/raw_data'):
        try:
            with open(f'bot/api/database/raw_data/{i}', encoding='utf-8', newline='') as f:
                artist_text = f.read()
                dictionary_words[i[:-4]] = clean_lemm_general(artist_text)
        except:
            print(i)
    return dictionary_words


def dict_words(name: str):
    '''Функция принимает на вход иполнителя, проверяет есть ли он в базе данных.
    Если есть, то записывает в словарь dictionary_words ключ и значние преобразованного текста его песен.'''

    if name + '.txt' in os.listdir('bot/api/database/raw_data'):
        with open(f'bot/api/database/raw_data/{name}.txt', encoding='utf-8', newline='') as f:
            artist_text = f.read()
            with open("bot/api/database/dictionary_words.pickle", 'rb') as v:
                    dictionary_words = pickle.load(v)
                    dictionary_words[name] = clean_lemm_general(artist_text)
                    outfile = open("bot/api/database/dictionary_words.pickle", 'wb')
                    pickle.dump(dictionary_words, outfile)
                    outfile.close()

            return dictionary_words
    else:
        print(False)

def del_let (name: str):
    '''Функция принимает на вход имя исполнителя и удаляет указанный ключ в словаре dictionary_words.'''

    diction = pickle.load(open("bot/api/database/dictionary_words.pickle", 'rb'))
    diction.pop(name)
    pickle.dump(diction, open("bot/api/database/dictionary_words.pickle", 'wb'))
