from app import app
from app import markov
import os.path

@app.route('/')
@app.route('/index')

def index():
    script_path = os.path.dirname(__file__)
    tweets_url = "".join([script_path, '/static/tweets.txt'])
    tweets = open(tweets_url, "r")
    trumpkov = markov.Markov(tweets)
    return trumpkov.generate_markov_text()
