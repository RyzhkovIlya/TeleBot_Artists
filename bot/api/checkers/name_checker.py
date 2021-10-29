import lyricsgenius as lg
from api.loader import API_TOKEN

def name_checker(name_artist: str, API_TOKEN=API_TOKEN):
    '''Функция принимает на вход имя исполнителя и возвращает исправленное имя исполнителя,
    если оно нуждается в исправлении, иначе возвращает входное имя
    '''
    
    try:
        genius = lg.Genius(API_TOKEN, skip_non_songs=True, remove_section_headers=True)
        response = genius.search_artist(name_artist, max_songs=0, sort='popularity')
        true_name = response.name
        return true_name
    except:
        return name_artist