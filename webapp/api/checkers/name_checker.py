import lyricsgenius as lg
from api.loader import API_TOKEN

def name_checker(name_artist, API_TOKEN=API_TOKEN):
    try:
        genius = lg.Genius(API_TOKEN, skip_non_songs=True, remove_section_headers=True)
        response = genius.search_artist(name_artist, max_songs=0, sort='popularity')
        true_name = response.name
        return true_name
    except:
        return name_artist
        
# import lyricsgenius as lg
# from joblib import Parallel, delayed
#
# def name_checker(names):
#     res = []
#     for i in names:
#         try:
#             genius = lg.Genius(API_TOKEN, skip_non_songs=True, remove_section_headers=True)
#             name = (genius.search_artist(i, max_songs=1, allow_name_change=True)).name
#             res.append(name)
#         except:
#             print('error')
#     Parallel(n_jobs=20, verbose=1)(delayed(name_checker)(i) for i in names)
#
#     return res