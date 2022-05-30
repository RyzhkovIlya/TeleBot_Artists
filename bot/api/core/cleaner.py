# from pymorphy2 import MorphAnalyzer
import nltk
import re
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords # стопслова

nltk.download('wordnet', 'nltk_data')
nltk.data.path.append('nltk_data')
nltk.download('stopwords')


def clean_lemm_general(text_general:str):
    '''Функция принимает на вход текст песен исполнителя и возвращает преобразованный текст его песен.'''
    
    def clean(text:str):
        '''Функция принимает на вход текст песен исполнителей и возвращает очищенный от лишних слов текст песен исполнителя.'''
        re_br = re.compile(r'<\s*br\s*/?>', re.IGNORECASE)
        text_clean_pre = text.lower()  # приводим все символы к нижнему регистру
        text_clean_pre = re.sub(r'\d+', '', text_clean_pre)  # удаляем все числа
        text_clean_pre = re.sub(r'[^\w\s]','', text_clean_pre)  # удаляем все знаки препинания
        text_clean_pre = re.sub(r'http\S+',"", text_clean_pre)
        text_clean_pre = re.sub(r'@\w+', '', text_clean_pre)
        text_clean_pre = re.sub(r'#\w+', '', text_clean_pre)
        return text_clean_pre
    text_clean_gen = [clean(i) for i in text_general.split()]
    text_lem = WordNetLemmatizer()
    # morph = MorphAnalyzer()
    sw_rus = stopwords.words('russian') # список стоп-слов 
    sw_eng = stopwords.words('english')
    lem_text = []
    # for words in text_clean_gen:
    #     morph_text.append(' '.join([morph.parse(word)[0].normal_form for word in words.split() if word not in sw_rus]))
    for words in text_clean_gen:
        lem_text.append(' '.join([text_lem.lemmatize(word) for word in words.split() if word not in sw_eng or word not in sw_rus]))
    return (' '.join(lem_text))
