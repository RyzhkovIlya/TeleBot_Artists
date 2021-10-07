import pandas as pd
def recommendation(name):
    df_TF_IDF = pd.read_csv('api/database/TF_IDF.csv', index_col=0)
    return '\n'.join(*[df_TF_IDF[name].sort_values(ascending=False).head(11)[1:].index.to_list()])
