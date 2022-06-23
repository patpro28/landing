import random

def general_info(request):
    version = random.randint(1, 1000000000)
    return {
        'version': version,
    }
