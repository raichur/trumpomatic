from app import app
from app import markov
from flask import render_template
import os.path

@app.route('/')
@app.route('/index')

def index():
    script_path = os.path.dirname(__file__)
    tweets_url = "".join([script_path, '/static/tweets.txt'])
    tweets = open(tweets_url, "r")
    trumpkov = markov.Markov(tweets)
    tweet_text = trumpkov.generate_markov_text()
    return render_template('index.html', markovtext=tweet_text)
