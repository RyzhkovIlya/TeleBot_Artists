import pandas as pd

def upd_artist_name(name: str):
    '''Функция принимает на вход имя иполнителя и обновляет список исполнителей.'''

    df = pd.read_csv('bot/api/database/artist_names.csv', sep='\t')
    df.loc[df.shape[0]+1] = name
    df.to_csv('bot/api/database/artist_names.csv', sep='\t',  index=False)
