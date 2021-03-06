import os
from api.core.update_artist_names import upd_artist_name
from api.core.recommendation import recommendation
from api.core.parcer import pars
from api.core.update_dictionary_words import dict_words, dict_all_words

import pickle
from api.core.tf_idf import tfidf
import pandas as pd
import logging

logging.basicConfig(filename='log.log',level=logging.INFO)
tfidf_not_exists = 'TF_IDF.csv' not in os.listdir('bot/api/database/')
if tfidf_not_exists:
    dictionary_words = dict_all_words()
    pickle.dump(dictionary_words, open("bot/api/database/dictionary_words.pickle", "wb"))
    artists_similarity = tfidf(pickle.load(open("bot/api/database/dictionary_words.pickle", 'rb')))
    pd.DataFrame(artists_similarity, index=dictionary_words.keys()).to_csv('bot/api/database/TF_IDF.csv')

def recommender(name: str):
    '''Функция принимает на вход имя исполнителя и возвращает Топ-10 рекомендованных исполнтелей.'''
    len_parc = pars(name)
    if len_parc > 0:
        dictionary_words = dict_words(name)
        logging.info('dict_words_created')
        with open("bot/api/database/dictionary_words.pickle", "wb") as f:
            pickle.dump(dictionary_words, f)
            logging.info('dict_words_dump')
        artists_similarity = tfidf(pickle.load(open("bot/api/database/dictionary_words.pickle", 'rb')))
        logging.info('art_sim_crated')
        pd.DataFrame(artists_similarity, index=dictionary_words.keys()).to_csv('bot/api/database/TF_IDF.csv')
        logging.info('df_created')
        reccomend = recommendation(name)
        upd_artist_name(name)
        return reccomend
    else:
        return 'False'
