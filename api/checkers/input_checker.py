def input_checker(name):
    try:
        isinstance(name, (int, str))
        return name
    except:
        print('error')
