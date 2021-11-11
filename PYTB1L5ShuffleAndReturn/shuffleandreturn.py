import random

def randomise(original):
    
    randomised = ''.join(random.sample(original, len(original)))
    return randomised


print(randomise(input("vul je naam in")))
