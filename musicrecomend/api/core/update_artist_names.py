import pandas as pd
import os
def upd_artist_name(name):
    df = pd.read_csv('api/database/artist_names.csv', sep='\t')
    df.loc[df.shape[0]+1] = name
    df.to_csv('api/database/artist_names.csv', sep='\t',  index=False)
