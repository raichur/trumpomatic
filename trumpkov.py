import markov

tweets = open("/Users/josh/Developer/trumpkov/tweets.txt","r")

trumpkov = markov.Markov(tweets)

print(trumpkov.generate_markov_text())
