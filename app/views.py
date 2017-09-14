from app import app
from app import markov

@app.route('/')
@app.route('/index')

def index():
    tweets = open("/users/josh/Developer/trumpkov/app/tweets.txt","r")
    trumpkov = markov.Markov(tweets)
    return trumpkov.generate_markov_text()
