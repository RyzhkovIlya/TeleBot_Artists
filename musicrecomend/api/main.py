import os
from api.core.update_artist_names import upd_artist_name
from api.core.recommendation import recommendation
from api.core.parcer import pars
from api.core.update_dictionary_words import dict_words, dict_all_words
from api.checkers.name_checker import name_checker
from api.checkers.input_checker import input_checker
import pickle
from api.core.tf_idf import tfidf
import pandas as pd 

tfidf_not_exists = 'TF_IDF.csv' not in os.listdir('bot/api/database/')
if tfidf_not_exists:
    dictionary_words = dict_all_words()
    pickle.dump(dictionary_words, open("bot/api/database/dictionary_words.pickle", "wb"))
    artists_similarity = tfidf(pickle.load(open("bot/api/database/dictionary_words.pickle", 'rb')))
    pd.DataFrame(artists_similarity, index=dictionary_words.keys()).to_csv('bot/api/database/TF_IDF.csv')

def recommender(name: str):
    """
    pass
    """
    
    name = input_checker(name)
    name = name_checker(name)

    df = pd.read_csv('bot/api/database/artist_names.csv', sep='\t')

    if name in df['authors'].to_list():
        recommend = recommendation(name)
        return recommend
    if name not in df['authors'].to_list():
        pars(name)
        dictionary_words = dict_words(name)
        pickle.dump(dictionary_words, open("bot/api/database/dictionary_words.pickle", "wb"))
        artists_similarity = tfidf(pickle.load(open("bot/api/database/dictionary_words.pickle", 'rb')))
        pd.DataFrame(artists_similarity, index=dictionary_words.keys()).to_csv('bot/api/database/TF_IDF.csv')
        reccomend = recommendation(name)
        upd_artist_name(name)
        return reccomend