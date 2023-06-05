import random 

def unknown():
    response = ['Can You Clarify Your Question?',
                'No Informattion According to My Knowladge',
                '...'][random.randrange(3)]
    return response
