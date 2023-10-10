import webbrowser
import time
import random


while True:
    sites = random.choice([
        'google.com',
        'youtube.com',
        'facebook.com',
        'instagram.com',
        'twitter.com',
        'instagram.com',
    ])
    webbrowser.open(sites)
    seconds = random.randrange(1,60)
    time.sleep(50)
    