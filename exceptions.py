import random 

def unknown():
    response = ["Can You Clarify Your Question?",
                'No Data According to My Knowladge, Try Again!',
                'Could You re-phrase Your Question?'][random.randrange(3)]
    return response
