def input_checker(name:str):
    '''Функция принимает на вход текст, проверят имеет ли введенный текст запрещенные символы или нет.'''
    
    try:
        isinstance(name, (int, str))
        return name
    except:
        print('error')
