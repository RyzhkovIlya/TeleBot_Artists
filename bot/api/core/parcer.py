from api.loader import API_TOKEN
import lyricsgenius as lg

def get_lyrics(name:str, k=20):
    '''Функция приниамет на вход исполнителя и количество песен, которое неоходимо запарсить (по умолчанию 20)'''

    c = 0
    try:
        genius = lg.Genius(API_TOKEN,skip_non_songs=True, excluded_terms=["(Remix)", "(Live)"], remove_section_headers=True, retries=2)
        response = genius.search_artist(name, max_songs=k, sort='popularity')
        songs = response.songs
        s = [song.lyrics for song in songs]
        name_1 = response.name
        with open(f"bot/api/database/raw_data/{name_1}.txt", "w", encoding='utf-8') as f:
            f.write("\n \n".join(s))
        c += 1
        print(f"Songs grabbed:{len(s)}")
        return len(s)
    except:
        print(f"some exception at {name}: {c}")

def pars(name: str):
    '''Функция принимает на вход имя исполнителя и возвращет результат функции get_lyrics.'''

    return get_lyrics(name, 20)
