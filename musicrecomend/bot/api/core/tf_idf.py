from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances
import logging
logging.basicConfig(filename='log.log',level=logging.INFO)

def tfidf (diction: dict) -> dict:
    tfidf = TfidfVectorizer(ngram_range=(1, 4))
    logging.info(f'{diction}')
    tfidf_representation = tfidf.fit_transform(diction.values())
    logging.info('represent_done')
    artists_similarity = 1 - pairwise_distances(tfidf_representation, metric="cosine")
    logging.info('art_sim_done')
    dict_of_artist_similarity = dict(zip(diction.keys(), artists_similarity))
    logging.info('dict_art_sim_done')
    return dict_of_artist_similarity
