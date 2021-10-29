import os
import re

import nltk
from nltk.stem import WordNetLemmatizer
from tqdm import tqdm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances
import pandas as pd

from api.checkers.name_checker import name_checker

def rec_music():
    return 'Меладзе'
    # pass

def clean_lemm_general(text_general):

    nltk.download('wordnet')
    def clean(text):

        text_clean_pre = text.lower()  # приводим все символы к нижнему регистру
        text_clean_pre = re.sub(r'\d+', '', text_clean_pre)  # удаляем все числа
        text_clean_pre = re.sub(r'[^\w\s]','', text_clean_pre)  # удаляем все знаки препинания
        text_clean_pre = re.sub(r'http\S+',"", text_clean_pre)
        text_clean_pre = re.sub(r'@\w+', '', text_clean_pre)
        text_clean_pre = re.sub(r'#\w+', '', text_clean_pre)
        return text_clean_pre

    text_clean_gen = [clean(i) for i in text_general.split()]
    text_lem = WordNetLemmatizer()
    lem_text = []
    for words in text_clean_gen:
        lem_text.append(' '.join([text_lem.lemmatize(word) for word in words.split()]))
    return ' '.join(lem_text)

def read_text(API_TOKEN):

    for i in tqdm(os.listdir('api/core/data')):
        os.rename(f'api/core/data/{i}', f'api/core/data/{name_checker(i[:-4], API_TOKEN)}.txt')

    text_dict = {}
    for i in os.listdir('api/core/data'):
        try:
            with open(f'api/core/data/{i}', encoding='utf-8', newline='') as f:
                artist_text = f.read()
                text_dict[i[:-4]] = clean_lemm_general(artist_text)
        except:
            print(i)
    return text_dict

# def tfidf (diction: dict) -> dict:
#
#     tfidf = TfidfVectorizer(ngram_range=(1, 4))
#     tfidf_representation = tfidf.fit_transform(diction.values())
#     artists_similarity = 1 - pairwise_distances(tfidf_representation, metric="cosine")
#     dict_of_artist_similarity = dict(zip(diction.keys(), artists_similarity))
#     return dict_of_artist_similarity

def final_df(artist_name: str, dict_artist_similary: dict, text_dict: dict) -> list[str, dict, dict]:

    df = pd.DataFrame(dict_artist_similary, index=text_dict.keys())
    return (',\n'.join([df[artist_name].sort_values(ascending=False).index[1:6]]))


