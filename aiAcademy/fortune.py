def get_fortune():
    from random import choice
    results = ['大吉', '吉', '小吉', '凶', '大凶', '末吉']
    return choice(results)
