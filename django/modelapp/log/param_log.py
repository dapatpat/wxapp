def log(func):

    def wrapper(*args, **kwargs):
        print('-------------------------------')
        print(*kwargs)
        print(*args)
        print('-------------------------------')
        return func(*args, **kwargs)
    return wrapper
