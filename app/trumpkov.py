import markov

tweets = open("tweets.txt","r")

trumpkov = markov.Markov(tweets)

print(trumpkov.generate_markov_text())
