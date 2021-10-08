from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances

def tfidf (diction: dict):
    ''' Функция принимает на вход словарь и созает или пересчитывает матрицу TF/IDF метода.'''

    tfidf = TfidfVectorizer(ngram_range=(1, 4))
    tfidf_representation = tfidf.fit_transform(diction.values())
    artists_similarity = 1 - pairwise_distances(tfidf_representation, metric="cosine")
    dict_of_artist_similarity = dict(zip(diction.keys(), artists_similarity))
    return dict_of_artist_similarity
